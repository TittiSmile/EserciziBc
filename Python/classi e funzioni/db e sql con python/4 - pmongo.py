import pymongo
from pymongo import MongoClient

client = MongoClient()
client = MongoClient("localhost", 27017)
db = client.pymongo_test

persone = db.persone

persone.create_index = ([("nome",pymongo.ASCENDING)])
p1 = {"nome": "Antonio"}
p2 = {"nome": "Mario"}

persone.insert_one(p1)
