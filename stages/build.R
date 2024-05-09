library(arrow)
library(dplyr)
library(fs)
library(purrr)
library(readr)
library(vroom)

# creates temp directory and data directory
tmp  <- fs::dir_create("tmp")
data <- fs::dir_create("brick")

# Get spec from metadata
datadef <- read.csv('metadata/definitions.csv') |>
  select(!c('CTTI.note', 'nlm.doc', 'enumerations')) |>
  subset( db.schema == 'ctgov' )

datadef_cols_single_type <- datadef |>
  group_by(column) |> distinct(data.type) |> count() |>
  subset( n == 1, select=column )

# Column names that are only integers.
datadef_integer <- (
	datadef |>
          subset( column %in% datadef_cols_single_type$column
                 & data.type == 'integer' )
        )[,'column'] |> unique()

col_spec <- cols(
  !!!map(set_names(datadef_integer), ~ col_integer())
)

# unzips zipfile
fs::dir_ls("download") |> tail(1) |> unzip(exdir = tmp)

fs::dir_ls(tmp) |> walk(function(f) {
  # files are txt files with | separation

  df <- vroom(f, delim = "|", col_names = TRUE,
              col_types = col_spec,
              locale = locale(encoding = "UTF-8"))

  # writes parquet file
  arrow::write_parquet(df, fs::path_ext_set(data/fs::path_file(f),"parquet"))
})

# delete temp directory
fs::dir_delete(tmp)
