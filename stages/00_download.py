import requests
from bs4 import BeautifulSoup
import os
import re

# Set timeout for the requests
requests.options.timeout = 1800  # download timeout

# read html from page and grab file to download
response = requests.get("https://aact.ctti-clinicaltrials.org/pipe_files")
page = response.content

# Parse HTML and find all links
soup = BeautifulSoup(page, 'html.parser')
links = soup.find_all('a')

# Detect the recent zip file link
recent = None
for link in links:
    if re.search(r'\.zip$', link.text.strip(), re.IGNORECASE):
        recent = link
        break

if recent:
    # Get file name and create download directory
    name = recent.get_text().strip()
    if not os.path.exists('download'):
        os.makedirs('download')
    download_path = os.path.join('download', name)
    
    # Get the full URL for download
    url = recent['href']
    print(f"Downloading {url} to {download_path}")
    
    # Download the file
    response = requests.get(url)
    with open(download_path, 'wb') as file:
        file.write(response.content)
else:
    print("No zip file found.")