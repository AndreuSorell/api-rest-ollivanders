import json

with open("stock_mock.json") as json_file:
    items = json.load(json_file)

def stock():
    return items