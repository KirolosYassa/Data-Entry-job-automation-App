from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up a headless Chrome browser
chrome_local_path = "C:\Development"
driver = webdriver.Chrome(executable_path=chrome_local_path)
# driver.get(url)

# Navigate to the Zillow homepage
Zillow_url="https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
driver.get(Zillow_url)

# Wait for the page to load
time.sleep(5) # adjust the sleep time as needed

# Pass the page source to Beautiful Soup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find elements using Beautiful Soup
# Example:
listings = soup.find_all('article', {'class': 'list-card'})

# Close the browser
driver.quit()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


# response = requests.get(url = Zillow_url, headers=headers)
# zillow_content = response.content

# time.sleep(2.5)

# soup = BeautifulSoup(zillow_content, 'html.parser')

# print(soup)

prices = soup.find_all('span', class_=['srp__sc-16e8gqd-1', 'jLQjry'])
prices_list = []

for price in prices:
    price_text = price.text
    prices_list.append(price_text)
    

addresses = soup.find_all('address')
addresses_list = []

for address in addresses:
    addresses_list.append(address.get_text())
    

links = soup.find_all('a', class_=['StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0','gdfTyO','property-card-link'])
links_list = []

for link in links:
    links_list.append(link.get('href'))
    
print(f"prices_list is about {len(prices_list)} prices")
print(prices_list)
print(f"addresses_list is about {len(addresses_list)} prices")
print(addresses_list)
print(f"links_list is about {len(links_list)} prices")
print(links_list)


form_url = "https://forms.gle/TLLBT651cR6ZrQjy6"
