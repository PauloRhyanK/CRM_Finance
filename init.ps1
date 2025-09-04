# Script de inicialização para Windows PowerShell
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development" 
$env:FLASK_RUN_HOST = "0.0.0.0"
$env:FLASK_RUN_PORT = "5000"

# Ativa o ambiente virtual e executa o Flask
C:/Programs/Repositorios/Faculdade/CRM_Finance/.venv/Scripts/flask.exe run
