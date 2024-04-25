from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple


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
    "pending_results"
]


def setup_webdriver(url):
    browser = webdriver.Firefox()
    browser.get(url)
    return browser


def find_data_table(webdriver: WebDriver) -> Tuple[WebElement]:
    table = webdriver.find_element(By.CLASS_NAME, "jsgrid-table")
    flt = table.find_element(By.CLASS_NAME, "jsgrid-filter-row")
    return (table, flt)


def get_input(filter_row: WebElement):
    search_bar = filter_row.find_element(By.CSS_SELECTOR, ":nth-child(4)")
    input = search_bar.find_element(By.CSS_SELECTOR, ":nth-child(1)")
    return input


def run_search(input: WebElement, search_term):
    _ = input.location_once_scrolled_into_view  # scrolls the table into view
    input.send_keys(search_term)
    input.send_keys(Keys.RETURN)


def get_each_table(input: WebElement, name):
    input.clear()
    run_search(input, name)
    # need to grab reference to jsgrid-table element
    table_ref = globals()['browser']
    outer_html = table_ref.find_element(By.CLASS_NAME, "jsgrid-grid-body").get_attribute("outerHTML")
    soup = BeautifulSoup(outer_html)
    return soup
    

def run_script():
    browser = setup_webdriver(URL)
    table, flt = find_data_table(browser)
    input = get_input(flt)
    soup = get_each_table(input, TABLE_NAMES[0])
    # need to get the actual data and not just the innerHTML
    return soup
