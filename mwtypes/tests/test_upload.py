import pickle

from nose.tools import eq_

from ..timestamp import Timestamp
from ..upload import Upload
from ..user import User


def test_upload():
    # No info
    u = Upload(Timestamp("20150101000000"))
    eq_(u.timestamp, Timestamp("20150101000000"))
    eq_(u.user, None)
    eq_(u.comment, None)
    eq_(u.filename, None)
    eq_(u.source, None)
    eq_(u.size, None)

    # All info
    u = Upload(Timestamp("20150101000000"),
               user=User(10, "Foobar"),
               comment="I have a lovely bunch of ...",
               filename="Foo_bar.jpg",
               source="https://foo",
               size=345678)
    eq_(u.timestamp, Timestamp("20150101000000"))
    eq_(u.comment, "I have a lovely bunch of ...")
    eq_(u.user.id, 10)
    eq_(u.user.text, "Foobar")
    eq_(u.filename, "Foo_bar.jpg")
    eq_(u.source, "https://foo")
    eq_(u.size, 345678)

    # JSON and Pickle
    eq_(u, Upload(u.to_json()))
    eq_(u, pickle.loads(pickle.dumps(u)))
