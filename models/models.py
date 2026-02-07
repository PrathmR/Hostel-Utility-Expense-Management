from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UtilityRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_no = db.Column(db.String(10), nullable=False)
    electricity = db.Column(db.Float, nullable=False)
    water = db.Column(db.Float, nullable=False)
    wifi = db.Column(db.Float, nullable=False)
