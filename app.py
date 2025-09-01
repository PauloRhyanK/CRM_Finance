import os
from app import create_app

config_name = os.getenv('FLASK_CONFIG') or os.getenv('FLASK_ENV') or 'default'
# Chama a nossa 'fábrica' para criar a instância da aplicação
app = create_app(config_name)
print(f"[DEBUG] app.debug = {app.debug}")
print(f"[DEBUG] config_name = {config_name}")

# Make the app available for flask command
application = app

if __name__ == '__main__':
    # O host='0.0.0.0' é importante para que a aplicação seja acessível
    # de fora do contêiner Docker.
    #app.run(host='0.0.0.0', port=5000)
    app.run()