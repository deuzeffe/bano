import pytest

from bano import helpers


def test_is_valid_housenumber():
    assert helpers.is_valid_housenumber('1234') is True
    assert helpers.is_valid_housenumber('012345678910') is False


@pytest.mark.parametrize('input,output', [
    ({}, ''),
    ({'addr:postcode': '75001'}, '75001'),
    ({'postal_code': '75001'}, '75001'),
    ({'addr:postcode': '75001', 'postal_code': '77999'}, '75001'),
    ({'addr:postcode': '', 'postal_code': '77999'}, '77999'),
    ({'addr:postcode': '', 'postal_code': ''}, '')
])
def test_find_cp_in_tags(input, output):
    assert helpers.find_cp_in_tags(input) == output