# app/services/auth_service.py

from app import db
from app.models.user_model import User
from app.util.exceptions import UserAlreadyExistsError, AuthenticationError

def register_new_user(form_data):
    """Registra um novo usuário. Levanta UserAlreadyExistsError se o email já existir."""
    email = form_data.get('ds_user_email')
    if User.query.filter_by(ds_user_email=email).first():
        raise UserAlreadyExistsError()

    new_user = User(
        ds_user=form_data.get('ds_user'),
        ds_user_email=email
    )
    new_user.set_password(form_data.get('password'))

    db.session.add(new_user)
    db.session.commit()
    return new_user  # Retorna apenas o objeto no caminho feliz

def authenticate_user(form_data):
    """Autentica um usuário. Levanta AuthenticationError se as credenciais forem inválidas."""
    email = form_data.get('ds_user_email')
    password = form_data.get('password')

    user = User.query.filter_by(ds_user_email=email).first()

    if not user or not user.check_password(password):
        raise AuthenticationError()
    
    return user  # Retorna apenas o objeto no caminho feliz