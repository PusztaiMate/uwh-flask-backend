import os

from flask import Flask
from flask_restplus import Api, Resource


app = Flask(__name__)
api = Api(app)

app_settings = os.getenv("APP_SETTINGS")
app.config.from_object(app_settings)


@api.route("/ping")
class Ping(Resource):
    def get(self):
        return {"status": "success", "message": "pong"}
