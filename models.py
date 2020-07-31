from app import db


class Flaskr(db.model):
    __tablename__ = 'flaskr'

    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return f"<title {self.body}>"

