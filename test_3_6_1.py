import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

LOC_TEXT_FIELD = (By.TAG_NAME, "textarea") 
LOC_SUBMIT = (By.CLASS_NAME, "submit-submission")
LOC_ANSWER = (By.CLASS_NAME, "smart-hints__hint")

@pytest.fixture(scope = "function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("link", ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_response(browser, link):
    browser.get(f"https://stepik.org/lesson/236{link}/step/1")
    field = WebDriverWait(browser, 10).until(EC.presence_of_element_located(LOC_TEXT_FIELD))
    inp = math.log(int(time.time()-1.5))
    field.send_keys(str(inp))
    browser.find_element(*LOC_SUBMIT).click()
    text_elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(LOC_ANSWER))
    assert text_elem.text == "Correct!"

