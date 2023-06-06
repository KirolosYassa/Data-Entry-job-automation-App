from bs4 import BeautifulSoup
import time
from selenium import webdriver

class Zillow():
    def __init__(self):
        self.chrome_local_path = "C:\Development"
        self.driver = webdriver.Chrome(executable_path=self.chrome_local_path)
        self.Zillow_url="https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
        self.driver.get(self.Zillow_url)

        time.sleep(2)

        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        self.prices_list = []
        self.addresses_list = []
        self.links_list = []


    def get_zillow_data(self):
                
        prices = self.soup.find_all('span', class_=['srp__sc-16e8gqd-1', 'jLQjry'])

        for price in prices:
            price_text = price.text
            self.prices_list.append(price_text)
            

        addresses = self.soup.find_all('address')

        for address in addresses:
            self.addresses_list.append(address.get_text())
            

        links = self.soup.find_all('a', class_=['StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0'])

        for link in links:
            link_text = link.get('href')
            if "https:" not in link_text:
                link_text = f"https://www.zillow.com{link.get('href')}"

            self.links_list.append(link_text)
            
        print(f"prices_list is about {len(self.prices_list)} prices")
        print(self.prices_list)
        print(f"addresses_list is about {len(self.addresses_list)} addresses")
        print(self.addresses_list)
        print(f"links_list is about {len(self.links_list)} links")
        print(self.links_list)
        
    def quit(self):
        self.driver.quit()
