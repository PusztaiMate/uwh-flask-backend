from datetime import datetime
from dateutil import parser
from project import db


players_to_trainings = db.Table(
    "players_to_trainings",
    db.Column("player_id", db.Integer, db.ForeignKey("players.id")),
    db.Column("training_id", db.Integer, db.ForeignKey("trainings.id")),
)


class Player(db.Model):
    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(64), nullable=False)
    lname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    club_id = db.Column(db.Integer, db.ForeignKey("clubs.id"))
    trainings = db.relationship(
        "Training",
        secondary=players_to_trainings,
        backref=db.backref("players", lazy="dynamic"),
    )

    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def __repr__(self):
        return (
            f"Player(fname={self.fname!r}, lname={self.lname!r}, email={self.email!r})"
        )


class Training(db.Model):
    __tablename__ = "trainings"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime())
    club_id = db.Column(db.Integer, db.ForeignKey("clubs.id"))

    def __init__(self, club_id=None, date=None, players=None):
        self.club_id = club_id
        self.players = players or []
        if isinstance(date, str):
            self.date = parser.parse(date)
        elif isinstance(date, datetime.datetime):
            self.date = date
        else:
            self.date = datetime.datetime.now()

    def __repr__(self):
        return f"Training(club_id={self.club_id!r}, date={self.date!r}, players={self.players!r})"


class Club(db.Model):
    __tablename__ = "clubs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    players = db.relationship("Player", backref="club")
    trainings = db.relationship("Training", backref="club")

    def __init__(self, name, players=None, trainings=None):
        self.name = name
        self.players = players or []
        self.trainings = trainings or []

    def __repr__(self):
        return f"Club(name={self.name!r}, players={self.players!r}, trainings={self.trainings!r})"
