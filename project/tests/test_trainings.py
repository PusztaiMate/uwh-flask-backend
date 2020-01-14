import json
import pytest


@pytest.mark.parametrize("date", ["2020-01-01T19:30"])
@pytest.mark.parametrize("player_ids", [[], [1], [1, 2, 3]])
@pytest.mark.parametrize(
    ["club_id", "status_code", "message"],
    [(1, 201, "Training(2020-01-01T19:30:00) was added",),],
)
def test_add_training(
    test_app, test_db_for_trainings, club_id, date, player_ids, status_code, message
):
    client = test_app.test_client()
    resp = client.post(
        "/trainings",
        data=json.dumps({"club_id": club_id, "date": date, "player_ids": player_ids}),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())

    assert resp.status_code == status_code
    assert message in data["message"]
