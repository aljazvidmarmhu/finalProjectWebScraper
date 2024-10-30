from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Create a Service object for the geckodriver
service = Service(executable_path=os.path.expanduser('~/Documents/Mars\ Hill\ University/finalProject/geckodriver2'))

# Create Firefox options if needed (optional)
options = Options()

# Create a new instance of the Firefox driver
driver = webdriver.Firefox(service=service, options=options)

# Go to a website
driver.get("https://flyer.inglesads.com/noncard/ThisWeek/index.jsp?ID3508")


# Close the browser
driver.quit()
