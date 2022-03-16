import sys
sys.path.append(".")
from repository.BBDD_access import DB


def get_items():
    item = DB.get_items()
    h = item['name']
    return { 'name': item['name'], 'sell_in': item['sellIn'], 'quality': item['quality'] }

get_items()