from flask import Blueprint

opnr_app = Blueprint('opnr_app',__name__)

@opnr_app.route('/')
def index():
    return '<h3>Welcome to opnr API!</h3>'
