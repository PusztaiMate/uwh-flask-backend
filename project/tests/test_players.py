import json

import pytest


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
def test_add_user(test_app, test_database, fname, lname, email, status_code, message):
    client = test_app.test_client()
    resp = client.post(
        "/players",
        data=json.dumps({"fname": fname, "lname": lname, "email": email}),
        content_type="application/json",
    )

    data = json.loads(resp.data.decode())

    assert resp.status_code == status_code
    assert message in data["message"]
