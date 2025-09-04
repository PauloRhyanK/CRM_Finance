@echo off
REM Script de inicialização para Windows Command Prompt

set FLASK_APP=app.py
set FLASK_ENV=development
set FLASK_RUN_HOST=0.0.0.0
set FLASK_RUN_PORT=5000

REM Ativa o ambiente virtual e executa o Flask
C:\Programs\Repositorios\Faculdade\CRM_Finance\.venv\Scripts\flask.exe run
