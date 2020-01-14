import json
import pytest


@pytest.mark.parametrize(
    ["name", "players", "trainings", "status_code", "message"],
    [("Egyszusz VSE", [], [], 200, "Egyszusz VSE was added")],
)
def test_add_club(
    test_app, test_database, name, players, trainings, status_code, message
):
    client = test_app.test_client()
    resp = client.post(
        "/clubs",
        data=json.loads({"name": name, "players": players, "trainings": trainings}),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())

    assert resp.status_code == status_code
    assert message in data["message"]
