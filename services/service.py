import sys
sys.path.append(".")
from repository.BBDD_access import DB


def get_items():
    items = DB.get_items()
    return items

get_items()