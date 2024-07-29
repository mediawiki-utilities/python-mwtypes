import io
import os

from pytest import raises

from ..functions import concat, extract_extension, normalize_path, reader


def test_concat():
    start = "Foobar1"
    f = io.StringIO("Foobar2")
    end = "Foobar3"

    assert concat(start, f, end).read() == "Foobar1Foobar2Foobar3"


def test_extract_extension():
    assert extract_extension("foo")[1] == None
    assert extract_extension("foo.xml")[1] == "xml"
    assert extract_extension("foo.xml.gz")[1] == "gz"
    assert extract_extension("foo.xml.bz2")[1] == "bz2"
    assert extract_extension("foo.xml-p10001p10200.7z")[1] == "7z"


def test_normalize_path_noexist():
    with raises(FileNotFoundError):
        normalize_path("IDONTEXIST!!!")


def test_normalize_path_directory():
    with raises(IsADirectoryError):
        normalize_path(os.path.dirname(__file__))


def test_open():
    f = io.StringIO()
    assert f == reader(f)
