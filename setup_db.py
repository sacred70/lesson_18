from flask_sqlalchemy import SQLAlchemy
#  инициализируем БД
db = SQLAlchemy()
session = db.session