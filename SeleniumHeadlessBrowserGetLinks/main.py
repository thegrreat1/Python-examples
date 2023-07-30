import sys
import time

try:
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.common.by import By
except ImportError:
    print("Error: Module selenium is not installed. Install it with pip install selenium")
    sys.exit(1)

url = "https://edition.cnn.com/"
options = Options()
options.add_argument("-headless")


with webdriver.Firefox(options=options) as browser:
    browser.get(url)
    page_source = browser.find_elements(By.XPATH, "//a[@href]")
    for link in page_source:
        print(link.get_attribute("href"))
    browser.close()

