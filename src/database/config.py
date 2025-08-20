import psycopg2
import os

conn = psycopg2.connect()

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentConfig :
    DEBUG = True # DEP do Flask
    
    DB_USER = os.getenv('POSTGRES_USER', 'default_user')
    DB_PASSWORD = os.getenv('POSTGRES_USER', 'default_user')
    DB_NAME = os.getenv('POSTGRES_USER', 'default_user')
    DB_HOST = 'database' #Nome do service do postgres
    
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'
