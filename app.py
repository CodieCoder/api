import os
from flask import Flask, Response
from flask_cors import CORS
from waitress import serve
from json import dumps
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
    message = dumps({'message': 'You do not have access to this resource!'})
    return Response(message, 200)


if __name__ == '__main__':
    # serve the app
    serve(app)