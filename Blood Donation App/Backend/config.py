# Backend/config.py

import os

DB_USER = "root"       # change to your MySQL user
DB_PASSWORD = "password"   # change to your MySQL password
DB_HOST = "localhost"
DB_NAME = "blood_donation"

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
