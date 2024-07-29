import os.path

from ..p7z import reader


def test_open_file():
    f = reader(os.path.join(os.path.dirname(__file__), "foo.7z"))
    assert f.read() == "foo\n"
