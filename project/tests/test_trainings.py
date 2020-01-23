import json
import pytest

from project.tests.db_utils import add_training


@pytest.mark.parametrize("date", [None, "2020-01-01T19:30"])
@pytest.mark.parametrize("player_ids", [None, [], [1], [1, 2, 3]])
@pytest.mark.parametrize(
    ["club_id", "status_code", "message"], [(1, 201, ") was added",),],
)
def test_add_training(
    test_app, test_db_for_trainings, club_id, date, player_ids, status_code, message
):
    client = test_app.test_client()

    payload = {"club_id": club_id}
    if player_ids is not None:
        payload["player_ids"] = player_ids
    if date is not None:
        payload["date"] = date

    resp = client.post(
        "/trainings", data=json.dumps(payload), content_type="application/json",
    )
    data = json.loads(resp.data.decode())

    assert resp.status_code == status_code
    assert message in data["message"]


def test_all_trainings(test_app, test_database):
    t1 = add_training()
    t2 = add_training()
    client = test_app.test_client()

    resp = client.get("/trainings")
    data = json.loads(resp.data.decode())

    assert resp.status_code == 200
    assert len(data) == 2
    assert t1.club_id == data[0]["club_id"]
