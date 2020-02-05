from flask import Blueprint, render_template

from project.api.models import Training, Player


stats_blueprint = Blueprint("stats", __name__, url_prefix="/stats")


@stats_blueprint.route("/trainings", methods=["GET"])
def trainings():
    return render_template("trainings.html", trainings=Training.query.all())


@stats_blueprint.route("/players", methods=["GET"])
def players():
    raw_players = Player.query.all()
    # shitty counter but the number is low, so...
    num_of_trainings = len(Training.query.all())
    players = []
    for p in raw_players:
        players.append(
            {
                "name": f"{p.lname} {p.fname}",
                "num_trainings": len(p.trainings),
                "training_percentage": int(len(p.trainings) / num_of_trainings * 100),
            }
        )
    return render_template("players.html", players=players)
