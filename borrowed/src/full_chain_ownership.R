## ======================================================================
## OBTAINING FULL NETWORK (CHAIN) of OWNERSHIP
## ======================================================================

rm(list = ls())  # clear environment

# install packages
user_lib <- "C:/Users/aitor_f/Documents/R/win-library/4.4"
dir.create(user_lib, recursive = TRUE, showWarnings = FALSE)
.libPaths(user_lib)
.libPaths()

install.packages(c("dplyr", "readr","data.table","haven"))

# Load packages
library(dplyr)
library(readr)
library(data.table)
library(haven)

# Folder where ownership_indXX.csv live
data_dir <- "C:/Users/aitor_f/Dropbox/supergrassi/data/uk_data_financial_accounts/OwnershipFAME"

# Temp folder for intermediate per-year raw files
tmp_dir  <- file.path(data_dir, "tmp_year_raw")

# Final output folder: one cleaned file per year
out_dir  <- file.path(data_dir, "cleaned_by_year")

dir.create(tmp_dir, showWarnings = FALSE)
dir.create(out_dir, showWarnings = FALSE)

# define industries and year 
#industries <- c(01,02,03,05,06,07,08,09,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,37,38,39,41,42,43,45,46,47,49,50,51,52,53,55,56,58,59,60,61,62,63,64,65,66,68,69,70,71,72,73,74,75,77,78,79,80,81,82,84,85,86,87,88,90,91,92,93,94,95,96,97,98,99)
industries <- c(10, 20, 28, 30, 64, 70, 86)  

#################################################
# 1) stream each industry into per-year raw files 
#################################################
process_industry_file <- function(industry, data_dir, tmp_dir) {
  
  file_path <- file.path(data_dir, sprintf("ownership_ind%02d.csv", industry))
  
  if (!file.exists(file_path)) {
    warning("File not found for industry ", industry, ": ", file_path)
    return(invisible(NULL))
  }
  
  message("Reading industry ", industry, " from ", file_path)
  
  # Read only needed columns (saves memory & disk I/O)
  dt <- fread(file_path,select = c("Company_name", "BvD_ID_number", "year","SH_name", "SH_BvD_ID_number", "SH_country","SH_direct_share", "SH_Type", "obs_id"))
  if (nrow(dt) == 0L) return(invisible(NULL))
  
  # Ensure company ID is character for startsWith()
  dt[, BvD_ID_number := as.character(BvD_ID_number)]
  
  # Drop Irish companies: BvD_ID_number starts with "IE"
  dt <- dt[!startsWith(BvD_ID_number, "IE")]
  if (nrow(dt) == 0L) return(invisible(NULL))
  
  # Drop rows where key shareholder variables are missing
  dt <- dt[!is.na(SH_name) & !is.na(SH_BvD_ID_number) & !is.na(SH_country) & !is.na(SH_Type) & !is.na(SH_direct_share)]
  if (nrow(dt) == 0L) return(invisible(NULL))
  
  # Split by year and append to year-specific raw files
  yrs <- unique(dt$year)
  
  for (yy in yrs) {
    dt_y <- dt[year == yy]
    if (nrow(dt_y) == 0L) next
    tmp_file <- file.path(tmp_dir, sprintf("year_%d_raw.csv", yy))
    fwrite(dt_y,tmp_file,append    = file.exists(tmp_file),col.names = !file.exists(tmp_file))
  }
  
  invisible(NULL)
}

# Run first pass: each file read once, streamed into yearly raw files
for (ind in industries) {
  process_industry_file(ind, data_dir = data_dir, tmp_dir = tmp_dir)
}


#################################################
# 2) dedupe per year, then delete raw file 
#################################################

dedupe_one_year <- function(year_to_keep, tmp_dir, out_dir) {
  
  tmp_file <- file.path(tmp_dir, sprintf("year_%d_raw.csv", year_to_keep))
  if (!file.exists(tmp_file)) {
    warning("No raw file for year ", year_to_keep) 
    return(invisible(NULL))
  }
  
  message("Deduplicating year ", year_to_keep)
  
  dt <- fread(tmp_file)
  if (nrow(dt) == 0L) {
    file.remove(tmp_file) 
    return(invisible(NULL))
  }
  
  # Count missing values in key SH fields for tie-breaking
  miss_cols <- c("SH_name", "SH_BvD_ID_number", "SH_country","SH_Type", "SH_direct_share")
  miss_cols <- intersect(miss_cols, names(dt))
  
  if (length(miss_cols) == 0L) {
    dt[, n_miss := 0L]
  } else {
    dt[, n_miss := rowSums(is.na(as.matrix(.SD))), .SDcols = miss_cols]
  }

  # Order so best rows (fewest NAs) come first
  setorder(dt,Company_name,BvD_ID_number,year,SH_name,SH_BvD_ID_number,n_miss)
  
  # keep one row per company–year–shareholder
  dt_unique <- dt[, .SD[1L], by = .(Company_name,BvD_ID_number,year,SH_name,SH_BvD_ID_number)]
  dt_unique[, n_miss := NULL]
  
  # flag "weird" cases: >2 shareholders and ALL have >=50%
  dt_unique[, `:=`(n_sh_total  = .N,n_sh_50plus = sum(SH_direct_share >= 50, na.rm = TRUE)), by = .(Company_name, BvD_ID_number, year)]
  dt_unique[, flag_many_50plus := as.integer(n_sh_total > 2 & n_sh_50plus == n_sh_total)]
  dt_unique[, c("n_sh_total", "n_sh_50plus") := NULL]
  
  # Write final cleaned file for this year
  out_file <- file.path(out_dir, sprintf("ownership_clean_%d.csv", year_to_keep))
  fwrite(dt_unique, out_file)
  
  # Delete raw temp file to free disk space
  file.remove(tmp_file)
  
  invisible(NULL)
}


# Figure out which years we actually have
tmp_year_files <- list.files(tmp_dir, pattern = "^year_\\d+_raw\\.csv$", full.names = TRUE)
years_available <- sort(as.integer(gsub(".*year_(\\d+)_raw\\.csv$", "\\1", tmp_year_files)))

for (yy in years_available) {
  dedupe_one_year(yy, tmp_dir = tmp_dir, out_dir = out_dir)
}


#########################################
# Put all years together
#########################################
year_files <- list.files(out_dir,pattern = "^ownership_clean_\\d+\\.csv$",full.names = TRUE)

# Read and combine
dt_list <- lapply(year_files, fread)
ownership_panel <- rbindlist(dt_list, use.names = TRUE, fill = TRUE)
setorder(ownership_panel, Company_name, BvD_ID_number, year, SH_direct_share)

# Basic checks
ownership_panel[, .N]                   # total number of rows
range(ownership_panel$year)             # should be 2006–2023
uniqueN(ownership_panel$BvD_ID_number)  # number of companies


###########################################
## Flag companies with a parent in the UK
###########################################

# Types that correspond to "owner is a firm"
firm_types <- c("Corporate", "Bank", "Financial company", "Insurance company")

# 1) Row-level flag: shareholder is UK firm with >= 50%
ownership_panel[, is_subsidiary_of_uk_firm := SH_direct_share >= 50 & SH_country == "GB" & SH_Type %chin% firm_types]

# 2) Firm–year dummy: at least one such shareholder
ownership_panel[, subsidiary_of_uk_firm := as.integer(any(is_subsidiary_of_uk_firm, na.rm = TRUE)), by = .(BvD_ID_number, Company_name, year)]

# 3) (Optional) drop helper column
ownership_panel[, is_subsidiary_of_uk_firm := NULL]


# firm-level dummy: ever a UK-firm subsidiary in any year
ownership_panel[, has_parent_in_UK := as.integer(any(subsidiary_of_uk_firm == 1, na.rm = TRUE)), by = .(BvD_ID_number, Company_name)]


################################
## Create two data frames 
################################

# df1: firms that NEVER have a parent in the UK
df1 <- ownership_panel[has_parent_in_UK == 0]

# df2: firms that have a UK parent in at least one year
df2 <- ownership_panel[has_parent_in_UK == 1]


######################################
## 1. Build child–parent firm edges 
######################################

# All firm → parent links (only firm shareholders with ≥50% share)
edges <- df2[SH_direct_share >= 50 & SH_Type %chin% firm_types,
  .(
    child_id     = BvD_ID_number,
    child_name   = Company_name,
    year,
    parent_id    = SH_BvD_ID_number,
    parent_name  = SH_name,
    parent_share = SH_direct_share
  )
]

# For each child–year, keep the parent with the largest share
edges_main <- edges[order(child_id, year, -parent_share)]
edges_main <- edges_main[, .SD[1L], by = .(child_id, year)]
edges_main[, parent_share := NULL]   # optional: drop now

###############################################################
## 2. Build parent chains up to max_depth (for now, set to 30)
###############################################################

max_depth <- 30

# Start from all firm–year combos in df2, keeping child id + name
chain <- unique(df2[, .(child_id   = BvD_ID_number,child_name = Company_name,year)])

# Level 1: direct parent (id + name)
chain <- merge(chain,edges_main[, 
  .(
    child_id,
    year,
    parent_level1_id   = parent_id,
    parent_level1_name = parent_name
  )],
  by = c("child_id", "year"),
  all.x = TRUE
)

# Levels 2–max_depth: parent’s parent, etc.
for (lvl in 2:max_depth) {
  prev_id_col   <- paste0("parent_level", lvl - 1, "_id")
  new_id_col    <- paste0("parent_level", lvl, "_id")
  new_name_col  <- paste0("parent_level", lvl, "_name")
  
  chain <- merge(chain,edges_main[, 
    .(
      child_id,
      year,
      parent_id,
      parent_name
    )],
    by.x = c(prev_id_col, "year"),   # previous parent becomes the new "child"
    by.y = c("child_id", "year"),
    all.x = TRUE
  )
  
  data.table::setnames(chain,old = c("parent_id", "parent_name"),new = c(new_id_col, new_name_col))
}

###################################################
## 3. Truncate at first repetition & flag cycles
###################################################

parent_id_cols   <- paste0("parent_level", 1:max_depth, "_id")
parent_name_cols <- paste0("parent_level", 1:max_depth, "_name")

# Work with matrices for speed
id_mat   <- as.matrix(chain[, ..parent_id_cols])
name_mat <- as.matrix(chain[, ..parent_name_cols])

# For each row, position of first duplicate id (0 = no cycle)
first_dup_pos <- apply(id_mat, 1L, function(x) {
  dup <- duplicated(x) & !is.na(x)
  if (any(dup)) which(dup)[1L] else 0L
})

has_cycle_vec <- as.integer(first_dup_pos > 0L)

# Truncate only rows with cycles: set ids/names from first duplicate onwards to NA
idx_cycle <- which(first_dup_pos > 0L)

if (length(idx_cycle) > 0L) {
  for (i in idx_cycle) {
    j <- first_dup_pos[i]
    id_mat[i,   j:max_depth] <- NA
    name_mat[i, j:max_depth] <- NA
  }
}

# After truncation, recompute number of parents
n_parents_vec <- rowSums(!is.na(id_mat))

# Assign back to `chain`
chain[, (parent_id_cols)   := as.data.table(id_mat)]
chain[, (parent_name_cols) := as.data.table(name_mat)]
chain[, `:=`(n_parents = as.integer(n_parents_vec),has_cycle = has_cycle_vec)]

######################################
## 4. Build firm–year chain dataset
######################################
ordered_parent_cols <- as.vector(rbind(parent_id_cols,parent_name_cols))
keep_cols <- c("child_id", "child_name", "year", "n_parents", "has_cycle", ordered_parent_cols)
firm_year_chain <- chain[, ..keep_cols]
data.table::setnames(firm_year_chain,old = c("child_id", "child_name"),new = c("BvD_ID_number", "Company_name"))
setorder(firm_year_chain, BvD_ID_number, Company_name, year)



######################################
## save firm-year chain data 
######################################
out_path <- file.path(data_dir,"firm_year_chain.dta")
write_dta(firm_year_chain, out_path)

