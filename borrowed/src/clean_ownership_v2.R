## ======================================================================
## OWNERSHIP DATA (2006-2023) BY INDUSTRY (BLOCK-BY-BLOCK VERSION)
## ======================================================================

rm(list = ls())  # clear environment

user_lib <- "C:/Users/aitor_f/Documents/R/win-library/4.4"
dir.create(user_lib, recursive = TRUE, showWarnings = FALSE)
.libPaths(user_lib)
.libPaths()

install.packages(c("dplyr", "tidyverse", "readxl", "stringr"))
library(tidyverse)
library(readxl)
library(stringr)
library(data.table)

# Base folder that contains all the industry subfolders: "01", "02",..., "99"
base_dir <- "C:/Users/aitor_f/Dropbox/supergrassi/data/uk_data_financial_accounts/OwnershipFAME"

process_industry <- function(ind_code) {
  
  message("Processing industry: ", ind_code)
  data_dir <- file.path(base_dir, ind_code)
  outfile  <- file.path(base_dir, paste0("ownership_ind", ind_code, ".csv"))
  
  # All Excel files in this industry's folder
  xlsx_files <- list.files(path = data_dir, pattern = "\\.xlsx$", full.names = TRUE)
  if (length(xlsx_files) == 0L) {
    message("  No .xlsx files found in ", data_dir, " -- skipping.")
    return(invisible(NULL))
  }
  
  ## --------------------------------------------------------------------
  ## Helper 0: read + standardise one "Results" sheet
  ## --------------------------------------------------------------------
  read_results_clean <- function(path) {
    raw <- read_excel(path, sheet = "Results")
    
    raw %>% select(-1) %>%  
      rename(
        Company_name        = `Company name`,
        BvD_ID_number       = `BvD ID number`,
        SH_Name             = `SH - Name`,
        SH_BvD_ID_number    = `SH - BvD ID number`,
        SH_Country_ISO_code = `SH - Country ISO code`,
        SH_Type             = `SH - Type`
      ) %>%
      tidyr::fill(Company_name, BvD_ID_number, .direction = "down") %>%
      rename_with(~ str_replace(.x, "^SH - Direct %\\n12/(\\d{4})$", "SH_Direct_\\1"),starts_with("SH - Direct"))
  }
  
  ## --------------------------------------------------------------------
  ## Helper 1: ownership codes -> numeric
  ## --------------------------------------------------------------------
  ownership_to_numeric <- function(x) {
    raw <- trimws(as.character(x))
    
    dplyr::case_when(
      raw %in% c("-", "")                    ~ NA_real_,     # no info
      raw %in% c("NA", "n.a", "na")          ~ NA_real_,
      raw %in% c("WO", "BR")                 ~ 100,
      raw %in% c("MO", "CQP1", ">50.00")     ~ 50.01,
      raw == ">25.00"                        ~ 25.01,
      raw == "NG"                            ~ 0.01,
      TRUE ~ suppressWarnings(readr::parse_number(raw))
    )
  }
  
  ## --------------------------------------------------------------------
  ## Parse filenames into blocks: industry_41_block_1_0614.xlsx, etc.
  ## --------------------------------------------------------------------
  file_info <- tibble(path = xlsx_files,fname = basename(path)) %>%
    mutate(
      block  = stringr::str_match(fname, "_block_(\\d+)_")[, 2],
      period = stringr::str_match(fname, "_(0614|1523)\\.xlsx$")[, 2]
    )
  
  blocks <- sort(unique(file_info$block))
  message("  Found blocks: ", paste(blocks, collapse = ", "))
  
  if (any(is.na(blocks))) {
    stop("Some files do not match the expected '..._block_<n>_0614/1523.xlsx' pattern.")
  }
  
  # list to store block-level panels
  block_panels <- vector("list", length(blocks))
  
  ## ====================================================================
  ## LOOP OVER BLOCKS
  ## ====================================================================
  for (i in seq_along(blocks)) {
    b <- blocks[i]
    block_id <- as.integer(b)
    message("  Processing block ", b)
    
    files_b <- file_info %>% filter(block == b)
    
    path_0614 <- files_b$path[files_b$period == "0614"]
    path_1523 <- files_b$path[files_b$period == "1523"]
    
    if (length(path_0614) != 1L || length(path_1523) != 1L) {
      stop("Block ", b, ": expected exactly one 0614 and one 1523 file.")
    }
    
    # ---- read both period files for this block ----
    df_0614 <- read_results_clean(path_0614)
    df_1523 <- read_results_clean(path_1523)
    
    id_cols <- c("Company_name","BvD_ID_number","SH_Name",
                 "SH_BvD_ID_number","SH_Country_ISO_code","SH_Type")
    
    # merge 2006–2014 and 2015–2023 for THIS block’s firms
    firms_wide <- dplyr::full_join(df_0614, df_1523, by = id_cols)
    
    # original firm order inside this block (based on first appearance)
    firm_order <- firms_wide %>%
      mutate(row_id = dplyr::row_number()) %>%
      group_by(Company_name, BvD_ID_number) %>%
      summarise(orig_order = min(row_id), .groups = "drop") %>%
      select(Company_name, BvD_ID_number, orig_order)
    
    ## ==================================================================
    ## 2. Identify share-year columns and prepare firm base (block-level)
    ## ==================================================================
    share_cols <- names(firms_wide) %>%stringr::str_subset("^SH_Direct_\\d{4}$")
    share_cols <- share_cols[order(readr::parse_number(share_cols))]
    years <- share_cols %>% stringr::str_extract("\\d{4}") %>% as.integer()
    
    firms <- firms_wide %>%
      mutate(
        Company_name  = as.character(Company_name),
        BvD_ID_number = as.character(BvD_ID_number),
        SH_Type       = factor(SH_Type),
        across(all_of(share_cols), ownership_to_numeric)
      )
    
    # firm base for this block, with original order + block id
    firms_base <- firms %>%
      distinct(Company_name, BvD_ID_number) %>%
      left_join(firm_order, by = c("Company_name", "BvD_ID_number")) %>%
      mutate(block = block_id) %>%
      select(block, orig_order, Company_name, BvD_ID_number)
    
    ## ==================================================================
    ## 3. Compute top owners per firm–year (same logic as before)
    ## ==================================================================
    dt <- as.data.table(firms)
    
    owners_top <- melt(
      dt,
      id.vars       = c("Company_name","BvD_ID_number","SH_Name","SH_BvD_ID_number","SH_Country_ISO_code","SH_Type"),
      measure.vars  = share_cols,
      variable.name = "share_col",
      value.name    = "SH_direct_share",
      variable.factor = FALSE
    )[
      , year := as.integer(sub("SH_Direct_", "", share_col))
    ][
      , share_for_rank := fifelse(is.na(SH_direct_share), -Inf, SH_direct_share)
    ][
      , max_share_raw := max(share_for_rank),
      by = .(Company_name, BvD_ID_number, year)
    ][
      , all_na := is.infinite(max_share_raw)
    ][
      , rank_desc := frank(-share_for_rank, ties.method = "first"),
      by = .(Company_name, BvD_ID_number, year)
    ][
      (all_na & rank_desc == 1L) |
        (!all_na & abs(max_share_raw - 50) < 1e-8 & abs(SH_direct_share - 50) < 1e-8) |
        (!all_na & abs(max_share_raw - 50) >= 1e-8 & rank_desc == 1L),
      .(Company_name,BvD_ID_number,year,
        SH_name          = SH_Name,
        SH_BvD_ID_number,
        SH_country       = SH_Country_ISO_code,
        SH_direct_share,
        SH_Type)
    ] |>
      as_tibble()
    
    ## ==================================================================
    ## 4–7. Panel, gap-bridge, LOCF, pre-incorporation (block-level)
    ## ==================================================================
    
    panel_base <- tidyr::crossing(firms_base, year = years)
    
    firms1_block <- panel_base %>%left_join(owners_top, by = c("Company_name", "BvD_ID_number", "year")) %>%
      
      # 5. bridge single-year gaps
      arrange(BvD_ID_number, year) %>%
      group_by(BvD_ID_number) %>%
      mutate(
        bridge_gap =
          # (a) rule: middle year is missing / <1 and both sides are the same owner
          (
            (is.na(SH_direct_share) | SH_direct_share < 1) &
              !is.na(lag(SH_direct_share)) &
              !is.na(lead(SH_direct_share)) &
              lag(SH_direct_share)      == lead(SH_direct_share) &
              lag(SH_name)              == lead(SH_name) &
              lag(SH_BvD_ID_number)     == lead(SH_BvD_ID_number) &
              lag(SH_country)           == lead(SH_country) &
              lag(SH_Type)              == lead(SH_Type)
          ) |
          # (b) rule: middle year <1, but both neighbours are >50
          (
            !is.na(lag(SH_direct_share)) & lag(SH_direct_share)  > 50 &
            !is.na(lead(SH_direct_share)) & lead(SH_direct_share) > 50 &
            !is.na(SH_direct_share) & SH_direct_share < 1
          ),
        SH_name          = if_else(bridge_gap, lag(SH_name),          SH_name),
        SH_BvD_ID_number = if_else(bridge_gap, lag(SH_BvD_ID_number), SH_BvD_ID_number),
        SH_country       = if_else(bridge_gap, lag(SH_country),       SH_country),
        SH_Type          = if_else(bridge_gap, lag(SH_Type),          SH_Type),
        SH_direct_share  = if_else(bridge_gap, lag(SH_direct_share),  SH_direct_share)
      ) %>%
      ungroup() %>%
      select(-bridge_gap) %>%
      
      # 6. LOCF within firm up to last real share
      group_by(BvD_ID_number) %>%
      arrange(year, .by_group = TRUE) %>%
      mutate(
        has_share        = !is.na(SH_direct_share),
        has_future_share = rev(cumany(rev(has_share)))
      ) %>%
      tidyr::fill(
        SH_name, SH_BvD_ID_number, SH_country, SH_Type, SH_direct_share,
        .direction = "down"
      ) %>%
      mutate(
        SH_name          = if_else(has_future_share, SH_name,          NA_character_),
        SH_BvD_ID_number = if_else(has_future_share, SH_BvD_ID_number, NA_character_),
        SH_country       = if_else(has_future_share, SH_country,       NA_character_),
        SH_Type          = if_else(has_future_share, SH_Type,          NA),
        SH_direct_share  = if_else(has_future_share, SH_direct_share,  NA_real_)
      ) %>%
      
      # 7. blank pre-incorporation years
      arrange(year, .by_group = TRUE) %>%
      mutate(
        first_non_na = match(TRUE, has_share),
        before_first = if_else(is.na(first_non_na),
                               TRUE,
                               dplyr::row_number() < first_non_na),
        SH_name          = if_else(before_first, NA_character_, SH_name),
        SH_BvD_ID_number = if_else(before_first, NA_character_, SH_BvD_ID_number),
        SH_country       = if_else(before_first, NA_character_, SH_country),
        SH_Type          = if_else(before_first, NA,             SH_Type),
        SH_direct_share  = if_else(before_first, NA_real_,       SH_direct_share)
      ) %>%
      ungroup() %>%
      select(-has_share, -has_future_share, -first_non_na, -before_first)
    
    block_panels[[i]] <- firms1_block
  } # end block loop
  
  ## ====================================================================
  ## Combine blocks and reassign obs_id preserving original order
  ## ====================================================================
  
  firms_all <- bind_rows(block_panels)
  
  # one row per firm, keeping block + orig_order to preserve Excel order
  firms_base_all <- firms_all %>%
    distinct(block, orig_order, Company_name, BvD_ID_number) %>%
    arrange(block, orig_order) %>%
    mutate(obs_id = dplyr::row_number())
  
  firms_all <- firms_all %>%
    left_join(firms_base_all,by = c("block", "orig_order", "Company_name", "BvD_ID_number")) %>%
    arrange(obs_id, year) %>%
    select(-block, -orig_order)
  
  readr::write_csv(firms_all, outfile)
  message("✔ Finished industry ", ind_code, " — saved: ", outfile)
}

##------------------------------------------------------------------------------
## SELECT INDUSTRIES AND CREATE OWNERSHIP DATA 
##------------------------------------------------------------------------------

# Get all immediate subfolders of base_dir, e.g. "01", "47", ...
#industries <- list.d:qirs(base_dir, recursive = FALSE, full.names = FALSE)
industries <- c("47")
#industries <- c("42")  

purrr::walk(industries, process_industry)
message("\n========== ALL INDUSTRIES COMPLETED ==========\n")
