from flask import Blueprint, render_template


from project.api.models import Training


trainings_view = Blueprint("trainings", __name__, url_prefix="/trainings")


@trainings_view.route("/", methods=["get"])
def all_trainings():
    return render_template("trainings.html", trainings=Training.query.all())
