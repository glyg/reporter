import pytest

from reporter.header import create_header


def test_create_header():

    john = {
        "first": "John",
        'last': "Lennon",
        "instrument": "Singer"
    }

    paul = {
        "first": "Paul",
        'last': "McCartney",
    }

    header_str = create_header([john, paul])
    assert isinstance(header_str, str)
    assert "Paul McCartney" in header_str


def test_create_header_missing():

    john = {
        'last': "Lennon",
        "instrument": "Singer"
    }

    paul = {
        "first": "Paul",
    }
    with pytest.warns(UserWarning):
        header_str = create_header([john, paul])
    assert isinstance(header_str, str)
    assert not "Singer" in header_str
