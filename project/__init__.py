import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(script_info=None):
    app = Flask(__name__)

    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    db.init_app(app)

    # views
    from project.views.index import index_blueprint
    from project.views.tranings import trainings_view
    from project.views.players import players_view

    # api
    from project.api.ping import ping_blueprint
    from project.api.players import players_api
    from project.api.clubs import clubs_blueprint
    from project.api.trainings import trainings_api

    app.register_blueprint(index_blueprint)
    app.register_blueprint(trainings_view)
    app.register_blueprint(players_view)

    app.register_blueprint(ping_blueprint)
    app.register_blueprint(players_api)
    app.register_blueprint(clubs_blueprint)
    app.register_blueprint(trainings_api)

    from project.api.models import Player, Training, Club

    @app.shell_context_processor
    def ctx():
        return {
            "app": app,
            "db": db,
            "Player": Player,
            "Training": Training,
            "Club": Club,
        }

    return app
