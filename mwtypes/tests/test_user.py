import pickle

from ..user import User


def test_user():
    # No info
    u = User()
    assert u.id == None
    assert u.text == None

    # Logged-in
    u = User(10, "Foobar")
    assert u.id == 10
    assert u.text == "Foobar"

    # IP
    u = User(text="192.168.0.1")
    assert u.id == None
    assert u.text == "192.168.0.1"

    # JSON and Pickle
    assert u == User(u.to_json())
    assert u == pickle.loads(pickle.dumps(u))
