from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt
from flask import jsonify
from app.services.user_validate import validate_user

# ...

# Custom error handler
def custom_invalid_token_callback(error):
    return jsonify({'err': 'Invalid token or Modified token'}), 401

# Other error handlers
def custom_unauthorized_callback(error):
    return jsonify({'err': "Unauthorized User"}), 401

def custom_expired_token_callback(error,info):
    return jsonify({'err': "Token has expired"}), 401


    