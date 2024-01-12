from json import dumps
from flask import Flask, Response
from pymongo import MongoClient

app = Flask(__name__)

db_client = MongoClient("mongodb+srv://develop:7HV4hsiVxS2JhjtV@develop.9co1n6k.mongodb.net/?retryWrites=true&w=majority")

# try:
#     db_client.admin.command('ping')
#     print('Pinged your deployment. You successfully connected to MongoDB!')
# except Exception as e:
#     print(e)

@app.route('/')
def home():
    message = dumps({'message': 'You do not have access to this resource!'})
    return Response(message, 200)


@app.route('/login', methods=['POST'])
def login():
    message = dumps({'message': 'You have logged in successfully!'})
    return Response(message, 200)

if __name__ == '__main__':
    app.run()