from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime 
from flask_login import UserMixin
from hashlib import md5
from flask import current_app
from time import time
import jwt
from app import db, login

# User tables
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    cash = db.Column(db.Integer)
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    portfolios = db.relationship('Portfolio', backref='stock', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def __init__(self, *args, **kwargs):
        super(User,self).__init__(*args, **kwargs)
        self.cash=10000
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'

    def  get_reset_password_token(self, expires_in=600):
        return jwt.encode({'reset_password': self.id, 'exp': time() + expires_in}, current_app.config['SECRET_KEY'], algorithm='HS256')
    
    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])['reset_password']
        except:
            raise Exception('Invalid Token')
        return User.query.get(id)



@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# Portfolio table
class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(32))
    name = db.Column(db.String(64))
    shares = db.Column(db.Integer)
    price = db.Column(db.Integer)
    type = db.Column(db.String(32))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Portfolio {}>'.format(self.body)