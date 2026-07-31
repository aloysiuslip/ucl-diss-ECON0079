################################################################################
## Combining new variables (extracted in August 2025) 
## Prepared by AIF, 2025-08-14
################################################################################

################################################################################
## 1) Set up: clear environment, load libraries / packages, define directories
################################################################################
rm(list = ls())  # clear environment

# set personal library path
user_lib <- file.path(Sys.getenv("USERPROFILE"), "R", "win-library", paste0(R.version$major, ".", R.version$minor))
dir.create(user_lib, recursive = TRUE, showWarnings = FALSE)
.libPaths(c(user_lib, .libPaths()))

# define required packages
packages <- c("readxl", "dplyr", "openxlsx", "purrr", "stringr", "janitor", "writexl", "tidyr", "lubridate", "ggplot2")

# install packages not yet installed 
installed_packages <- packages %in% rownames(installed.packages())
if (any(!installed_packages)) install.packages(packages[!installed_packages])

# load all packages
invisible(lapply(packages, library, character.only = TRUE))

# define paths
user <- "aitor_f"
dirs <- list()
dirs$root <- paste0("/Users/", user, "/Dropbox/supergrassi")
dirs$work <- paste0(dirs$root, "/data/uk_data_financial_accounts")
dirs$data <- paste0(dirs$root, "/data/uk_data_financial_accounts/2025.07.30")
dirs$output <- paste0(dirs$root, "/data/uk_data_financial_accounts/2025.07.30/output")
dir.create(dirs$output, recursive = TRUE, showWarnings = FALSE)

# list industry subfolders as they exists (e.g. 01_11, 12_20, 21,...)
#industries <- c("01_12", "70")
industries <- list.dirs(dirs$data, full.names = FALSE, recursive = FALSE)

# ---------------------------------------------------------------------------
# Load the CLEAN data (Excel) just to get the IDs we’ll merge with
# ---------------------------------------------------------------------------

clean_path <- "C:/Users/aitor_f/Dropbox/supergrassi/data/uk_data_financial_accounts/AnalyseFAME3_2025_02/output/master_panel.xlsx"
message("Reading clean dataset from: ", clean_path)
clean_current <- readxl::read_xlsx(clean_path)

# Make names consistent, and keep only IDs 
clean_current <- janitor::clean_names(clean_current)

# Some exports store registered_number as numeric—coerce to character.
clean_current <- clean_current %>%
  mutate(
    registered_number = as.character(registered_number),
    company_name      = as.character(company_name)
  )

# This is the set of firms we actually care about (for early filtering).
# If registered_number is missing, fall back to company_name (rare but possible).
keep_ids <- clean_current %>%
  transmute(
    merge_id = dplyr::coalesce(dplyr::na_if(registered_number, ""), company_name)
  ) %>%
  filter(!is.na(merge_id), merge_id != "") %>%
  distinct()

# Do we also have year in the clean dataset? If yes, we’ll use it for the final merge.
has_year_in_clean <- "year" %in% names(clean_current)

# Don’t write huge intermediates unless you explicitly flip these:
SAVE_PER_INDUSTRY <- FALSE
SAVE_MASTER       <- FALSE   # you asked not to save the giant combined set





################################################################################
## 2) Helper functions
################################################################################

##################
# Function to standardize data types (i.e. a variable with different data types, e.g. numeric and character)
##################
standardize_column_types <- function(df, except = c("status_date","date_of_incorporation", "accounting_reference_date")) {
  df_names <- names(df)
  non_date_vars <- setdiff(df_names, except)
  df[non_date_vars] <- lapply(df[non_date_vars], as.character)
  for (nm in intersect(except, df_names)) df[[nm]] <- as.character(df[[nm]])
  df
}

###################
# Function to read and clean the 'Results' sheet from each Excel file
###################
read_and_clean_excel <- function(file_path) {
  out <- tryCatch(
    readxl::read_excel(file_path, sheet = "Results", col_types = "text"),
    error = function(e) {
      message("  ! Skipping (can’t read 'Results'): ", basename(file_path))
      return(NULL)
    }
  )
  if (is.null(out)) return(NULL)
  out <- out[, !duplicated(colnames(out)), drop = FALSE]
  names(out) <- gsub("\\.\\.\\d+$", "", names(out))
  names(out) <- gsub("\\.$", "", names(out))
  out <- janitor::clean_names(out)
  standardize_column_types(out)
}


# Parse Excel-serial or ISO/UK/US date strings into Date (for normal dates)
parse_excel_or_iso_date <- function(x) {
  if (is.null(x)) return(as.Date(NA))
  x <- as.character(x)
  as_num <- suppressWarnings(as.numeric(x))
  out <- rep(as.Date(NA), length(x))
  is_serial <- !is.na(as_num)
  if (any(is_serial)) out[is_serial] <- as.Date(as_num[is_serial], origin = "1899-12-30")
  to_parse <- which(!is_serial & !is.na(x) & nzchar(trimws(x)))
  if (length(to_parse)) {
    xx <- trimws(x[to_parse])
    d <- suppressWarnings(lubridate::dmy(xx, quiet = TRUE))          # UK first
    miss <- is.na(d)
    if (any(miss)) d[miss] <- suppressWarnings(lubridate::ymd(xx[miss], quiet = TRUE))
    miss <- is.na(d)
    if (any(miss)) d[miss] <- suppressWarnings(lubridate::mdy(xx[miss], quiet = TRUE))
    out[to_parse] <- d
  }
  out
}

# For accounting reference: output simple "mm-dd" strings (month-day only)
parse_accounting_reference_md_str <- function(x) {
  if (is.null(x)) return(NA_character_)
  x_chr <- as.character(x)
  out <- rep(NA_character_, length(x_chr))
  
  # Excel serials
  as_num <- suppressWarnings(as.numeric(x_chr))
  is_serial <- !is.na(as_num)
  if (any(is_serial)) {
    d <- as.Date(as_num[is_serial], origin = "1899-12-30")
    out[is_serial] <- format(d, "%m-%d")
  }
  
  # Non-serials
  idx <- which(!is_serial & !is.na(x_chr) & nzchar(trimws(x_chr)))
  if (length(idx)) {
    xx <- trimws(x_chr[idx])
    
    # try full dates first (dmy -> ymd -> mdy)
    d_full <- suppressWarnings(lubridate::dmy(xx, quiet = TRUE))
    miss <- is.na(d_full)
    if (any(miss)) d_full[miss] <- suppressWarnings(lubridate::ymd(xx[miss], quiet = TRUE))
    miss <- is.na(d_full)
    if (any(miss)) d_full[miss] <- suppressWarnings(lubridate::mdy(xx[miss], quiet = TRUE))
    
    # if only d/m without year, append a dummy year (2000) and parse
    no_year <- is.na(d_full) & grepl("^\\d{1,2}/\\d{1,2}$", xx)
    if (any(no_year)) {
      dm <- paste0(xx[no_year], "/2000")
      d_dm <- suppressWarnings(lubridate::dmy(dm, quiet = TRUE))
      d_full[no_year] <- d_dm
    }
    
    out[idx] <- ifelse(is.na(d_full), NA_character_, format(d_full, "%m-%d"))
  }
  
  out
}


# Ensure date vars are parsed; accounting_reference_date becomes "mm-dd"
fix_date_vars <- function(df) {
  if (!("status_date" %in% names(df))) df$status_date <- NA_character_
  if (!("date_of_incorporation" %in% names(df))) df$date_of_incorporation <- NA_character_
  if (!("accounting_reference_date" %in% names(df))) df$accounting_reference_date <- NA_character_
  
  df$status_date <- parse_excel_or_iso_date(df$status_date)
  df$date_of_incorporation <- parse_excel_or_iso_date(df$date_of_incorporation)
  df$accounting_reference_date <- parse_accounting_reference_md_str(df$accounting_reference_date)
  
  df
}


################################################################################
## 3) Main loop across subfolders and industries
################################################################################

# define years (year 2024 is also available but incomplete for some firms)
years <- 2006:2023

# list of fixed variables (fixed meaning same info for all available years)
fixed_vars <- c("company_name", "registered_number", "inactive", "quoted", "own_data", "woco",
                "bv_d_id_number", "company_status", "status_date", "legal_form", "date_of_incorporation",
                "accounting_reference_date", "registered_accounts_type", "jordans_company_classification", 
                "account_currency", "guo_name", "guo_bv_d_id_number", "duo_name", "duo_bv_d_id_number")


# list of yearly variables (from 2006 to 2023)
yearly_vars <- c(
  cost_of_sales_th_gbp                     = "cost_of_sales_th_gbp",
  exceptional_items_pre_gp_th_gbp          = "exceptional_items_pre_gp_th_gbp",
  cash_out_in_flow_investing_activ_th_gbp  = "cash_out_in_flow_investing_activ_th_gbp",
  capital_expenditure_financ_invest_th_gbp = "capital_expenditure_financ_invest_th_gbp",
  acquisition_disposal_th_gbp              = "acquisition_disposal_th_gbp",
  equity_dividends_paid_th_gbp             = "equity_dividends_paid_th_gbp"
)


# key for dedupe (include year only if present in clean)
key_vars <- if (has_year_in_clean) c(fixed_vars, "year") else fixed_vars

all_industries_panels <- vector("list", length(industries))
names(all_industries_panels) <- industries

for (industry in industries) {
  cat("\n=== Processing industry:", industry, "===\n")
  
  folder_path <- file.path(dirs$data, industry)
  excel_files <- list.files(folder_path, pattern = "\\.xlsx$", full.names = TRUE)
  
  if (!length(excel_files)) {
    message("  (no Excel files found)")
    next
  }
  
  # Read all files; compact to drop NULLs
  lst <- purrr::map(excel_files, read_and_clean_excel) |> purrr::compact()
  if (!length(lst)) {
    message("  (no readable 'Results' sheets)")
    next
  }
  
  # Row-bind (NOT join), remove exact duplicates
  merged_data <- dplyr::bind_rows(lst) |> distinct()
  
  # Early filter to the set of firms you actually care about (if provided)
  if (!is.null(keep_ids)) {
    merged_data <- merged_data %>%
      mutate(merge_id = dplyr::coalesce(dplyr::na_if(registered_number, ""), company_name)) %>%
      dplyr::semi_join(keep_ids, by = "merge_id")
  }
  
  
  # Safe names (and strip .x remnants from accidental earlier joins)
  names(merged_data) <- make.names(names(merged_data), unique = TRUE)
  names(merged_data) <- stringr::str_replace_all(names(merged_data), "\\.x(\\.\\.\\d+)?$", "")
  
  # Build long panel by reducing left_joins on melted variables
  panel <- purrr::reduce(
    purrr::imap(yearly_vars, function(pattern, varname) {
      merged_data |>
        select(any_of(fixed_vars), matches(pattern)) |>
        tidyr::pivot_longer(
          cols = matches(pattern),
          names_to   = "year",
          names_pattern = paste0("^", varname, "_?(\\d{4})$"),
          values_to  = varname
        ) |>
        filter(year %in% as.character(years))
    }),
    .f = dplyr::left_join,
    by = c(fixed_vars, "year")
  )
  
  # Numeric conversion for the yearly columns we just created
  panel <- panel |>
    mutate(across(all_of(names(yearly_vars)), ~ suppressWarnings(as.numeric(.))))
  
  # Fix dates
  panel <- fix_date_vars(panel)
  
  #  De-dupe within-industry by business key
  panel <- panel %>%
    distinct(across(all_of(key_vars)), .keep_all = TRUE)
  
  # Store in memory
  all_industries_panels[[industry]] <- panel
  
  # Optional per-industry write (off by default)
  if (SAVE_PER_INDUSTRY) {
    writexl::write_xlsx(panel, file.path(dirs$output, paste0("industry_", industry, ".xlsx")))
  }
  
  rm(lst, merged_data, panel); gc()
}

cat("\n✅ Finished per-industry processing (objects kept in memory).\n")


## 5) Merge with the clean dataset and SAVE ONLY the smaller result ------------
master_panel <- bind_rows(all_industries_panels, .id = "industry_folder") %>%
  distinct(across(all_of(key_vars)), .keep_all = TRUE) 

cat("Industries processed:", length(all_industries_panels), "\n")
cat("Rows in master_panel:", nrow(master_panel), "\n")


master_dups <- master_panel %>%
  mutate(merge_id = dplyr::coalesce(dplyr::na_if(registered_number, ""), company_name)) %>%
  {
    if (has_year_in_clean) count(., merge_id, year, name = "n") else count(., merge_id, name = "n")
  } %>%
  filter(n > 1)
cat("Duplicate key combos in master_panel: ", nrow(master_dups), "\n")   ## CHANGED
if (nrow(master_dups) > 0) print(utils::head(master_dups, 10)) 



# Build comparable keys on both sides
clean_keys <- clean_current %>%
  mutate(
    merge_id = dplyr::coalesce(dplyr::na_if(registered_number, ""), company_name)
  ) %>%
  { if (has_year_in_clean) dplyr::select(., merge_id, year, company_name) else dplyr::select(., merge_id, company_name) } %>%
  distinct()

mp_keys <- master_panel %>%
  mutate(
    merge_id = dplyr::coalesce(dplyr::na_if(registered_number, ""), company_name)
  ) %>%
  { if (has_year_in_clean) dplyr::select(., merge_id, year) else dplyr::select(., merge_id) } %>%
  distinct()

# Row-level (firm-year if year available) matches / non-matches
matched_pairs   <- dplyr::semi_join(clean_keys, mp_keys, by = intersect(names(clean_keys), names(mp_keys)))
unmatched_pairs <- dplyr::anti_join(clean_keys, mp_keys, by = intersect(names(clean_keys), names(mp_keys)))

n_matched   <- nrow(matched_pairs)
n_unmatched <- nrow(unmatched_pairs)

cat("Merge diagnostics — row level:\n")
cat("  Matched rows:   ", n_matched, "\n")
cat("  Unmatched rows: ", n_unmatched, "\n")

# Firm-level unique matches / non-matches (ignores year)
clean_firms <- clean_current %>%
  mutate(merge_id = dplyr::coalesce(dplyr::na_if(registered_number, ""), company_name)) %>%
  distinct(merge_id, company_name)

mp_firms <- master_panel %>%
  mutate(merge_id = dplyr::coalesce(dplyr::na_if(registered_number, ""), company_name)) %>%
  distinct(merge_id)

matched_firms   <- dplyr::semi_join(clean_firms, mp_firms, by = "merge_id")
unmatched_firms <- dplyr::anti_join(clean_firms, mp_firms, by = "merge_id")

n_matched_firms   <- nrow(matched_firms)
n_unmatched_firms <- nrow(unmatched_firms)

cat("Merge diagnostics — firm level (unique firms):\n")
cat("  Matched firms:   ", n_matched_firms, "\n")
cat("  Unmatched firms: ", n_unmatched_firms, "\n")

# Save the unique list of firms that did not merge (one row per firm)
# (You asked for the name just once — we keep merge_id + company_name, unique.)
not_merged_firms_path <- file.path(dirs$output, "firms_not_merged_unique.xlsx")
writexl::write_xlsx(unmatched_firms, not_merged_firms_path)
cat("📄 Wrote unique firms not merged to: ", not_merged_firms_path, "\n")



# Ensure comparable types for merging on year if present
if (has_year_in_clean) {
  # clean_current$year might be numeric/integer; align master_panel
  master_panel <- master_panel %>% mutate(year = as.integer(year))
  clean_current <- clean_current %>% mutate(year = as.integer(year))
  final_merged <- clean_current %>%
    mutate(
      registered_number = as.character(registered_number),
      company_name      = as.character(company_name),
      merge_id          = dplyr::coalesce(dplyr::na_if(registered_number, ""), company_name)
    ) %>%
    left_join(
      master_panel %>%
        mutate(merge_id = dplyr::coalesce(dplyr::na_if(registered_number, ""), company_name)) %>%
        select(-registered_number, -company_name),
      by = c("merge_id","year")
    ) %>%
    select(-merge_id)
} else {
  final_merged <- clean_current %>%
    mutate(
      registered_number = as.character(registered_number),
      company_name      = as.character(company_name),
      merge_id          = dplyr::coalesce(dplyr::na_if(registered_number, ""), company_name)
    ) %>%
    left_join(
      master_panel %>%
        mutate(merge_id = dplyr::coalesce(dplyr::na_if(registered_number, ""), company_name)) %>%
        select(-registered_number, -company_name),
      by = "merge_id"
    ) %>%
    select(-merge_id)
}

# Save ONLY the merged result (RDS recommended; XLSX optional if small enough)
writexl::write_xlsx(final_merged, file.path(dirs$output, "merged_all_variables_2025_08_27.xlsx"))

cat("\n📦 Saved merged result only. Objects in memory: `master_panel`, `final_merged`.\n")

cat("Rows clean_current vs final_merged: ", nrow(clean_current), " vs ", nrow(final_merged), "\n")