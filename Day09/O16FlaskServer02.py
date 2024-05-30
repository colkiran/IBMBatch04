
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

products = {
    'pepsi': {'item': '2 ltr Bottle', 'price': 120,'qty': 200},
    'coke': {'item': '500 ml Bottle', 'price': 40, 'qty': 450},
    'thumbs_up':{'item': '300 ml CAN', 'price': 45, 'qty': 150}
}
class Products(Resource):

    def get(self, product):
        return {product: products[product]}

api.add_resource(Products, "/getproduct/<product>")

if __name__ == '__main__':
    app.run(debug=True, use_reloader = True)

