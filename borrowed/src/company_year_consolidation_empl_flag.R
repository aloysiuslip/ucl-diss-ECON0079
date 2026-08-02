## ======================================================================
## BUILD COMPANY–YEAR PANEL (CONSOLIDATION + EMPLOYMENT)
## - Reads FAME Excel exports (sheet: "Results")
## - Extracts consolidation status and number of employees by year
## - Outputs a clean company–year panel
## ======================================================================

rm(list = ls())
library(data.table)
library(readxl)
library(stringr)

## ----------------------------------------------------------------------
## 1. Paths, years, output folder
## ----------------------------------------------------------------------

# root directory containing industry folders (01, 02, ...)
root_dir <- "C:/Users/aitor/Dropbox/supergrassi/data/uk_data_financial_accounts/2025.02"

# years to keep
years    <- 2006:2023

# output directory for derived datasets
out_dir  <- file.path(root_dir, "_company_year_consolidation_empl_flag")
dir.create(out_dir, showWarnings = FALSE)

# industries to process (start small for testing)
inds <- c(61)
#inds <- c("01","02","03","05","06","07","08","09",10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,37,38,39,41,42,43,45,46,47,49,50,51,52,53,55,56,58,59,60,61,62,63,64,65,66,68,69,70,71,72,73,74,75,77,78,79,80,81,82,84,85,86,87,88,90,91,92,93,94,95,96,97,98,99)
#inds <- c(58,59,60,61,62,63,64,65,66,68,69,70,71,72,73,74,75,77,78,79,80,81,82,84,85,86,87,88,90,91,92,93,94,95,96,97,98,99)
#inds <- c(56,91,94,96)


## ----------------------------------------------------------------------
## 2. Read ONE Excel file → company–year rows
## Each Excel file is wide (one column per year). This function reshapes it into a proper company–year dataset.
## ----------------------------------------------------------------------
read_one <- function(path, years) {
  
  # Read Results sheet as text to avoid type-guessing issues
  dt <- as.data.table(read_excel(path, sheet = "Results",col_types = "text",.name_repair = "minimal"))
  if (!nrow(dt)) return(NULL)
  
  # Identify consolidation and employment columns by year
  cons_cols <- intersect(paste0("Cons./Uncons.\n", years), names(dt))
  emp_cols  <- intersect(paste0("Number of employees\n", years), names(dt))
  if (!length(cons_cols) && !length(emp_cols)) return(NULL)
  
  # Keep only identifiers + relevant variables
  keep <- intersect(c("Registered number", "Company name", cons_cols, emp_cols),names(dt))
  
  # Drop file if it has no usable identifier
  if (!("Registered number" %in% keep) && !("Company name" %in% keep)) return(NULL)
  dt <- dt[, ..keep]
  
  # ID variables that actually exist in this file
  id_vars <- intersect(c("Registered number", "Company name"), names(dt))
  
  ## --------------------------------------------------------------
  ## 2a. Consolidation: wide → long → clean
  ## --------------------------------------------------------------
  cons_long <- NULL
  if (length(cons_cols)) {
    cons_long <- melt(dt,id.vars = id_vars,measure.vars = cons_cols,variable.name = "var",value.name = "v")
    
    # Extract year from column name
    cons_long[, year := as.integer(str_extract(as.character(var), "\\d{4}$"))]
    cons_long <- cons_long[year %in% years]
    
    # Recode consolidation to numeric flag
    cons_long[, consolidated := fifelse(trimws(v) == "Consolidated", 1L,fifelse(trimws(v) == "Unconsolidated", 0L, NA_integer_))]
    cons_long[, c("var","v") := NULL]
  }
  
  ## --------------------------------------------------------------
  ## 2b. Employment: wide → long → clean
  ## --------------------------------------------------------------
  emp_long <- NULL
  if (length(emp_cols)) {
    emp_long <- melt(dt,id.vars = id_vars,measure.vars = emp_cols,variable.name = "var",value.name = "v")
    emp_long[, year := as.integer(str_extract(as.character(var), "\\d{4}$"))]
    emp_long <- emp_long[year %in% years]
    
    # Convert employment to numeric
    emp_long[, employees := suppressWarnings(as.numeric(gsub(",", "", v)))]
    emp_long[, c("var","v") := NULL]
  }
  
  ## --------------------------------------------------------------
  ## 2b.5 Collapse duplicates BEFORE merging (prevents cartesian joins)
  ## --------------------------------------------------------------
  if (!is.null(cons_long)) {
    cons_long <- cons_long[, .(
      consolidated = consolidated[which.max(!is.na(consolidated))]
    ), by = c(id_vars, "year")]
  }
  
  if (!is.null(emp_long)) {
    emp_long <- emp_long[, .(
      employees = employees[which.max(!is.na(employees))]
    ), by = c(id_vars, "year")]
  }
  
  ## --------------------------------------------------------------
  ## 2c. Merge consolidation and employment into one table
  ## --------------------------------------------------------------
  wide <- if (!is.null(cons_long) && !is.null(emp_long)) {
    merge(cons_long, emp_long, by = c(id_vars, "year"), all = TRUE)
  } else if (!is.null(cons_long)) {
    cons_long[, employees := NA_real_]
  } else {
    emp_long[, consolidated := NA_integer_]
  }
  
  ## --------------------------------------------------------------
  ## 2d. Standardise identifiers and drop unusable rows
  ## --------------------------------------------------------------
  setnames(wide,c("Registered number", "Company name"),c("registered_number", "company_name"),skip_absent = TRUE)
  
  if (!("registered_number" %in% names(wide))) wide[, registered_number := NA_character_]
  if (!("company_name" %in% names(wide)))      wide[, company_name := NA_character_]
  
  # Treat empty strings as missing
  wide[, registered_number := fifelse(registered_number == "", NA_character_, registered_number)]
  wide[, company_name      := fifelse(company_name == "",      NA_character_, company_name)]
  
  # Keep rows with at least one identifier
  wide <- wide[!(is.na(registered_number) & is.na(company_name))]
  
  # Return only required variables
  wide[, .(company_name, registered_number, year, consolidated, employees)]
}

## ----------------------------------------------------------------------
## 3. Build ONE industry dataset
## Firms appear in multiple Excel exports; we collapse them to one row per company–year within each industry.
## ----------------------------------------------------------------------
build_industry <- function(ind) {
  
  dir_fin <- file.path(root_dir, ind, "a2_key_finance")
  files <- list.files(dir_fin, pattern = "\\.xlsx$", full.names = TRUE)
  if (!length(files)) return(NULL)
  
  # Read all Excel files for the industry
  x <- rbindlist(lapply(files, read_one, years = years), fill = TRUE)
  if (!nrow(x)) return(NULL)
  
  ## --------------------------------------------------------------
  ## 3a. Deduplicate company–year rows
  ##     Rule: prefer rows with non-missing consolidation and employment
  ## --------------------------------------------------------------
  x[, has_cons := as.integer(!is.na(consolidated))]
  x[, has_emp  := as.integer(!is.na(employees))]
  
  setorder(x, registered_number, company_name, year, -has_cons, -has_emp)
  x <- x[, .SD[1], by = .(registered_number, company_name, year)]
  
  x[, c("has_cons","has_emp") := NULL]
  setorder(x, registered_number, company_name, year)
  
  # Save industry-level output
  fwrite(x, file.path(out_dir, paste0("company_year_cons_empl_", ind, ".csv")))
  x
}

## ----------------------------------------------------------------------
## 4. Run selected industries
## ----------------------------------------------------------------------
for (ind in inds) build_industry(ind)

## ----------------------------------------------------------------------
## 5. Combine industries + final deduplication
## The same firm may appear in multiple industries.
## ----------------------------------------------------------------------
files <- file.path(out_dir, paste0("company_year_cons_empl_", inds, ".csv"))
dt_all <- rbindlist(lapply(files[file.exists(files)], fread), fill = TRUE)

dt_all[, has_cons := as.integer(!is.na(consolidated))]
dt_all[, has_emp  := as.integer(!is.na(employees))]

setorder(dt_all, registered_number, company_name, year, -has_cons, -has_emp)
final_panel <- dt_all[, .SD[1], by = .(registered_number, company_name, year)]

final_panel[, c("has_cons","has_emp") := NULL]
setorder(final_panel, registered_number, company_name, year)

## ----------------------------------------------------------------------
## 6. Save final company–year panel
## ----------------------------------------------------------------------
fwrite(final_panel, file.path(out_dir, "company_year_consolidation_empl_final.csv"))





#########################################################################################
#########################################################################################
#########################################################################################


library(data.table)

out_dir <- "C:/Users/aitor/Dropbox/supergrassi/data/uk_data_financial_accounts/2025.02/_company_year_consolidation_empl_flag"

## ----------------------------------------------------------------------
## 5. Combine ALL industry files + final deduplication (with progress)
## ----------------------------------------------------------------------
files <- list.files(
  out_dir,
  pattern = "^company_year_cons_empl_[0-9]+\\.csv$",
  full.names = TRUE
)

stopifnot(length(files) > 0)

message("Combining ", length(files), " industry files...")

dt_list <- vector("list", length(files))

for (i in seq_along(files)) {
  message(sprintf("  [%d / %d] Reading %s",
                  i, length(files), basename(files[i])))
  dt_list[[i]] <- fread(files[i])
}

dt_all <- rbindlist(dt_list, use.names = TRUE, fill = TRUE)
rm(dt_list)  # free memory

## Prefer rows with non-missing info
dt_all[, has_cons := as.integer(!is.na(consolidated))]
dt_all[, has_emp  := as.integer(!is.na(employees))]

setorder(dt_all, registered_number, company_name, year, -has_cons, -has_emp)
final_panel <- dt_all[, .SD[1], by = .(registered_number, company_name, year)]

final_panel[, c("has_cons","has_emp") := NULL]
setorder(final_panel, registered_number, company_name, year)

## ----------------------------------------------------------------------
## 6. Save final dataset
## ----------------------------------------------------------------------
fwrite(final_panel,
       file.path(out_dir, "company_year_consolidation_empl_final.csv"))

message("Done. Firms = ", uniqueN(final_panel$registered_number),
        ", rows = ", nrow(final_panel))











