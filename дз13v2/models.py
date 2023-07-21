from app import app, db

class User(db.Model):  
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    login = db.Column(
        db.String(180),
        nullable=False,
        unique=True    
    )  
    password_hash = db.Column(
        db.String(150),
        nullable=False
    )