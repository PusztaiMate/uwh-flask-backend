import json
import pytest


@pytest.mark.parametrize("players", [None, [1], [1, 2, 3]])
@pytest.mark.parametrize("trainings", [None, [1], [1, 2]])
@pytest.mark.parametrize(
    ["name", "status_code", "message"],
    [("Egyszusz VSE", 201, "Egyszusz VSE was added"),],
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


@pytest.mark.parametrize("players", [None, [1, 2, 3]])
@pytest.mark.parametrize("trainings", [None, [1]])
@pytest.mark.parametrize(
    ["name", "status_code", "message"],
    [(None, 400, "Input payload validation failed")],
)
def test_add_club_bad_input(
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
