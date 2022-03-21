import sys
sys.path.append(".")
from repository.BBDD_access import *

class Services():
    def get_items(query):
        item = DB.get_items(query)
        return item

    def post_items(query):
        DB.post_item(query)
