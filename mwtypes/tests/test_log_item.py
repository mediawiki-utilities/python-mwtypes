import pickle

from nose.tools import eq_

from ..log_item import Deleted, LogItem, Page
from ..timestamp import Timestamp
from ..user import User


def test_log_item():
    # No info
    l = LogItem(10, Timestamp("20150101000000"))
    eq_(l.id, 10)
    eq_(l.timestamp, Timestamp("20150101000000"))
    eq_(l.comment, None)
    eq_(l.user, None)
    eq_(l.page, None)
    eq_(l.type, None)
    eq_(l.action, None)
    eq_(l.text, None)
    eq_(l.params, None)
    eq_(l.deleted, None)

    # All info
    l = LogItem(10, Timestamp("20150101000000"),
                comment="I have a lovely bunch of ...",
                user=User(10, "Foobar"),
                page=Page(0, "Anarchism"),
                type="foo",
                action="bar",
                text="I am the text",
                params="I am the params",
                deleted=Deleted(action=True, comment=False, user=False,
                                restricted=False))
    eq_(l.id, 10)
    eq_(l.timestamp, Timestamp("20150101000000"))
    eq_(l.comment, "I have a lovely bunch of ...")
    eq_(l.user.id, 10)
    eq_(l.user.text, "Foobar")
    eq_(l.page.namespace, 0)
    eq_(l.page.title, "Anarchism")
    eq_(l.type, "foo")
    eq_(l.action, "bar")
    eq_(l.text, "I am the text")
    eq_(l.params, "I am the params")
    eq_(l.deleted.action, True)
    eq_(l.deleted.comment, False)
    eq_(l.deleted.user, False)
    eq_(l.deleted.restricted, False)

    # JSON and Pickle
    eq_(l, LogItem(l.to_json()))
    eq_(l, pickle.loads(pickle.dumps(l)))


def test_deleted():
    # No info
    d = Deleted()
    eq_(d.action, None)
    eq_(d.comment, None)
    eq_(d.user, None)
    eq_(d.restricted, None)

    # Just one
    d = Deleted(action=True)
    eq_(d.action, True)
    eq_(d.comment, None)
    eq_(d.user, None)
    eq_(d.restricted, None)

    # All
    d = Deleted(action=True, comment=False, user=True, restricted=False)
    eq_(d.action, True)
    eq_(d.comment, False)
    eq_(d.user, True)
    eq_(d.restricted, False)

    d = Deleted.from_int(0)
    eq_(d.action, False)
    eq_(d.comment, False)
    eq_(d.user, False)
    eq_(d.restricted, False)

    d = Deleted.from_int(3)
    eq_(d.action, True)
    eq_(d.comment, True)
    eq_(d.user, False)
    eq_(d.restricted, False)

    d = Deleted.from_int(9)
    eq_(d.action, True)
    eq_(d.comment, False)
    eq_(d.user, False)
    eq_(d.restricted, True)

    d = Deleted.from_int(15)
    eq_(d.action, True)
    eq_(d.comment, True)
    eq_(d.user, True)
    eq_(d.restricted, True)

    # JSON and Pickle
    eq_(d, Deleted(d.to_json()))
    eq_(d, pickle.loads(pickle.dumps(d)))
