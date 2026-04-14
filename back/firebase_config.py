import pyrebase
from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET")
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()