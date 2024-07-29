import pickle

from ..log_item import Deleted, LogItem, Page
from ..timestamp import Timestamp
from ..user import User


def test_log_item():
    # No info
    l = LogItem(10, Timestamp("20150101000000"))
    assert l.id == 10
    assert l.timestamp == Timestamp("20150101000000")
    assert l.comment == None
    assert l.user == None
    assert l.page == None
    assert l.type == None
    assert l.action == None
    assert l.text == None
    assert l.params == None
    assert l.deleted == None

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
    assert l.id == 10
    assert l.timestamp == Timestamp("20150101000000")
    assert l.comment == "I have a lovely bunch of ..."
    assert l.user.id == 10
    assert l.user.text == "Foobar"
    assert l.page.namespace == 0
    assert l.page.title == "Anarchism"
    assert l.type == "foo"
    assert l.action == "bar"
    assert l.text == "I am the text"
    assert l.params == "I am the params"
    assert l.deleted.action == True
    assert l.deleted.comment == False
    assert l.deleted.user == False
    assert l.deleted.restricted == False

    # JSON and Pickle
    assert l == LogItem(l.to_json())
    assert l == pickle.loads(pickle.dumps(l))


def test_deleted():
    # No info
    d = Deleted()
    assert d.action == None
    assert d.comment == None
    assert d.user == None
    assert d.restricted == None

    # Just one
    d = Deleted(action=True)
    assert d.action == True
    assert d.comment == None
    assert d.user == None
    assert d.restricted == None

    # All
    d = Deleted(action=True, comment=False, user=True, restricted=False)
    assert d.action == True
    assert d.comment == False
    assert d.user == True
    assert d.restricted == False

    d = Deleted.from_int(0)
    assert d.action == False
    assert d.comment == False
    assert d.user == False
    assert d.restricted == False

    d = Deleted.from_int(3)
    assert d.action == True
    assert d.comment == True
    assert d.user == False
    assert d.restricted == False

    d = Deleted.from_int(9)
    assert d.action == True
    assert d.comment == False
    assert d.user == False
    assert d.restricted == True

    d = Deleted.from_int(15)
    assert d.action == True
    assert d.comment == True
    assert d.user == True
    assert d.restricted == True

    # JSON and Pickle
    assert d == Deleted(d.to_json())
    assert d == pickle.loads(pickle.dumps(d))
