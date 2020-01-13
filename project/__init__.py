from flask import Flask
from flask_restplus import Api, Resource


app = Flask(__name__)
api = Api(app)

app.config.from_object("project.config.DevelopmentConfig")


@api.route("/ping")
class Ping(Resource):
    def get(self):
        return {"status": "success", "message": "pong"}
