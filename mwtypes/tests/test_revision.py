import pickle

from nose.tools import eq_

from ..contributor import Contributor
from ..deleted import Deleted
from ..revision import Revision
from ..timestamp import Timestamp


def test_revision():
    # No info
    r = Revision(10, Timestamp("20150101000000"))
    eq_(r.id, 10)
    eq_(r.timestamp, Timestamp("20150101000000"))
    eq_(r.contributor, Contributor())
    eq_(r.minor, None)
    eq_(r.comment, None)
    eq_(r.text, None)
    eq_(r.bytes, None)
    eq_(r.sha1, None)
    eq_(r.parent_id, None)
    eq_(r.model, None)
    eq_(r.format, None)
    eq_(r.deleted, Deleted())

    # All info
    r = Revision(10, Timestamp("20150101000000"),
                 contributor=Contributor(10, "Foobar"),
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
    eq_(r.contributor, Contributor(10, "Foobar"))
    eq_(r.minor, False)
    eq_(r.comment, "I have a lovely bunch of ...")
    eq_(r.text, "I am the text")
    eq_(r.bytes, 257)
    eq_(r.sha1, "fe5f4fe65fe765ef")
    eq_(r.parent_id, 9)
    eq_(r.model, "text")
    eq_(r.format, "also_text")
    eq_(r.deleted, Deleted(text=True, comment=False, user=False,
                   restricted=False))

    # JSON and Pickle
    eq_(r, Revision(r.to_json()))
    eq_(r, pickle.loads(pickle.dumps(r)))
