from flask import Blueprint

bp = Blueprint('auth', __name__)
from app.v1.routes import auth
from app.v1.routes import user
from app.v1.routes import note