from datetime import timedelta
import pytest
from utils.security import hash_password, verify_password, create_access_token


@pytest.fixture
def passwords():
    return {
        "valid": "secure_password",
        "invalid": "wrong_password",
        "empty": "",
        "long": "a" * 100,
    }


@pytest.fixture
def hashed_passwords(passwords):
    return {key: hash_password(value) for key, value in passwords.items()}


def test_hash_password(passwords, hashed_passwords):
    for key, password in passwords.items():
        hashed = hashed_passwords[key]
        assert hashed != password
        assert isinstance(hashed, str)


@pytest.mark.parametrize(
    "password_key, expected",
    [
        ("valid", True),
        ("invalid", False),
        ("empty", False),
        ("long", False),
    ],
)
def test_verify_password(password_key, expected, passwords, hashed_passwords):
    assert (
        verify_password(passwords[password_key], hashed_passwords["valid"]) == expected
    )


def test_create_access_token():
    token1 = create_access_token({"user_id": 1, "username": "danial", "role": "admin"})
    assert isinstance(token1, str)
    assert token1.count(".") == 2
    token1 = create_access_token(
        {"user_id": 1, "username": "danial", "role": "admin"}, timedelta(minutes=30)
    )
    assert isinstance(token1, str)
    assert token1.count(".") == 2
