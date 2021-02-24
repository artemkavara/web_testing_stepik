from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest

LOC_FIRST_NAME = (By.XPATH, '//div[@class = "first_block"]//input[@class = "form-control first"]')
LOC_LAST_NAME = (By.XPATH, '//div[@class = "first_block"]//input[@class = "form-control second"]')
LOC_EMAIL = (By.XPATH, '//div[@class = "first_block"]//input[@class = "form-control third"]')

LOC_PHONE = (By.XPATH, '//div[@class = "second_block"]//input[@class = "form-control first"]')
LOC_ADDRESS = (By.XPATH, '//div[@class = "second_block"]//input[@class = "form-control second"]')

LOC_SUBMIT = (By.XPATH, "//button[text()='Submit']")
LOC_WELCOME_TEXT = (By.TAG_NAME, "h1")
 
def form(link):
    driver = webdriver.Chrome()
    driver.get(link)
    driver.find_element(*LOC_FIRST_NAME).send_keys("1")
    driver.find_element(*LOC_LAST_NAME).send_keys("1")
    driver.find_element(*LOC_EMAIL).send_keys("1")
    driver.find_element(*LOC_PHONE).send_keys("1")
    driver.find_element(*LOC_ADDRESS).send_keys("1")
    driver.find_element(*LOC_SUBMIT).click()
    text = driver.find_element(*LOC_WELCOME_TEXT).text
    driver.quit()
    return text    

class TestForm(unittest.TestCase):

    def test_first_form(self):
        link = "https://suninjuly.github.io/registration1.html"
        self.assertRegex(text = form(link), expected_regex = r"\w* You\w*", msg = "Element not detected!")

    def test_second_form(self):
        link = "https://suninjuly.github.io/registration2.html"
        self.assertRegex(text = form(link), expected_regex = r"\w* You\w*", msg = "Element not detected!")

if __name__ == "__main__":
    unittest.main()