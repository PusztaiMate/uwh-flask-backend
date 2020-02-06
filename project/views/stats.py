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
        train_perc = calculate_training_percentage(len(p.trainings), num_of_trainings)
        color = determine_color(train_perc)
        players.append(
            {
                "name": f"{p.lname} {p.fname}",
                "num_trainings": len(p.trainings),
                "training_percentage": train_perc,
                "chart_color": color,
            }
        )
    players.sort(key=lambda p: p["name"])
    return render_template("players.html", players=players)


def calculate_training_percentage(players_num: int, all_training_num: int) -> int:
    return int(players_num / all_training_num * 100)


def determine_color(percentage: int) -> str:
    values = [(30, "is-danger"), (60, "is-warning"), (90, "is-success")]
    for perc, color in values:
        if percentage < perc:
            return color
    return "is-link"
