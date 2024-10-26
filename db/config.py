# config.py
import os

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb+srv://swathi:test@yashmongo1.pdwb1iv.mongodb.net/')
