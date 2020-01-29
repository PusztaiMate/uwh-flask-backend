import json
from typing import List

import pytest

from project.api.models import Club, Player
from project.tests.db_utils import (add_club_if_not_present,
                                    add_player_if_not_present)


@pytest.mark.parametrize("players", [None, [1], [1, 2, 3]])
@pytest.mark.parametrize("trainings", [None, [1], [1, 2]])
@pytest.mark.parametrize(
    ["name", "status_code", "message"],
    [("Egyszusz VSE", 201, "Egyszusz VSE was added")],
)
def test_add_club(
    test_app, test_db_for_clubs, name, players, trainings, status_code, message
):
    client = test_app.test_client()
    resp = client.post(
        "/clubs",
        data=json.dumps({"name": name, "players": players, "trainings": trainings}),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())

    assert resp.status_code == status_code
    assert message in data["message"]


def test_all_clubs(test_app, empty_db):
    c1, (p1, p2) = add_club_with_players("Club GETALL_1", ["Jakab Gipsz", "Joe Gipsz"])
    c2, (p3,) = add_club_with_players("Club GETALL_2", ["Julia Gipsz"])
    client = test_app.test_client()

    resp = client.get("/clubs")
    data = json.loads(resp.data.decode())

    assert resp.status_code == 200
    assert len(data) == 2
    assert len(data[0]["players"]) == 2
    assert p3.fname in data[1]["players"][0]
    assert data[0]["name"] == c1.name
    assert data[1]["name"] == c2.name


def test_get_single_club(test_app, empty_db):
    c1, (p1, p2) = add_club_with_players("Club GETALL_1", ["Jakab Gipsz", "Joe Gipsz"])
    c2, (p3,) = add_club_with_players("Club GETALL_2", ["Julia Gipsz"])
    client = test_app.test_client()

    resp = client.get(f"/clubs/{c1.id}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert len(data["players"]) == 2
    assert data["name"] == c1.name

    resp = client.get(f"/clubs/{c2.id}")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert len(data["players"]) == 1
    assert data["name"] == c2.name


def add_club_with_players(club_name: str, players: List[str]) -> (Club, List[Player]):
    players = [add_player_if_not_present(name=name) for name in players]
    club = add_club_if_not_present(club_name, players=players)
    return club, players
