from flask import Flask, render_template, request, url_for, redirect
from app.main import mongo
from app.v1.main import bp
from app.models.user import User
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity




@bp.route("/all-registered-users/", methods=["GET"])
@jwt_required()
def show_all_users():
    try:
        current_user = get_jwt_identity()
        data = User.objects.only("user_name","name")
        if not data:
            return jsonify({"err":"No User Found"}),404

        return jsonify(data) , 200

    except Exception as err:
        print(str(err))
        return jsonify({"err":str(err)}),400