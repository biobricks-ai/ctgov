from bs4 import BeautifulSoup
import httpx
import pandas as pd

timeout = httpx.Timeout(10.0, read=60.0)
client = httpx.Client(timeout=timeout)

def get_aact_html():
    url = "https://aact.ctti-clinicaltrials.org/data_dictionary"
    resp = client.get(url)
    soup = BeautifulSoup(resp.text)
    soup.find_all("table")