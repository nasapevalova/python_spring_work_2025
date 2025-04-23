from flask import Flask
from models import User, Note, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:password@localhost/students' #'sqlite:///users.db'

db.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    print('Создана база данных users')