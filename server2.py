#!/usr/bin/env python3

from flask import Flask
from flask_restful import Api, Resource
import json
app = Flask(__name__)
api = Api(app)
class My_Data(Resource):
 def get(self):
   with open('myfile.json') as json_file:
     data = json.load(json_file)
     return data
api.add_resource(My_Data, "/holidays")
if __name__ == "__main__":
 app.run(debug=True)
