
from pytest import warns
from reporter.header import create_header

def test_create_header():
    authors = [{'firstname': 'John', 'lastname': 'Lennon', 'instru': 'rythm guitar'},
               {'firstname': 'Paul', 'lastname': 'McCartney', 'instru': 'bass'}]
    head = create_header(authors)
    assert "Paul" in head
    assert "Lennon" in head


def test_create_header_missing():
    authors = [{'firstname': 'George', 'instru': 'lead guitar'},
               {'lastname': 'Starr', 'instru': 'drums'}]

    with warns(UserWarning):
        head = create_header(authors)

    assert "George" in head
    assert "Starr" in head

def test_create_header_city():
    authors = [{'firstname': 'John', 'lastname': 'Lennon', 'instru': 'rythm guitar'},
               {'firstname': 'Paul', 'lastname': 'McCartney', 'instru': 'bass'}]
    head = create_header(authors, "NY")
    assert "NY" in head
