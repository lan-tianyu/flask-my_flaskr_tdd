from app import db


class Flaskr(db.model):
    __tablename__ = 'flaskr'
    post_id = db.Column(db.Integer, primary_key=True)
