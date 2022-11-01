from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'you-will-never-guess'

    app.debug = True

    from .routes import index_blueprint

    app.register_blueprint(index_blueprint)

    return app
