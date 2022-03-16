import re
import pymongo

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
    