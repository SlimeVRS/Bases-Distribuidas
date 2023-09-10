from pymongo import MongoClient
import json

MONGO_URI = 'mongodb://192.168.100.36:27017'

client = MongoClient(MONGO_URI)

db = client['bibliotecatec']
collection = db['libro']

f = open('bsamazon.json', encoding= "utf8")
data = json.load(f)

for i in data:
    collection.insert_one({
                            "name": i['Name'],
                            "author": i['Author'],
                            "user_rating": i['User Rating'],
                            "reviews": i['Reviews'],
                            "price": i['Price'],
                            "year": i['Year'],
                            "genre": i['Genre'],
                            "estado": i['estado']
                            })

f.close()