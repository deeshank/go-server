from flask_mongoengine import MongoEngine
from flask import Flask

VERSION='v1'
HOSTNAME='localhost'
PORT=5000

db = MongoEngine()

def create_app(*args,**kwargs):
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')
    app.config.update(kwargs)

    db.init_app(app)

    from opnr.views import opnr_app

    app.register_blueprint(opnr_app)

    return app
