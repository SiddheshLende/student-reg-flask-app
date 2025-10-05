import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "devkey")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "mysql+pymysql://studuser:StrongPassword!@localhost/studreg"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
