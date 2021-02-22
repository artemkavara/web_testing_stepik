from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

LOC_FIRST_NAME = (By.XPATH, '//div[@class = "first_block"]//input[@class = "form-control first"]')
LOC_LAST_NAME = (By.XPATH, '//div[@class = "first_block"]//input[@class = "form-control second"]')
LOC_EMAIL = (By.XPATH, '//div[@class = "first_block"]//input[@class = "form-control third"]')

LOC_PHONE = (By.XPATH, '//div[@class = "second_block"]//input[@class = "form-control first"]')
LOC_ADDRESS = (By.XPATH, '//div[@class = "second_block"]//input[@class = "form-control second"]')

LOC_SUBMIT = (By.XPATH, "//button[text()='Submit']")

link = "https://suninjuly.github.io/registration1.html"

driver = webdriver.Chrome()
driver.get(link)

try:
    driver.find_element(*LOC_FIRST_NAME).send_keys("1")
    driver.find_element(*LOC_LAST_NAME).send_keys("1")
    driver.find_element(*LOC_EMAIL).send_keys("1")
    driver.find_element(*LOC_PHONE).send_keys("1")
    driver.find_element(*LOC_ADDRESS).send_keys("1")
    driver.find_element(*LOC_SUBMIT).click()
except NoSuchElementException as e:
    print(e)
finally:
    driver.quit()