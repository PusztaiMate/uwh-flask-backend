import pytest

from project import create_app, db
from project.tests.db_utils import (
    add_club_if_not_present,
    add_player_if_not_present,
    add_training,
)


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


@pytest.fixture(scope="function")
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


@pytest.fixture(scope="function")
def empty_db():
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()
