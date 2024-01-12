from flask import Blueprint, url_for, request, redirect, Response, session
import flask
from models import User
from utils.password import set_password, check_password
from json import dumps

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    response = flask.jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    if request.method == 'POST':
        json_data = request.json
        email = json_data.get("email")
        password = json_data.get("password")
        print(json_data.get("email"))

        user = User.objects(email=email).first()
        if user:
            if check_password(user.password, password):
                # Manual session management
                session['user_id'] = str(user.id)

                data_to_return = {
                    "email": user.email,
                    "firstName": user.firstName,
                    "lastName": user.lastName,
                    "maritalStatus": user.maritalStatus,
                    "country": user.country,
                }
                success_message = dumps(data_to_return, skipkeys=True)
                return Response(success_message, 201)

            else:
                error_message = dumps({"message": "Invalid email/password"})
                return Response(error_message, 401)
        else:
            error_message = dumps({"message": "Invalid email/password"})
            return Response(error_message, 401)
    else:
        error_message = dumps({"message": "Invalid request"})
        return Response(error_message, 401)


@auth.route('/logout')
def logout():
    # Manual session management
    session.pop('user_id', None)
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        json_data = request.json
        email = json_data.get('email')
        first_name = json_data.get('firstName')
        last_name = json_data.get('lastName')
        password = json_data.get('password')
        password2 = json_data.get('password2')
        user = User.objects(email=email).first()
        if user:
            error_message = dumps({"message": "Email already in use"})
            return Response(error_message, 401)
        elif not email and len(email) < 5:
            error_message = dumps({"message": "Invalid email address"})
            return Response(error_message, 401)
        elif not first_name or len(first_name) < 2:
            error_message = dumps({"message": "Invalid first name"})
            return Response(error_message, 401)
        elif not last_name or len(last_name) < 2:
            error_message = dumps({"message": "Invalid last name"})
            return Response(error_message, 401)
        elif password != password2:
            print(password, password2)
            error_message = dumps({"message": "Both password do not match"})
            return Response(error_message, 401)
        else:
            hashed_password = set_password(password)
            result = User(email=email, firstName=first_name, lastName=last_name, password=hashed_password).save()
            if result:
                # Manual session management
                session['user_id'] = str(result.id)

                data_to_post = {"firstName": result.firstName, "lastName": result.lastName, "email": result.email,
                                "maritalStatus": result.maritalStatus, "country": result.country}
                success_message = dumps(data_to_post)
                return Response(success_message, 201)
            else:
                error_message = dumps({"message": "Could not create new user. Please try again"})
                return Response(error_message, 401)