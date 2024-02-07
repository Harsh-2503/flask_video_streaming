from flask_bcrypt import check_password_hash
from flask import jsonify
from app.models.user import User


def validate_user(data):

    if not data.validate():
        return jsonify({"err":data.errors},400)

    user = data.data

    user_name = user.get("user_name")
    data = User.objects(user_name=user_name).first()
    if not data:
        return jsonify({"err":"Check User Name or Password"}),404

    data = data.to_mongo().to_dict()

    valid_user = check_password_hash(data.get("password"), user.get("password"))

    if not valid_user:
        return jsonify({"err":"Check User Name or Password"}) , 404


    return jsonify({"valid_user":valid_user}) , 200



def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = data['username']
        except jwt.ExpiredSignatureError:
            new_token = jwt.encode({'username': current_user, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return jsonify({'message': 'Token has expired', 'new_token': new_token.decode('utf-8')}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

        return f(current_user, *args, **kwargs)

    return decorated