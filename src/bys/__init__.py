import os

from flask import Flask


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True, static_folder="../static")
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev"
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_json("config.json")
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from bys import db
    db.init()

    from bys import urls

    app.register_blueprint(urls.bp)

    app.add_url_rule("/", endpoint="index")

    return app