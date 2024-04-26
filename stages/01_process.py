from bs4 import BeautifulSoup, PageElement
import json
import logging
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from typing import Tuple

logger = logging.getLogger(__name__)
logging.basicConfig(format="%(asctime)s %(message)s")
logger.setLevel("DEBUG")

URL = "https://aact.ctti-clinicaltrials.org/data_dictionary"
TABLE_NAMES = [
    "countries",
    "reported_event_totals",
    "facility_contacts",
    "overall_officials",
    "design_groups",
    "ipd_information_types",
    "detailed_descriptions",
    "studies",
    "facility_investigators",
    "documents",
    "calculated_values",
    "conditions",
    "reported_events",
    "designs",
    "browse_interventions",
    "facilities",
    "provided_documents",
    "links",
    "sponsors",
    "participant_flows",
    "design_group_interventions",
    "keywords",
    "study_references",
    "design_outcomes",
    "brief_summaries",
    "outcome_analyses",
    "central_contacts",
    "drop_withdrawals",
    "result_groups",
    "id_information",
    "baseline_counts",
    "result_contacts",
    "browse_conditions",
    "baseline_measurements",
    "search_results",
    "outcome_counts",
    "eligibilities",
    "interventions",
    "outcome_measurements",
    "retractions",
    "responsible_parties",
    "milestones",
    "outcome_analysis_groups",
    "outcomes",
    "result_agreements",
    "intervention_other_names",
    "pending_results",
]


class DataDicts:
    _webdriver: WebDriver

    def __init__(self, url):
        session = webdriver.Chrome()
        session.get(url)
        session.implicitly_wait(5)
        self._webdriver = session

    def find_data_table(self) -> Tuple[WebElement]:
        table = self._webdriver.find_element(By.CSS_SELECTOR, ".jsgrid-grid-body > .jsgrid-table")
        flt = self._webdriver.find_element(By.CLASS_NAME, "jsgrid-filter-row")
        return (table, flt)

    def get_input(self, filter_row: WebElement):
        search_bar = filter_row.find_element(By.CSS_SELECTOR, ":nth-child(4)")
        input = search_bar.find_element(By.CSS_SELECTOR, ":nth-child(1)")
        return input

    def run_search(self, input: WebElement, search_term):
        input.send_keys(search_term)
        input.send_keys(Keys.RETURN)
        time.sleep(3)

    def get_each_table(self, table_el: WebElement, input: WebElement, name: str):
        input.clear()
        self.run_search(input, name)
        # need to grab reference to jsgrid-table element
        outer_html = table_el.get_attribute("outerHTML")
        soup = BeautifulSoup(outer_html)
        return soup

    def get_el_text(self, el: PageElement):
        return el.get_text()

    def make_col_dicts(self, soup: BeautifulSoup):
        col_names = soup.select("tr > td:nth-of-type(5)")
        col_types = soup.select("tr > td:nth-of-type(6)")
        return dict(
            zip(map(self.get_el_text, col_names), map(self.get_el_text, col_types))
        )

    def __call__(self):
        table, flt = self.find_data_table()
        input = self.get_input(flt)
        output = {}
        for table_name in TABLE_NAMES:
            soup = self.get_each_table(table, input, table_name)
            logger.info(soup)
            data_dicts = self.make_col_dicts(soup)
            assert data_dicts != {'': ''}
            output[table_name] = data_dicts
            if table_name != "countries":
                assert list(data_dicts.keys()) != ["id", "name", "nct_id", "removed"]
            time.sleep(2)
        return output


if __name__ == "__main__":
    output = DataDicts(URL)
    data = output()
    
    with open("test.json", "w") as f:
        f.write(json.dumps(data, indent=4))