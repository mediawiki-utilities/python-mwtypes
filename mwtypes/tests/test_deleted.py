import pickle

from nose.tools import eq_

from ..deleted import Deleted


def test_deleted():
    # No info
    d = Deleted()
    eq_(d.text, None)
    eq_(d.comment, None)
    eq_(d.user, None)
    eq_(d.restricted, None)

    # Just one
    d = Deleted(text=True)
    eq_(d.text, True)
    eq_(d.comment, None)
    eq_(d.user, None)
    eq_(d.restricted, None)

    # All
    d = Deleted(text=True, comment=False, user=True, restricted=False)
    eq_(d.text, True)
    eq_(d.comment, False)
    eq_(d.user, True)
    eq_(d.restricted, False)

    d = Deleted.from_int(0)
    eq_(d.text, False)
    eq_(d.comment, False)
    eq_(d.user, False)
    eq_(d.restricted, False)

    d = Deleted.from_int(3)
    eq_(d.text, True)
    eq_(d.comment, True)
    eq_(d.user, False)
    eq_(d.restricted, False)

    d = Deleted.from_int(9)
    eq_(d.text, True)
    eq_(d.comment, False)
    eq_(d.user, False)
    eq_(d.restricted, True)

    d = Deleted.from_int(15)
    eq_(d.text, True)
    eq_(d.comment, True)
    eq_(d.user, True)
    eq_(d.restricted, True)

    # JSON and Pickle
    eq_(d, Deleted(d.to_json()))
    eq_(d, pickle.loads(pickle.dumps(d)))
