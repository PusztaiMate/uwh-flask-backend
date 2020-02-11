from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for

from project import db
from project.api.models import Training
from project.views.utils import get_all_players_sorted, sort_player_list_by_name


trainings_view = Blueprint("trainings", __name__, url_prefix="/trainings")


@trainings_view.route("/", methods=["get"])
def all_trainings():
    return render_template("trainings.html", trainings=Training.query.all())


@trainings_view.route("/add", methods=["get", "post"])
def add_training():
    players = get_all_players_sorted()
    present_pattern = "players-present"
    if request.method == "POST":
        players_present = request.values.getlist(present_pattern)
        current_date = datetime.today()
        db.session.add(
            Training(club_id=1, date=current_date, player_ids=players_present)
        )
        db.session.commit()
        return redirect(url_for("trainings.all_trainings"))
    return render_template(
        "add_training.html", present_pattern=present_pattern, players=players
    )


@trainings_view.route("/<int:training_id>")
def get_single_training(training_id: int):
    training = Training.query.filter_by(id=training_id).first()
    if not training:
        return render_template("404.html"), 404
    players = sort_player_list_by_name(training.players)
    return render_template("single_training.html", players=players, training=training)
