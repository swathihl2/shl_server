# db/mongo.py
from pymongo import MongoClient

from db.config import Config

client = MongoClient(Config.MONGO_URI)
db = client['items']
