import pickle

from ..page import Page
from ..revision import Deleted, Revision
from ..slots import Content, Slots
from ..timestamp import Timestamp
from ..user import User


def test_revision():
    # No info
    r = Revision(10, Timestamp("20150101000000"))
    assert r.id == 10
    assert r.timestamp == Timestamp("20150101000000")
    assert r.user == None
    assert r.page == None
    assert r.minor == None
    assert r.comment == None
    assert r.text == None
    assert r.bytes == None
    assert r.sha1 == None
    assert r.parent_id == None
    assert r.model == None
    assert r.format == None
    assert r.deleted == None
    assert r.slots == None

    # All info
    r = Revision(10, Timestamp("20150101000000"),
                 user=User(10, "Foobar"),
                 page=Page(12, "Anarchism", 2),
                 minor=False,
                 comment="I have a lovely bunch of ...",
                 slots=Slots(
                    sha1="2345672bb",
                    contents={'main': Content(
                            text="I am the text",
                            bytes=257,
                            sha1="fe5f4fe65fe765ef",
                            model="text",
                            format="also_text",
                            deleted=True)}),
                 parent_id=9,
                 deleted=Deleted(text=True, comment=False, user=False,
                                 restricted=False))
    assert r.id == 10
    assert r.timestamp == Timestamp("20150101000000")
    assert r.user.id == 10
    assert r.user.text == "Foobar"
    assert r.page.id == 12
    assert r.page.title == "Anarchism"
    assert r.page.namespace == 2
    assert r.minor == False
    assert r.comment == "I have a lovely bunch of ..."
    assert r.text == "I am the text"
    assert r.slots['main'].text == "I am the text"
    assert r.bytes == 257
    assert r.slots['main'].bytes == 257
    assert r.sha1 == "fe5f4fe65fe765ef"
    assert r.slots.sha1 == "2345672bb"
    assert r.model == "text"
    assert r.slots['main'].model == "text"
    assert r.format == "also_text"
    assert r.slots['main'].format == "also_text"
    assert r.parent_id == 9
    assert r.deleted.text == True
    assert r.deleted.comment == False
    assert r.deleted.user == False
    assert r.deleted.restricted == False

    # JSON and Pickle
    assert r == Revision(r.to_json())
    assert r == pickle.loads(pickle.dumps(r))


def test_deleted():
    # No info
    d = Deleted()
    assert d.text == None
    assert d.comment == None
    assert d.user == None
    assert d.restricted == None

    # Just one
    d = Deleted(text=True)
    assert d.text == True
    assert d.comment == None
    assert d.user == None
    assert d.restricted == None

    # All
    d = Deleted(text=True, comment=False, user=True, restricted=False)
    assert d.text == True
    assert d.comment == False
    assert d.user == True
    assert d.restricted == False

    d = Deleted.from_int(0)
    assert d.text == False
    assert d.comment == False
    assert d.user == False
    assert d.restricted == False

    d = Deleted.from_int(3)
    assert d.text == True
    assert d.comment == True
    assert d.user == False
    assert d.restricted == False

    d = Deleted.from_int(9)
    assert d.text == True
    assert d.comment == False
    assert d.user == False
    assert d.restricted == True

    d = Deleted.from_int(15)
    assert d.text == True
    assert d.comment == True
    assert d.user == True
    assert d.restricted == True

    # JSON and Pickle
    assert d == Deleted(d.to_json())
    assert d == pickle.loads(pickle.dumps(d))


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
