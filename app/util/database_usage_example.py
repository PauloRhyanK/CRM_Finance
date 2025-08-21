"""
Exemplo de uso da classe DatabaseManager
"""
from flask import Flask
from util.database import db_manager

# Exemplo de como usar o DatabaseManager

def exemplo_basico():
    """Exemplo básico de uso"""
    
    # 1. Criar aplicação Flask
    app = Flask(__name__)
    
    # 2. Inicializar o DatabaseManager
    db_manager.init_app(app)
    
    # 3. Usar dentro do contexto da app
    with app.app_context():
        
        # Verificar saúde da conexão
        health = db_manager.health_check()
        print(f"Status do banco: {health}")
        
        # Criar tabelas
        db_manager.create_all_tables()
        
        # Obter estatísticas
        stats = db_manager.get_stats()
        print(f"Estatísticas: {stats}")

def exemplo_transacao():
    """Exemplo usando transações seguras"""
    
    app = Flask(__name__)
    db_manager.init_app(app)
    
    with app.app_context():
        # Usando context manager para transação segura
        try:
            with db_manager.transaction():
                # Suas operações de banco aqui
                # Se der erro, faz rollback automaticamente
                db_manager.execute_raw_sql(
                    "INSERT INTO clientes (nome, email) VALUES (:nome, :email)",
                    {"nome": "João", "email": "joao@email.com"}
                )
                print("Cliente inserido com sucesso!")
                
        except Exception as e:
            print(f"Erro na transação: {e}")

def exemplo_queries_customizadas():
    """Exemplo executando queries personalizadas"""
    
    app = Flask(__name__)
    db_manager.init_app(app)
    
    with app.app_context():
        # Query personalizada
        result = db_manager.execute_raw_sql(
            "SELECT * FROM clientes WHERE empresa = :empresa",
            {"empresa": "Tech Corp"}
        )
        
        # Processar resultado
        clientes = [dict(row) for row in result]
        print(f"Clientes encontrados: {clientes}")

def exemplo_backup():
    """Exemplo de backup de tabela"""
    
    app = Flask(__name__)
    db_manager.init_app(app)
    
    with app.app_context():
        # Criar backup da tabela clientes
        sucesso = db_manager.backup_table("clientes", "clientes_backup_2025")
        
        if sucesso:
            print("Backup criado com sucesso!")
        else:
            print("Erro ao criar backup")

if __name__ == "__main__":
    # Executar exemplos
    exemplo_basico()
    exemplo_transacao()
    exemplo_queries_customizadas()
    exemplo_backup()
