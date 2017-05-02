import pickle

from nose.tools import eq_

from ..user import User


def test_user():
    # No info
    u = User()
    eq_(u.id, None)
    eq_(u.text, None)

    # Logged-in
    u = User(10, "Foobar")
    eq_(u.id, 10)
    eq_(u.text, "Foobar")

    # IP
    u = User(text="192.168.0.1")
    eq_(u.id, None)
    eq_(u.text, "192.168.0.1")

    # JSON and Pickle
    eq_(u, User(u.to_json()))
    eq_(u, pickle.loads(pickle.dumps(u)))
