from pymongo import MongoClient

MONGO_URI = 'mongodb://192.168.100.36:27017'

client = MongoClient(MONGO_URI)

db = client['bibliotecatec']
collection = db['libro']
libro = collection.find({})

index = 0
for x in libro:
    print(x)