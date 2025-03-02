from dataclasses import dataclass
from src import db

@dataclass
class User(db.Model):
    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    age: int

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)