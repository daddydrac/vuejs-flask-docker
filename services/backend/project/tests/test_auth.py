# services/users/project/tests/test_auth.py


import json

import pytest
from flask import current_app


def test_user_registration(test_app, test_database, add_user):
    client = test_app.test_client()
    resp = client.post(
        "/auth/register",
        data=json.dumps(
            {"username": "justatest", "email": "test@test.com", "password": "123456"}
        ),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert resp.content_type == "application/json"
    assert "justatest" in data["username"]
    assert "test@test.com" in data["email"]
    assert "password" not in data


def test_user_registration_duplicate_email(test_app, test_database, add_user):
    add_user("test", "test@test.com", "test")
    client = test_app.test_client()
    resp = client.post(
        "/auth/register",
        data=json.dumps(
            {"username": "joehoeller", "email": "test@test.com", "password": "test"}
        ),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert resp.content_type == "application/json"
    assert "Sorry. That email already exists." in data["message"]


@pytest.mark.parametrize(
    "payload",
    [
        [{}],
        [{"email": "me@ml-app-name.com", "password": "greaterthanten"}],
        [{"username": "joehoeller", "password": "greaterthanten"}],
        [{"email": "me@ml-app-name.com", "username": "joehoeller"}],
    ],
)
def test_user_registration_invalid_json(test_app, test_database, payload):
    client = test_app.test_client()
    resp = client.post(
        f"/auth/register", data=json.dumps(payload), content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert resp.content_type == "application/json"
    assert "Input payload validation failed" in data["message"]


def test_registered_user_login(test_app, test_database, add_user):
    add_user("test3", "test3@test.com", "test")
    client = test_app.test_client()
    resp = client.post(
        "/auth/login",
        data=json.dumps({"email": "test3@test.com", "password": "test"}),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert resp.content_type == "application/json"
    assert data["access_token"]
    assert data["refresh_token"]


def test_not_registered_user_login(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        "/auth/login",
        data=json.dumps({"email": "testnotreal@test.com", "password": "test"}),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404
    assert resp.content_type == "application/json"
    assert "User does not exist." in data["message"]


def test_valid_refresh(test_app, test_database, add_user):
    add_user("test4", "test4@test.com", "test")
    client = test_app.test_client()
    # user login
    resp_login = client.post(
        "/auth/login",
        data=json.dumps({"email": "test4@test.com", "password": "test"}),
        content_type="application/json",
    )
    # valid refresh
    data = json.loads(resp_login.data.decode())
    refresh_token = json.loads(resp_login.data.decode())["refresh_token"]
    resp = client.post(
        "/auth/refresh",
        data=json.dumps({"refresh_token": refresh_token}),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert resp.content_type == "application/json"
    assert data["access_token"]
    assert data["refresh_token"]


def test_invalid_refresh_expired_token(test_app, test_database, add_user):
    add_user("test5", "test5@test.com", "test")
    current_app.config["REFRESH_TOKEN_EXPIRATION"] = -1
    client = test_app.test_client()
    # user login
    resp_login = client.post(
        "/auth/login",
        data=json.dumps({"email": "test5@test.com", "password": "test"}),
        content_type="application/json",
    )
    # invalid token refresh
    refresh_token = json.loads(resp_login.data.decode())["refresh_token"]
    resp = client.post(
        "/auth/refresh",
        data=json.dumps({"refresh_token": refresh_token}),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 401
    assert resp.content_type == "application/json"
    assert "Signature expired. Please log in again." in data["message"]


def test_invalid_refresh(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        "/auth/refresh",
        data=json.dumps({"refresh_token": "Invalid"}),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 401
    assert resp.content_type == "application/json"
    assert "Invalid token. Please log in again." in data["message"]


def test_user_status(test_app, test_database, add_user):
    add_user("test6", "test6@test.com", "test")
    client = test_app.test_client()
    resp_login = client.post(
        "/auth/login",
        data=json.dumps({"email": "test6@test.com", "password": "test"}),
        content_type="application/json",
    )
    token = json.loads(resp_login.data.decode())["access_token"]
    resp = client.get(
        "/auth/status",
        headers={"Authorization": f"Bearer {token}"},
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 200
    assert resp.content_type == "application/json"
    assert "test6" in data["username"]
    assert "test6@test.com" in data["email"]
    assert "password" not in data


def test_invalid_status(test_app, test_database):
    client = test_app.test_client()
    resp = client.get(
        "/auth/status",
        headers={"Authorization": "Bearer invalid"},
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 401
    assert resp.content_type == "application/json"
    assert "Invalid token. Please log in again." in data["message"]
