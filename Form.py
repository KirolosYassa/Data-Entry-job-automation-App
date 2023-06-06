import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Form():
    def __init__(self):
        self.chrome_local_path = "C:\Development"
        self.driver = webdriver.Chrome(executable_path=self.chrome_local_path)
        self.form_url="https://docs.google.com/forms/d/e/1FAIpQLSd1fRcBESrTAgVZkYPPhijk-UuagLz_MOnNwVq6FvXOq2EyAg/viewform?usp=sf_link"
        self.driver.get(self.form_url)

        time.sleep(2)
        

    def input_form_data(self, addresses=[], prices=[], links=[]):
        
        for i in range(len(addresses)):
            questions_answers = self.driver.find_elements(By.CSS_SELECTOR, "input.whsOnd")
            
            questions_answers[0].send_keys(addresses[i])
            questions_answers[1].send_keys(prices[i])
            questions_answers[2].send_keys(links[i])

            submit = self.driver.find_element(By.CSS_SELECTOR, "span.NPEfkd")
            submit.click()
            time.sleep(1)
            
            answer_another_response = self.driver.find_element(By.CSS_SELECTOR, "div.c2gzEf > a")
            answer_another_response.click()
            time.sleep(1)
