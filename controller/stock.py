from flask_restful import Resource, reqparse
import sys
sys.path.append(".")
from services.service import get_items

class Stock(Resource):
    def get(self, name):
        return get_items(name)