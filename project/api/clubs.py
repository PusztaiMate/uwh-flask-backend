from flask import Blueprint, request
from flask_restplus import Api, Resource
from flask_restplus.fields import List, String, Integer

from project import db
from project.api.models import Club


clubs_blueprint = Blueprint("clubs", __name__)
api = Api(clubs_blueprint)


clubs_out = api.model(
    "Club",
    {
        "id": Integer(readonly=True),
        "name": String(required=True),
        "players": List(String, default=[]),
        "trainings": List(String, default=[]),
    },
)

clubs_in = api.model(
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
    @api.expect(clubs_in, validate=True)
    def post(self):
        post_data = request.get_json()
        name, player_ids, trainings_ids = (
            post_data.get("name"),
            post_data.get("player_ids"),
            post_data.get("training_ids"),
        )
        response_object = {}

        db.session.add(Club(name=name, player_ids=player_ids, training_ids=trainings_ids))
        db.session.commit()

        response_object["message"] = f"{name} was added."
        return response_object, 201

    @api.marshal_with(clubs_out, as_list=True)
    def get(self):
        return Club.query.all(), 200