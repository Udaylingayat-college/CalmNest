from pymongo import MongoClient
from backend.config import Config


client = MongoClient(Config.MONGO_URI)
db = client.get_database()

users_collection = db["users"]
tests_collection = db["test_results"]
courses_collection = db["courses"]
notes_collection = db["user_notes"]
