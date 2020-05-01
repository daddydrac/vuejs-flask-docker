# services/users/project/tests/test_ping.py


import json


def test_ping(test_app):
    client = test_app.test_client()
    resp = client.get("/ping")
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert "pong" in data["message"]
    assert "success" in data["status"]
