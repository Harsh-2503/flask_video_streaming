from flask import Flask, Response,render_template, request, redirect,jsonify
import json
from werkzeug.datastructures import MultiDict
from flask_cors import CORS
from config import MONGO_URI,JWT_SECRET_KEY
from flask_mongoengine import MongoEngine
import cv2
import os
from flask_socketio import SocketIO
import base64
import time
import threading
from app.schemas.user import AddUser,OverlayItemForm,GetUser
from app.models.user import User
from flask_validate_json import validate_json


app = Flask(__name__)
CORS(app)
socketio = SocketIO(app,cors_allowed_origins="*")

user_states = {}

os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;tcp'


def generate_frames(user_id,rtsp_url):
    print(rtsp_url, "yo")
    cap = cv2.VideoCapture(rtsp_url)
    
    while True:
        with user_states[user_id]['frame_lock']:
            if not user_states[user_id]['send_frames']:
                continue

        success, frame = cap.read()
        if not success:
            break

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = base64.b64encode(buffer).decode('utf-8')

        socketio.emit('frame', {'frame': frame_bytes, 'sid':user_id}, namespace='/test', room=user_id)

@socketio.on('rtsp_url', namespace='/test')
def handle_connect(data):
    user_id = request.sid
    print(f'User {user_id} connected')
    
    user_states[user_id] = {'send_frames': True, 'frame_lock': threading.Lock()}
    socketio.start_background_task(target=generate_frames, user_id=user_id, rtsp_url = data)

@app.route('/pause', methods=['POST'])
def pause_frames():
    user_id = request.json.get('sid')
    with user_states[user_id]['frame_lock']:
        user_states[user_id]['send_frames'] = False
    return "Frames paused"

@app.route('/play', methods=['POST'])
def play_frames():
    user_id = request.json.get('sid')
    with user_states[user_id]['frame_lock']:
        user_states[user_id]['send_frames'] = True
    return "Frames resumed"

from flask import request, jsonify
import json

@app.route('/add-user', methods=['POST'])
def add_user():  
    user = AddUser(request.form)
    if not user.validate():
        return jsonify({"err": user.errors}, 400)

    data = user.data
    user = User.objects(user_name=data["user_name"]).first()
    if user:
        return jsonify({"err":"User Already Exists"})

    user = User(**data).save()

    return jsonify({"data": data})


@app.route('/get-user', methods=['POST'])
def get_user():  

    data = request.form

    if not data.get("user_name"):
        return jsonify({"err":"bad request"})

    user = User.objects(user_name=data.get("user_name")).first()
    if not user:
        return jsonify({"err":"User Doesn't Exists"})

    return jsonify(user),200


@app.route('/overlays', methods=['PUT'])
def overlays():  
    user = GetUser(request.form)
    if not user.validate():
        return jsonify({"err": user.errors}, 400)

    data = user.data
    user = User.objects(user_name=data["user_name"]).first()


    if not user:
        return jsonify({"err":"User Doesn't exists"})

    user.update(**data)



    return jsonify({"data": data})


@app.route("/")
def hello():
  return "Hello World!"

app.config["MONGODB_HOST"] = MONGO_URI
# jwt = JWTManager(app)

# jwt.invalid_token_loader(custom_invalid_token_callback)
# jwt.unauthorized_loader(custom_unauthorized_callback)
# jwt.expired_token_loader(custom_expired_token_callback)


# app.config.from_object('config')

mongo = MongoEngine()
mongo.init_app(app)


# from app.v1.main import bp as auth_bp
# app.register_blueprint(auth_bp,url_prefix="/v1")




    
