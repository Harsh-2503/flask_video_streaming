from flask import Flask, render_template, request, url_for, redirect
from app.main import mongo
from app.v1.main import bp
from app.models.user import User
from app.models.note import Note
from flask import jsonify
from app.schemas.note import AddNote, UpdateNote
from flask_jwt_extended import jwt_required, get_jwt_identity



@bp.route("/create-note/",methods=["POST"])
@jwt_required()
def create_note():
    try:
        current_user = get_jwt_identity()

        data = AddNote(request.form)
        
        if not data.validate():
            return jsonify({"err":data.errors},400)

        user = User.objects(user_name=current_user).first()
        if not user:
            return jsonify({"err":"No User Found"}), 404

        data = data.data
        data["user"] = user

        note = Note(**data).save()

        return jsonify(note),201

    except Exception as err:
        print(str(err))
        return jsonify({"err":str(err)}),400


@bp.route("/get-notes/",methods=["GET"])
@jwt_required()
def get_notes():
    try:
        current_user = get_jwt_identity()

        user = User.objects(user_name=current_user).first()
        if not user:
            return jsonify({"err":"No User Found"}), 404


        notes = Note.objects(user=user)

        return jsonify(notes),200
    except Exception as err:
        print(str(err))
        return jsonify({"err":str(err)}),400



@bp.route("/update-note/<id>/",methods=["PUT"])
@jwt_required()
def update_note(id):

    try:
        current_user = get_jwt_identity()

        data = UpdateNote(request.form)
        
        if not data.validate():
            return jsonify({"err":data.errors},400)

        data = data.data

        user = User.objects(user_name=current_user).first()

        if not user:
            return jsonify({"err":"No User Found"}), 404

        note = Note.objects(id=id,user=user).first()
        if not note:
            return jsonify({"err":"No Note found"}), 404

        note.update(**data)

        
        return jsonify(note),200

    except Exception as err:
        print(str(err))
        return jsonify({"err":str(err)}),400


@bp.route("/delete-note/<id>/",methods=["DELETE"])
@jwt_required()
def delete_note(id):
    try:
        current_user = get_jwt_identity()

        user = User.objects(user_name=current_user).first()

        if not user:
            return jsonify({"err":"No User Found"}), 404

        note = Note.objects(id=id,user=user).first()
        if not note:
            return jsonify({"err":"No Note found"}), 404

        note.delete()

        return jsonify({"success":"Note Deleted"}),200

    except Exception as err:
        print(str(err))
        return jsonify({"err":str(err)}),400