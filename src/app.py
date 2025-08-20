from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from database.config import DevelopmentConfig 

load_dotenv()
app = Flask(__name__)

app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)
migrate = Migrate(app,db)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)