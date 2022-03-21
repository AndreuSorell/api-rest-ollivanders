from flask import Flask, request, jsonify
from flask_restful import Api
from controller.stock import Stock

app = Flask(__name__)

api = Api(app, catch_all_404s=True)

api.add_resource(Stock, '/stock')

@app.route('/')
def index():
    return '<h1>Olivanders Shop</h1>'

# @app.route('/stock', methods=['POST'])
# def create_item():
#      # Receiving Data
#     name = request.json['name']
#     sellIn = request.json['sellIn']
#     quality = request.json['quality']
#     if name and sellIn and quality:
#         id = mongo.db.users.insert(
#             {'name': name, 'sellIn': sellIn, 'quality': quality})
#         response = jsonify({
#             '_id': str(id),
#             'name': name,
#             'quality': quality,
#             'sellIn': sellIn
#         })
#         response.status_code = 201
#         return response
#     else:
#         return "not_found()"


if __name__ == "__main__":
    app.run(debug=True)