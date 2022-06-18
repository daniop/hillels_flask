import os

from flask import Flask
import time


def create_app(test_config=None):
    # create and configure the app

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.template_filter()
    def format_seconds(value):
        if time.gmtime(value).tm_hour:
            return time.strftime("%H:%M:%S", time.gmtime(value))
        else:
            return time.strftime("%M:%S", time.gmtime(value))

    from . import db
    db.init_app(app)

    from . import music
    app.register_blueprint(music.bp)

    from . import parse
    app.register_blueprint(parse.bp)

    return app
