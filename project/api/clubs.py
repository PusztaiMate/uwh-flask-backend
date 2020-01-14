from flask import Blueprint, request
from flask_restplus import Api, Resource
from flask_restplus.fields import List, String, Integer

from project import db
from project.api.models import Club


clubs_blueprint = Blueprint("clubs", __name__)
api = Api(clubs_blueprint)


clubs = api.model(
    "Club",
    {
        "id": Integer(readonly=True),
        "name": String(required=True),
        "player_ids": List(Integer, default=[]),
        "training_ids": List(Integer, default=[]),
    },
)


@api.route("/clubs")
class ClubsList(Resource):
    @api.expect(clubs, validate=True)
    def post(self):
        post_data = request.get_json()
        name, players, trainings = (
            post_data.get("name"),
            post_data.get("player_ids"),
            post_data.get("training_ids"),
        )
        response_object = {}

        db.session.add(Club(name=name, player_ids=players, training_ids=trainings))
        db.session.commit()

        response_object["message"] = f"{name} was added."
        return response_object, 201
