from bano import helpers

def test_find_cp_in_tags():
    assert helpers.find_cp_in_tags({'addr:postcode': '95120'}) == '95120'
    assert helpers.find_cp_in_tags({'postal_code': '95120'}) == '95120'
    assert helpers.find_cp_in_tags({'postal_code': None}) == ''
    assert helpers.find_cp_in_tags({'addr:postcode': '95120', 'postal_code': '93800'}) == '95120'