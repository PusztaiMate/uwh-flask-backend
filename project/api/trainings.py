from flask import Blueprint, request
from flask_restplus import Api, Resource
from flask_restplus.fields import List, String, Integer

from project import db
from project.api.models import Training


trainings_blueprint = Blueprint("trainings", __name__)
api = Api(trainings_blueprint)


trainings = api.model(
    "Training",
    {
        "id": Integer(readonly=True),
        "date": String(required=False, default=None),
        "player_ids": List(Integer, required=False, default=[]),
        "club_id": Integer(required=False, default=None),
    },
)


@api.route("/trainings")
class TrainingsList(Resource):
    @api.expect(trainings, validate=True)
    def post(self):
        post_data = request.get_json()
        club_id, date, player_ids = (
            post_data.get("club_id"),
            post_data.get("date"),
            post_data.get("player_ids"),
        )
        response_object = {}

        t = Training(club_id=club_id, date=date, player_ids=player_ids)
        db.session.add(t)
        db.session.commit()

        response_object["message"] = f"{t} was added."
        return response_object, 201

    @api.marshal_with(trainings, as_list=True)
    def get(self):
        return Training.query.all(), 200
