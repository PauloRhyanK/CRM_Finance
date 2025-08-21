# Arquivo: app/services/auth_service.py

from app import db
from app.models.user_model import User

def register_new_user(form_data):
    """
    Serviço para registrar um novo usuário.
    Recebe um dicionário com os dados do formulário.
    """
    email = form_data.get('ds_user_email')
    
    # 1. Guarda de segurança: Verifica se o usuário já existe no banco
    if User.query.filter_by(ds_user_email=email).first():
        # Retorna um erro indicando que o email já está em uso
        return None, "Email já cadastrado."

    # 2. Cria a nova instância do usuário com os dados recebidos
    new_user = User(
        ds_user=form_data.get('ds_user'),
        ds_user_email=email,
        dt_user_nasc=form_data.get('dt_user_nasc'),
        cd_role=form_data.get('cd_role', 1) # Define '1' como role padrão se não for fornecido
    )

    # 3. USA O MÉTODO SEGURO para definir o hash da senha
    new_user.set_password(form_data.get('password'))

    # 4. Adiciona à sessão e salva no banco de dados
    db.session.add(new_user)
    db.session.commit()

    # 5. Retorna o usuário criado e uma mensagem de sucesso
    return new_user, "Usuário registrado com sucesso!"


def authenticate_user(form_data):
    """
    Serviço para autenticar um usuário.
    Recebe um dicionário com email e senha.
    """
    email = form_data.get('ds_user_email')
    password = form_data.get('password')

    # 1. Busca o usuário pelo email
    user = User.query.filter_by(ds_user_email=email).first()

    # 2. Verifica se o usuário existe E se a senha está correta
    #    usando nosso método seguro que compara os hashes.
    if user and user.check_password(password):
        # Retorna o usuário se a autenticação for bem-sucedida
        return user, "Login bem-sucedido."
    
    # Retorna None se o usuário não existir ou a senha estiver incorreta
    return None, "Email ou senha inválidos."