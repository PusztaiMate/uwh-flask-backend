from flask import Blueprint, render_template

from project import db
from project.api.models import Training, Player


views_blueprint = Blueprint("views", __name__, url_prefix="/statisztika")


class DummyTraining:
    def __init__(self, date, num_of_players):
        self.date = date
        self.num_of_players = num_of_players
    
    def __str__(self):
        return f"Training({self.date}, {self.num_of_players} players)"
    
dummy_trainings = [
    DummyTraining("2020-01-01", 20),
    DummyTraining("2020-01-03", 22),
    DummyTraining("2020-01-08", 13)
]


@views_blueprint.route("/edzés", methods=["GET"])
def trainings():
    return render_template("trainings.html", trainings=Training.query.all())


@views_blueprint.route("/játékos", methods=["GET"])
def players():
    return render_template("players.html", players=Player.query.all())