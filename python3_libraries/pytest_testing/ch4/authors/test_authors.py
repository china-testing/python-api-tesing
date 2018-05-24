"""Some tests that use temp data files."""
import json


def test_brian_in_portland(author_file_json):
    """A test that uses a data file."""
    with author_file_json.open() as f:
        authors = json.load(f)
    assert authors['Brian']['City'] == 'Portland'


def test_all_have_cities(author_file_json):
    """Same file is used for both tests."""
    with author_file_json.open() as f:
        authors = json.load(f)
    for a in authors:
        assert len(authors[a]['City']) > 0
