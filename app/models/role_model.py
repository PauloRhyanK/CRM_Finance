# Arquivo: app/models/role_model.py

from app import db

class Role(db.Model):
    __tablename__ = 'roles'

    cd_role = db.Column(db.Integer, primary_key=True)
    ds_role = db.Column(db.String(80), unique=True, nullable=False)
    ds_description = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'<Role {self.ds_role}>'
