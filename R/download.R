library(rvest)
library(purrr)
library(fs)

options(timeout=1800) # download timeout

# read html from page and grab file to download
page   <- read_html("https://aact.ctti-clinicaltrials.org/pipe_files")
href   <- page |> html_nodes("a") |> html_attr("href") 
recent <- detect(href, ~ grepl("*.zip",.))

# download file to download directory
download <- fs::dir_create("download") |> fs::path(fs::path_file(recent))
url      <- paste0("https://aact.ctti-clinicaltrials.org",recent)
download.file(url,download)
