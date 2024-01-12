
from werkzeug.security import generate_password_hash, check_password_hash

def set_password(password):
        return generate_password_hash(password, method='sha256')

def check_password(pwhash, password):
        return check_password_hash(pwhash, password)