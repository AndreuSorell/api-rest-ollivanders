from flask_restful import Resource
from repository.data_access import stock

class Stock(Resource):
    def get(self):
        return stock()