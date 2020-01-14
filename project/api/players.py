from flask import Blueprint, request
from flask_restplus import Api, Resource
from flask_restplus.fields import String, Integer

from project import db
from project.api.models import Player


players_blueprint = Blueprint("players", __name__)
api = Api(players_blueprint)


player = api.model(
    "Player",
    {
        "id": Integer(readonly=True),
        "fname": String(required=True),
        "lname": String(required=True),
        "email": String(required=True),
    },
)


@api.route("/players")
class PlayersList(Resource):
    @api.expect(player, validate=True)
    def post(self):
        post_data = request.get_json()
        fname, lname, email = (
            post_data.get("fname"),
            post_data.get("lname"),
            post_data.get("email"),
        )
        response_object = {}

        if Player.query.filter_by(email=email).first():
            response_object["message"] = f"{email} already exists."
            return response_object, 400

        db.session.add(Player(fname=fname, lname=lname, email=email))
        db.session.commit()
        response_object["message"] = f"{fname} {lname} was added!"
        return response_object, 201
