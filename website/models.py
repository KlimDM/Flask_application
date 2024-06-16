from . import db
from flask_login import UserMixin
from sqlalchemy import func


class User(db.Model, UserMixin):
    __tablename__ = "Пользователи"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    firstName = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now(tz='Europe/Moscow'))
