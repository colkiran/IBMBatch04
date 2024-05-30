
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWrold(Resource):

    def get(self):
        return {'Message': "Hello World"}


api.add_resource(HelloWrold, "/helloworld")

if __name__ == '__main__':
    app.run(debug=True, use_reloader = True)
    