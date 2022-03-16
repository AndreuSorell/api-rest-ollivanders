from flask_restful import Resource

import sys
sys.path.append(".")
from services.service import get_items

class Stock(Resource):
    def get(self):
        return get_items()