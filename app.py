import os
from flask import Flask, jsonify
from flask_cors import CORS
from waitress import serve
from mongoengine import *
from routes.auth import user_auth


#Create app
app = Flask(__name__)
CORS(app)
mongo_uri = os.environ['MONGO_URI']
connect("users", host=mongo_uri)

# auth routes
app.register_blueprint(user_auth)

@app.route('/')
def home():
    response = jsonify({'message': 'You do not have access to this resource!'})
    return response


if __name__ == '__main__':
    # serve the app
    serve(app)