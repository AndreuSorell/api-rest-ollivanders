from flask import Flask
from flask_restful import Api
from stock import Stock

app = Flask(__name__)

api = Api(app, catch_all_404s=True)

api.add_resource(Stock, '/stock')

@app.route('/')
def index():
    return '<h1>Olivanders Shop</h1>'

if __name__ == "__main__":
    app.run(debug=True)