import pymongo
import json

class DB():
    uri = 'mongodb+srv://admin:admin@cluster0.thpbm.mongodb.net/ollivanders?retryWrites=true&w=majority'
    
    global collection

    client = pymongo.MongoClient(uri)
    client.server_info()
    collection = client.ollivanders.stock

    @classmethod
    def get_items(cls, name):
        for document in collection.find({"name": name},{"_id":False}):
            return document

with open("stock_mock.json") as json_file:
        items = json.load(json_file)

def insertar(items):
    collection.insert_many(items)
    
# insertar(items)