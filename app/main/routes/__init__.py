from flask import current_app
from .. import main

@main.route('/')
@main.route('/index')
def index():
    ambiente = current_app.config.get('CONFIG_NAME', 'Desconhecido')
    return f"<h1>hello world - Ambiente: {ambiente}</h1>", 200

