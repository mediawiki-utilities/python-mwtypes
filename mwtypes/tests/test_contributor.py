import pickle

from nose.tools import eq_

from ..contributor import Contributor


def test_contributor():
    # No info
    c = Contributor()
    eq_(c.id, None)
    eq_(c.user_text, None)

    # Logged-in
    c = Contributor(10, "Foobar")
    eq_(c.id, 10)
    eq_(c.user_text, "Foobar")

    # IP
    c = Contributor(user_text="192.168.0.1")
    eq_(c.id, None)
    eq_(c.user_text, "192.168.0.1")

    # JSON and Pickle
    eq_(c, Contributor(c.to_json()))
    eq_(c, pickle.loads(pickle.dumps(c)))
