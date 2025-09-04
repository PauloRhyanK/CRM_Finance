#!/bin/bash
# Script de inicialização para Linux/Unix/WSL

export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=5000

# Ativa o ambiente virtual e executa o Flask
source .venv/bin/activate
flask run