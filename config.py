import os
from dotenv import load_dotenv

load_dotenv()

DB_CLIENT = os.environ.get("DB_CLIENT")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")


# MONGO_URI = f"mongodb://{DB_CLIENT}:{DB_PORT}/{DB_NAME}"
MONGO_URI = f"mongodb+srv://Harsh:{DB_PASSWORD}@cluster0.tsowggv.mongodb.net/?retryWrites=true&w=majority"

SECRET_KEY = f"your-secret-key"

JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")