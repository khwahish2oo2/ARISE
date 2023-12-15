import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("login-database-a039a-firebase-adminsdk-nl21h-077c59e4c6.json")
firebase_admin.initialize_app(cred)
