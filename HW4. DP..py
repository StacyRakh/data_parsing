# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 13:34:40 2024

@author: Анастасия Рахманина
"""
# Импортируем все необходимые модули
from lxml import html
import requests
import re 
import csv

# Используем данные сайта различных рейтингов сайтов.
# Изначально я хотела взять рейтинг вузов, но сайт оказался капризным
# и выводил меня на 1 страницу при обычном скролинге
# из-за этого данные подгружались из разных рейтингов, поэтому взяла основной




#Для обработки возьмем номер в рейтинге, название агентства, рейтинг, стаж
rating_nums=[]
names = []
rating_score=[]
exp=[]



n=1
while n <= 7:    
   if n==1:
       url = 'https://wwwrating.com'
   else:
       url = f'https://wwwrating.com/?PAGEN_2={n}'
   response = requests.get (url = url,
                             headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'})
   tree = html.fromstring(html=response.content)
   unis = tree.xpath ('//table/tbody/tr')
   for uni in unis:
           try:
               rating_nums.append (int(uni.xpath('.//td[@class="mob-ib nmb"]/span/text()')[0]))
           except:
               rating_nums.append(" ")
           try:
               names.append(uni.xpath('.//td[@data-attr="Компания"]/a/text()')[0])
           except:
               names.append(" ")
           try:
               rating_score.append(float(uni.xpath('.//td[@data-attr="Рейтинг"]/text()')[0]))
           except:
               rating_score.append(" ")
           try:
               exp.append(int((re.findall(r'\d{1,2}',(uni.xpath('.//td[@data-attr="Домен"]/div/div/div/text()')[0])))[0]))
           except:
               exp.append(" ")
   n=n+1

# Я обработала до 7 страницы, хотя изначально планировала обработать все 505
# но после 7 страницы он у меня начинал обрабатывать 470 раз 1 страницу
# и только в конце 505. На сайте он также вылетает после 7 страницы на 1.

zipped_values = zip(rating_nums,names,rating_score,exp)
with open('agents.csv', 'w', newline='') as csvfile:
    fieldnames = ['rating_nums', 'names', 'rating_score', 'exp']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    writer.writerows(zipped_values)
with open('agents.csv') as f:
    print(f.read())

