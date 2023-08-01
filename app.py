import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin
from resources.hook import Webhook


app= Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(Webhook, '/')

if __name__ == '__main__':
    app.run(port=5000, debug='true')