from flask import Blueprint, render_template

from project.api.models import Player, Training


players_view = Blueprint("players", __name__, url_prefix="/players")


@players_view.route("/", methods=["get"])
def all_players():
    players = prepare_players_dataobject()
    return render_template("players.html", players=players)


def prepare_players_dataobject() -> list:
    all_players = Player.query.all()
    num_of_trainings = len(Training.query.all())
    players = []
    for player in all_players:
        train_perc = calc_training_perc(len(player.trainings), num_of_trainings)
        color = determine_color(train_perc)
        players.append(
            {
                "name": f"{player.lname} {player.fname}",
                "num_trainings": len(player.trainings),
                "training_percentage": train_perc,
                # color shouldn't be determined in backend, but...
                "chart_color": color,
            }
        )
    players.sort(key=lambda p: p["name"])
    return players


def calc_training_perc(players_num: int, all_training_num: int) -> int:
    return int(players_num / all_training_num * 100)


# This really doesn't belong here, please learn javascript :'(
def determine_color(percentage: int) -> str:
    values = [(30, "is-danger"), (60, "is-warning"), (90, "is-success")]
    for perc, color in values:
        if percentage < perc:
            return color
    return "is-link"
