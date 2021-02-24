#imports
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#get list of available languages
list_lang = []
with open("list_lang.txt", "r") as f:
    for lang in f:
        list_lang.append(lang.replace("\n", ""))

#initialize parameter
def pytest_addoption(parser):
    parser.addoption("--language", action = "store", 
                    default = "eng", help = "Enter language:")

#set browser configurations
@pytest.fixture(scope = "function")
def browser(request):
    lang = request.config.getoption("language")
    if lang in list_lang:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lang})
        driver = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language option is not available")
    yield driver
    driver.quit()