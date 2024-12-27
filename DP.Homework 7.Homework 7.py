from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from bs4 import BeautifulSoup
import requests

driver = webdriver.Chrome()
driver.get("https://psyjournals.ru/")

cookie_box = driver.find_element(By.ID,"cookie-policy-accept-button")
cookie_box.click()

time.sleep(15)

search_box = driver.find_element(By.XPATH, "//*[.='Консультативная психология и психотерапия']")
search_box.click()

authors = []
titles = []
pages = []

output = {'Authors':authors,'Title':titles,'Pages':pages}
import urllib.parse
import re
website = driver.find_element(By.XPATH, "//html/head/link[1]").get_attribute('href')     
page = requests.get(website)
soup = BeautifulSoup(page.content, 'html.parser')
result = soup.find_all('li', ('class', 'publicationissues-list-item'))
url2=[]
for i in result:
        url2.append(i.find('a').get('href'))
    
url_joined = []
for link in url2:
        url_joined.append(urllib.parse.urljoin(website,link))
for el in url_joined:
        response = requests.get(el)
        soup = BeautifulSoup(response.content, 'html.parser')
    # Авторы
        try:
            authors.append(soup.find('div',('class','publications-list-item-head')).text.rstrip())
        except:
            authors.append('')
    # Названия
        try:
            titles.append(soup.find('h5').text)
        except:
            titles.append('')
    # страницы
        try:
            pages.append(soup.find('div',('class','publications-list-item-body-pages')).text)
        except:
            pages.append('')
    
   
  
print(output)
import json
psyjournals = json.dumps(output)
with open('psyjournals.json', 'w', encoding='utf-8') as file:
    json.dump(psyjournals, file, ensure_ascii=False, indent=4)
driver.quit()







