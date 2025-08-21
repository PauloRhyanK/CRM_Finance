from app import create_app

# Chama a nossa 'fábrica' para criar a instância da aplicação
app = create_app()

if __name__ == '__main__':
    # O host='0.0.0.0' é importante para que a aplicação seja acessível
    # de fora do contêiner Docker.
    app.run(host='0.0.0.0', port=5000)