import os

from flask import Flask

def create_app():

    # instantiate the app
    app = Flask(__name__)
    # register blueprints
    from server.main.views import main_blueprint
    app.register_blueprint(main_blueprint)
    return app
