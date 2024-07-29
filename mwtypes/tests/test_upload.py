import pickle

from ..timestamp import Timestamp
from ..upload import Upload
from ..user import User


def test_upload():
    # No info
    u = Upload(Timestamp("20150101000000"))
    assert u.timestamp == Timestamp("20150101000000")
    assert u.user == None
    assert u.comment == None
    assert u.filename == None
    assert u.source == None
    assert u.size == None

    # All info
    u = Upload(Timestamp("20150101000000"),
               user=User(10, "Foobar"),
               comment="I have a lovely bunch of ...",
               filename="Foo_bar.jpg",
               source="https://foo",
               size=345678)
    assert u.timestamp == Timestamp("20150101000000")
    assert u.comment == "I have a lovely bunch of ..."
    assert u.user.id == 10
    assert u.user.text == "Foobar"
    assert u.filename == "Foo_bar.jpg"
    assert u.source == "https://foo"
    assert u.size == 345678

    # JSON and Pickle
    assert u == Upload(u.to_json())
    assert u == pickle.loads(pickle.dumps(u))
