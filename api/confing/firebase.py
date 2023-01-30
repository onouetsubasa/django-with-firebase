import firebase_admin
from firebase_admin import credentials
import json
import os


firebase_info = {
    "type": "service_account",
    'apiKey': os.environ.get('FIREBASE_API_KEY'),
    'authDomain': os.environ.get('FIREBASE_AUTH_INFO'),
    'projectId': os.environ.get('FIREBASE_PROJECT_ID'),
    'storageBucket': os.environ.get('FIREBASE_STORAGE_BUCKET'),
    'messagingSenderId': os.environ.get('FIREBASE_MESSAGE_SENDER_ID'),
    'appId': os.environ.get('FIREBASE_APP_ID'),
    'measurementId': os.environ.get('FIREBASE_MEASUREMENT_ID')
}

firebase_json = json.dumps(firebase_info, ensure_ascii=False, indent=2)

cred = credentials.Certificate(firebase_json)
firebase_admin.initialize_app(cred)


