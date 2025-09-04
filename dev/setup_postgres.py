# Script para configurar PostgreSQL local
# Execute este arquivo com: python setup_postgres.py

import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

def create_database():
    """
    Cria o banco de dados PostgreSQL se não existir
    """
    db_name = os.getenv('POSTGRES_DB', 'crm_db')
    db_user = os.getenv('POSTGRES_USER', 'postgres')
    db_password = os.getenv('POSTGRES_PASSWORD', '1234')
    db_host = os.getenv('DB_HOST', 'localhost')
    
    try:
        # Conecta ao PostgreSQL (banco padrão 'postgres')
        connection = psycopg2.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database='postgres'  # Banco padrão para criar outros bancos
        )
        connection.autocommit = True
        cursor = connection.cursor()
        
        # Verifica se o banco já existe
        cursor.execute(
            "SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s",
            (db_name,)
        )
        exists = cursor.fetchone()
        
        if not exists:
            # Cria o banco de dados
            cursor.execute(
                sql.SQL("CREATE DATABASE {}").format(
                    sql.Identifier(db_name)
                )
            )
            print(f"✅ Banco de dados '{db_name}' criado com sucesso!")
        else:
            print(f"ℹ️  Banco de dados '{db_name}' já existe.")
            
        cursor.close()
        connection.close()
        
        return True
        
    except psycopg2.Error as e:
        print(f"❌ Erro ao conectar com PostgreSQL: {e}")
        print("💡 Verifique se:")
        print("   - PostgreSQL está instalado e rodando")
        print("   - Usuário e senha estão corretos no .env")
        print("   - Serviço PostgreSQL está ativo")
        return False

def test_connection():
    """
    Testa a conexão com o banco criado
    """
    db_name = os.getenv('POSTGRES_DB', 'crm_db')
    db_user = os.getenv('POSTGRES_USER', 'postgres')
    db_password = os.getenv('POSTGRES_PASSWORD', '1234')
    db_host = os.getenv('DB_HOST', 'localhost')
    
    try:
        connection = psycopg2.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"✅ Conexão testada com sucesso!")
        print(f"📋 PostgreSQL version: {version[0]}")
        
        cursor.close()
        connection.close()
        return True
        
    except psycopg2.Error as e:
        print(f"❌ Erro ao testar conexão: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Configurando PostgreSQL para desenvolvimento...")
    print("=" * 50)
    
    if create_database():
        if test_connection():
            print("\n🎉 PostgreSQL configurado com sucesso!")
            print("📝 Próximos passos:")
            print("   1. flask db init")
            print("   2. flask db migrate -m 'Initial migration'")
            print("   3. flask db upgrade")
            print("   4. python init_data.py")
            print("   5. ./init.ps1")
        else:
            print("\n⚠️  Banco criado, mas há problema na conexão.")
    else:
        print("\n❌ Não foi possível configurar o PostgreSQL.")
        print("💡 Considere usar SQLite como alternativa:")
        print("   - Descomente SQLALCHEMY_DATABASE_URI = 'sqlite:///crm_finance.db' no config.py")
        print("   - Comente as linhas PostgreSQL no config.py")
