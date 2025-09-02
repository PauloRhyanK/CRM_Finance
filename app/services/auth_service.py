# Arquivo: app/services/auth_service.py

from app import db
from app.models.user_model import User

def register_new_user(form_data):
    """
    Serviço para registrar um novo usuário.
    Recebe um dicionário com os dados do formulário.
    """
    email = form_data.get('ds_user_email')
    
    if User.query.filter_by(ds_user_email=email).first():
        return None, "Email já cadastrado."

    new_user = User(
        ds_user=form_data.get('ds_user'),
        ds_user_email=email,
        dt_user_nasc=form_data.get('dt_user_nasc'),
        cd_role=form_data.get('cd_role', 1) )

    new_user.set_password(form_data.get('password'))

    db.session.add(new_user)
    db.session.commit()

    return new_user, "Usuário registrado com sucesso!"


def authenticate_user(form_data):
    """
    Serviço para autenticar um usuário.
    Recebe um dicionário com email e senha.
    """
    email = form_data.get('ds_user_email')
    password = form_data.get('password')

    user = User.query.filter_by(ds_user_email=email).first()

    if user and user.check_password(password):
        return user, "Login bem-sucedido."
    
    return None, "Email ou senha inválidos."