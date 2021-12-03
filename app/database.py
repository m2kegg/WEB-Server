from flask_login.mixins import UserMixin
from app import app, db, loginm
from werkzeug.security import generate_password_hash,  check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key = True)
    email = db.Column(db.String(100), nullable = False)
    username = db.Column(db.String(100), nullable = False, unique = True)
    pw_hash = db.Column(db.String(100), nullable = False)

    def __repr__(self):
	    return "<{}:{}>".format(self.id, self.username)
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
    def check(self, password):
        return check_password_hash(self.pw_hash, password)    
    @loginm.user_loader
    def load_user(userid):
        return db.session.query(User).get(userid)    
