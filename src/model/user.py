
from flask import current_app
from app import db

class User(db.Model):
    __tablename__ = 'users'
    cd_user = db.Column(db.Integer, primary_key=True)
    ds_user = db.Column(db.String(100))
    ds_user_email = db.Column(db.String(100))
    ds_user_password = db.Column(db.String(100))
    dt_user_nasc = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    dt_user_create = db.Column(db.DateTime, default=db.func.current_timestamp())
    cd_role = db.Column(db.Integer, db.ForeignKey('roles.cd_role'))

    def __init__(self, ds_user, ds_user_email, ds_user_password, dt_user_nasc, cd_role):
        self.ds_user = ds_user
        self.ds_user_email = ds_user_email
        self.ds_user_password = ds_user_password
        self.dt_user_nasc = dt_user_nasc
        self.cd_role = cd_role

    def login(self, ds_user_email, ds_user_password):
        user = User.query.filter_by(ds_user_email=ds_user_email, ds_user_password=ds_user_password).first()
        return user

    def logout(self):
        pass

    def register(self, ds_user, ds_user_email, ds_user_password, dt_user_nasc, cd_role):
        new_user = User(ds_user=ds_user, ds_user_email=ds_user_email, ds_user_password=ds_user_password, dt_user_nasc=dt_user_nasc, cd_role=cd_role)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    