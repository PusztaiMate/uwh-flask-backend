import json

import pytest

from project.tests.db_utils import add_player_if_not_present


@pytest.mark.parametrize(
    ["fname", "lname", "email", "status_code", "message"],
    [
        ["Jakab", "Gipsz", "jakab@gipsz.hu", 201, "Jakab Gipsz was added!"],
        ["Jakab", "Gipsz", "jakab@gipsz.hu", 400, "jakab@gipsz.hu already exists."],
        ["Janos", None, "janos@gipsz.hu", 400, "Input payload validation failed"],
        [None, "Gipsz", "janos@gipsz.hu", 400, "Input payload validation failed"],
        ["Janos", "Gipsz", None, 400, "Input payload validation failed"],
    ],
)
def test_add_player(test_app, test_database, fname, lname, email, status_code, message):
    client = test_app.test_client()
    resp = client.post(
        "/api/players",
        data=json.dumps({"fname": fname, "lname": lname, "email": email}),
        content_type="application/json",
    )

    data = json.loads(resp.data.decode())

    assert resp.status_code == status_code
    assert message in data["message"]


def test_get_single_player(test_app, test_database):
    player = add_player_if_not_present("Jakab Gipsz")
    client = test_app.test_client()
    resp = client.get(f"/api/players/{player.id}")

    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert data["fname"] == "Jakab"
    assert data["lname"] == "Gipsz"


def test_get_all_players(test_app, test_database):
    p1 = add_player_if_not_present("Jakab Gipsz")
    p2 = add_player_if_not_present("János Gipsz")
    client = test_app.test_client()

    resp = client.get("/api/players")
    data = json.loads(resp.data.decode())

    assert resp.status_code == 200
    assert len(data) == 2
    assert data[0]["fname"] == p1.fname
    assert data[1]["lname"] == p2.lname
