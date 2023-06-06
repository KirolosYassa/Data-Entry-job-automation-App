from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Zillow import Zillow

# Set up a headless Chrome browser
# chrome_local_path = "C:\Development"
# driver = webdriver.Chrome(executable_path=chrome_local_path)
# # driver.get(url)


zillow = Zillow()
zillow.get_zillow_data()


form_url = "https://forms.gle/TLLBT651cR6ZrQjy6"
# driver.quit()
