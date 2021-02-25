#imports
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#locators and links
LOC_ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '[class*="btn-add-to-basket"]')
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

#test
def test_existance_of_basket_button(browser):
    browser.get(link)
    #to check workability of language changing
    #by default this line of code is commented so you can check button search first
    #time.sleep(30)
    #get list of buttons with the locator
    basket_button = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located(LOC_ADD_TO_BASKET_BUTTON))
    #checks whether there is a basket button on a page 
    assert basket_button is not None