import pytest

from project import db, create_app
from project.api.models import Player, Training, Club


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config.from_object("project.config.TestingConfig")
    with app.app_context():
        yield app


@pytest.fixture(scope="module")
def test_database():
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()


@pytest.fixture(scope="function")
def test_db_for_clubs():
    db.create_all()
    p1, p2, p3 = (
        add_player_if_not_present("Jakab Gipsz"),
        add_player_if_not_present("Jozsef Gipsz"),
        add_player_if_not_present("Janos Gipsz"),
    )
    add_training(players=[p1, p2, p3])
    add_training(players=[p2, p3])
    yield db
    db.session.remove()
    db.drop_all()


@pytest.fixture(scope="module")
def test_db_for_trainings():
    db.create_all()
    p1, p2, p3 = (
        add_player_if_not_present("Jakab Gipsz"),
        add_player_if_not_present("Jozsef Gipsz"),
        add_player_if_not_present("Janos Gipsz"),
    )
    add_club_if_not_present("Egyszusz VSE", players=[p1, p2, p3])
    yield db
    db.session.remove()
    db.drop_all()


def add_player(name: str) -> Player:
    fname, lname = name.split(" ")
    p = Player(fname=fname, lname=lname, email=f"{fname.lower()}@{lname.lower()}.hu")
    db.session.add(p)
    db.session.commit()
    return p


def add_player_if_not_present(name: str) -> Player:
    fname, lname = name.split(" ")
    email = f"{fname.lower()}@{lname.lower()}.hu"
    p = Player.query.filter_by(email=email).first()
    if not p:
        p = Player(fname=fname, lname=lname, email=email)
        db.session.add(p)
        db.session.commit()
    return p


def add_training(players: list = None) -> Training:
    player_ids = [p.id for p in players] if players else []
    t = Training(player_ids=player_ids)
    db.session.add(t)
    db.session.commit()
    return t


def add_club(name: str, players: list = None) -> Club:
    players = players or []
    c = Club(name=name, player_ids=[p.id for p in players], training_ids=None)
    db.session.add(c)
    db.session.commit()
    return c


def add_club_if_not_present(name: str, players: list = None) -> Club:
    players = players or []
    c = Club.query.filter_by(name=name).first()
    if not c:
        c = Club(name=name, player_ids=[p.id for p in players], training_ids=None)
        db.session.add(c)
        db.session.commit()
    return c
