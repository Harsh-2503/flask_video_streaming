from flask import Flask, render_template, request, url_for, redirect
from app.main import mongo
from app.v1.main import bp
from app.models.user import User
from app.models.note import Note
from flask import jsonify
from flask_bcrypt import generate_password_hash,check_password_hash
from app.schemas.user import AddUser,ValidateUser
from app.schemas.note import AddNote, UpdateNote
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, create_refresh_token



@bp.route("/signup/", methods=["POST"])
def signup():
    try:
        data = AddUser(request.form)
        print(data.validate())
        
        if not data.validate():
            return jsonify({"err":data.errors},400)

        user = data.data
        User(**user).validate(clean=True)
        pw_hash = generate_password_hash(user.get("password"), 10)
        user["password"] = pw_hash
        User(**user).save()

        access_token = create_access_token(identity=user.get("user_name"))
        refresh_token = create_refresh_token(identity=user.get("user_name"))

        return jsonify({'access_token': access_token,"refresh_token":refresh_token}), 201

    except Exception as err:
        print(str(err))
        return jsonify({"err":str(err)}),400


@bp.route("/login/", methods=["GET"])
def login():
    try:
        data = ValidateUser(request.form)
        user = data.data

        user_name = user.get("user_name")
        data = User.objects(user_name=user_name).first()
        if not data:
            return jsonify({"err":"Check User Name or Password"}),404

        data = data.to_mongo().to_dict()

        valid_user = check_password_hash(data.get("password"), user.get("password"))

        if not valid_user:
            return jsonify({"err":"Check User Name or Password"}) , 404

        access_token = create_access_token(identity=user_name)
        refresh_token = create_refresh_token(identity=user_name)

        return jsonify({'access_token': access_token,"refresh_token":refresh_token}), 201


    except Exception as err:
        print(str(err))
        return jsonify({"err":str(err)}),400


@bp.route("/refresh/",methods=["GET"])
@jwt_required(refresh=True)
def refresh():
    try:
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return jsonify(access_token=access_token), 201
    except Exception as err:
        print(str(err))
        return jsonify({"err":str(err)}),400


