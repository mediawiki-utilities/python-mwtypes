import pickle

from nose.tools import eq_

from ..page import Page
from ..revision import Deleted, Revision
from ..timestamp import Timestamp
from ..user import User


def test_revision():
    # No info
    r = Revision(10, Timestamp("20150101000000"))
    eq_(r.id, 10)
    eq_(r.timestamp, Timestamp("20150101000000"))
    eq_(r.user, None)
    eq_(r.page, None)
    eq_(r.minor, None)
    eq_(r.comment, None)
    eq_(r.text, None)
    eq_(r.bytes, None)
    eq_(r.sha1, None)
    eq_(r.parent_id, None)
    eq_(r.model, None)
    eq_(r.format, None)
    eq_(r.deleted, None)

    # All info
    r = Revision(10, Timestamp("20150101000000"),
                 user=User(10, "Foobar"),
                 page=Page(12, "Anarchism", 2),
                 minor=False,
                 comment="I have a lovely bunch of ...",
                 text="I am the text",
                 bytes=257,
                 sha1="fe5f4fe65fe765ef",
                 parent_id=9,
                 model="text",
                 format="also_text",
                 deleted=Deleted(text=True, comment=False, user=False,
                                 restricted=False))
    eq_(r.id, 10)
    eq_(r.timestamp, Timestamp("20150101000000"))
    eq_(r.user.id, 10)
    eq_(r.user.text, "Foobar")
    eq_(r.page.id, 12)
    eq_(r.page.title, "Anarchism")
    eq_(r.page.namespace, 2)
    eq_(r.minor, False)
    eq_(r.comment, "I have a lovely bunch of ...")
    eq_(r.text, "I am the text")
    eq_(r.bytes, 257)
    eq_(r.sha1, "fe5f4fe65fe765ef")
    eq_(r.parent_id, 9)
    eq_(r.model, "text")
    eq_(r.format, "also_text")
    eq_(r.deleted.text, True)
    eq_(r.deleted.comment, False)
    eq_(r.deleted.user, False)
    eq_(r.deleted.restricted, False)

    # JSON and Pickle
    eq_(r, Revision(r.to_json()))
    eq_(r, pickle.loads(pickle.dumps(r)))



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
