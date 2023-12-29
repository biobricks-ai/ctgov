library(purrr)
library(arrow)
library(fs)

# creates temp directory and data directory
tmp  <- fs::dir_create("tmp")
data <- fs::dir_create("brick")

# unzips zipfile
fs::dir_ls("download") |> tail(1) |> unzip(exdir = tmp)

fs::dir_ls(tmp) |> walk(function(f) {
  # files are txt files with | separation
  df <- read.table(f, sep = "|", fill = TRUE, header = TRUE)
  # writes parquet file
  arrow::write_parquet(df, fs::path_ext_set(data/fs::path_file(f),"parquet"))
})

# delete temp directory
fs::dir_delete(tmp)


