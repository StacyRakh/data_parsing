#!/usr/bin/env python
# coding: utf-8




from bs4 import BeautifulSoup
import requests
import pandas as pd

names = []
availabilitys = []
prices = []
descriptions = []
output = {'Name':names,'Price':prices,'Availability':availabilitys,'Description':descriptions}


# ## Скрейпинг всего сайта



import urllib.parse
import re

for i in range(1,51):
    website = f'https://books.toscrape.com/catalogue/page-{i}.html'     
    page = requests.get(website)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find_all('article', ('class', 'product_pod'))
    url2=[]
    for i in result:
        for link in i.find_all('div', ('class', 'image_container')):
            url2.append(link.find('a').get('href'))
    
    url_joined = []
    for link in url2:
        url_joined.append(urllib.parse.urljoin(website,link))
    for i in url_joined:
        response = requests.get(i)
        soup = BeautifulSoup(response.content, 'html.parser')
    #Названия
        try:
            names.append(soup.find('h1').text)
        except:
            names.append('')
            #Цены
        p=soup.find('p',('class','price_color')).text
        p = float(p[1:])
        prices.append (p)
    
    #Количество
        a = soup.find('p',('class','instock availability')).text
        a = re.findall(r'[-+]?\d+', a)
        for i in a:
            a = int(i)
        availabilitys.append(a)
  
    #Описание
        try:
            d = soup.find_all('p')
            d = d[3].text
            descriptions.append(d)
        except:
            descriptions.append('')

   
import json
json_obj = json.dumps(output)
print(json_obj)



# In[ ]:




