from flask_restful import Resource, reqparse
import sys
sys.path.append(".")
from services.service import Services

class Stock(Resource):
    def __init__(self):
        self.query = reqparse.RequestParser()
        self.query.add_argument("name", type=str)
        self.query.add_argument("sellIn", type=int)
        self.query.add_argument("quality", type=int)
        self.query = dict(self.query.parse_args())
        print(self.query)
    
    def get(self):
        # http.../stock?name=Aged%20Brie
        query = dict(self.query)
        self.remove_null(query)
            
        return Services.get_items(self.query)
    
    def post(self):
        # curl -d '{"name":"capa", "sellIn":5, "quality":10}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/stock
        query = dict(self.query)
        self.remove_null(query)
        Services.post_items(self.query)
        return Services.get_items(self.query)


    def remove_null(self, query):
        # En la request no tienes porque rellenar todos los campos ya que los campos no son 'required'
        for item in query.keys():
            if query[item] == None:
                self.query.pop(item)