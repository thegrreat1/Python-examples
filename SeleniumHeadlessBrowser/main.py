import sys

try:
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
except ImportError:
    print("Error: Module selenium is not installed. Install it with pip install selenium")
    sys.exit(1)

url = "https://wttr.in"
options = Options()
options.add_argument("-headless")

try:
    with webdriver.Firefox(options=options) as browser:
        # opening the target website in the browser
        browser.get(url)
        print(browser.page_source)
except:
    print("Error: Could not connect to the website")
    sys.exit(1)
