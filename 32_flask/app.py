import logging
from flask import Flask
from config import AppConfig
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = Flask(__name__)
app.logger.setLevel(logging.INFO)
app.config.from_object(AppConfig)
db.init_app(app)


from views import *
from models import *


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host=app.config.get('HOST'),
            port=app.config.get('PORT'),
            debug=app.config.get('DEBUG'))
