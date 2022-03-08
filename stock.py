from flask_restful import Resource
from data_access import stock

class Stock(Resource):
    def get(self):
        return stock()