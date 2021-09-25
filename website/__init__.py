from flask import Flask
from website.dconnect import connect

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'qwerty'
    connect.init_app(app)
    from .views import views

    app.register_blueprint(views,url_prefix='/')
    return app


    