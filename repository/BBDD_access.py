import re
import pymongo

class DB():
    uri = 'mongodb+srv://admin:admin@cluster0.thpbm.mongodb.net/ollivanders?retryWrites=true&w=majority'
    
    global collection

    # Utilizamos una funcion de pymongo para conectarnos a la base de datos
    client = pymongo.MongoClient(uri)
    client.server_info() # Fuerza la conexion, si no se conecta pasa al except
    db = client.ollivanders
    collection = db.stock

    @classmethod
    def get_items(cls):
        for document in collection.find({"name": "Aged Brie"}):
            return document
    