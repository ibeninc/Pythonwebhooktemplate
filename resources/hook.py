import os
import flask
from flask import make_response, render_template
from flask_restful import Resource, reqparse
import random
import requests
import json
import os

class Webhook(Resource):

    def get(self):
        # handle and get params from callback url
        data = flask.request.args.get("code")


    def post(self):
        # Handle Webhook post callback in json
        data = flask.request.get_json()
        print(data)

