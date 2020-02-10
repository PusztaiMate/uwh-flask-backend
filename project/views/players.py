from flask import Blueprint, render_template, redirect, url_for

from project import db
from project.api.models import Player, Training
from project.views.forms import RegisterPlayerForm


players_view = Blueprint("players", __name__, url_prefix="/players")


@players_view.route("/", methods=["get"])
def all_players():
    players = prepare_players_dataobject()
    return render_template("players.html", players=players)


@players_view.route("/<int:player_id>")
def get_single_player(player_id: int):
    player = Player.query.filter_by(id=player_id).first()
    if not player_id:
        return render_template("404.html"), 404
    training_percentage = int(player.get_training_percentage())
    return render_template(
        "single_player.html", player=player, training_percentage=training_percentage
    )


@players_view.route("/add", methods=["POST", "GET"])
def add_player():
    form = RegisterPlayerForm()
    if form.validate_on_submit():
        player = Player(fname=form.fname.data, lname=form.lname.data, email=None)
        db.session.add(player)
        db.session.commit()
        return redirect(url_for("players.get_single_player", player_id=player.id))
    return render_template("add_player.html", form=form)


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
