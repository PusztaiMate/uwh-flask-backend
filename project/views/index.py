from flask import Blueprint, render_template


index_blueprint = Blueprint("index", __name__)


@index_blueprint.route("/", methods=["GET"])
@index_blueprint.route("/home", methods=["GET"])
def index():
    return render_template("index.html")
