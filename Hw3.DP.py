# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 21:35:24 2024

@author: Анастасия Рахманина
"""

import pymongo
import json 
from pymongo import MongoClient
client = MongoClient ('mongodb://localhost:27017')


#Открываем файл 
with open ('json_obj.json','r') as json_file:
    data=json.load(json_file)
  # print (data)
  
db = client.books_to_scrape

def find():
   # query = {'Availabilitys':17}
   # query = {'prices':{'$lte':100.0}} 
   # query = {'descriptions':{'regex':'[Llove'}} 
     query = {'availabilitys':{'$gt':15}} 
   # query = {'$or': [{'prices':{'$lt':100}},{'descriptions:{'regex':'[Adventure]'}}]}
   
     projection = {'names':1,'prices':0,'availabilitys':0, 'descriptions':0}
    
     books = db.books.find (query,projection)
     for a in books:
        print(a)
if __name__ == 'main':
    find()
    


