from datetime import datetime
from flaskblog import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description =db.Column(db.String, nullable=True)
    isDone = db.Column(db.Boolean, default=False)
    date_due = db.Column(db.DateTime)
    # skill = db.relationship("") ← relationship with skill db [later]

    def __repr__(self):
        # how the object is printed when we print it out
        return f"User('{self.id}','{self.title}','{self.description}','{self.isDone}')"