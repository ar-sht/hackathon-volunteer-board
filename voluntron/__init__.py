import os

from flask import Flask, render_template


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",  #TODO: change before deploying
        DATABASE=os.path.join(app.instance_path, "voluntron.sqlite"),
    )

    app.config.from_pyfile("config.py", silent=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.route("/about")
    def about():
        return render_template("index.html") #TODO: Change this

    @app.route("/dashboard")
    def dashboard():
        return render_template("index.html") #TODO: Change this

    from . import db

    db.init_app(app)

    from . import auth

    app.register_blueprint(auth.bp)

    from . import search

    app.register_blueprint(search.bp)

    return app
