# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:45:45 2024

@author: Анастасия Рахманина
"""
from pymongo.server_api import ServerApi
import pymongo
from pymongo import MongoClient
uri = "mongodb+srv://StacyRakh:<nASTUHASUPER96!>@cluster0.0pffu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    