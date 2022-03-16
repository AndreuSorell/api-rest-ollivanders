import sys
sys.path.append(".")
from repository.BBDD_access import DB


def get_items(name):
    item = DB.get_items(name)
    # return { 'name': item['name'], 'sell_in': item['sellIn'], 'quality': item['quality'] }
    return item
# get_items()