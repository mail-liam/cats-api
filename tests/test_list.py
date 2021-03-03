"""Tests for API_ENDPOINT/facts/.

Example response has all items in an object with an 'all' key,
while endpoint is actually returning a JSON array.
Proceeding with tests as though array is accurate.
"""

def test_list_response_contains_id(api_list_data):
    fact, *other = api_list_data

    assert '_id' in fact.keys()


def test_list_response_has_matching_test_id(api_list_data, test_data):
    fact, *other = api_list_data

    for test_fact in test_data:
        match = list(filter(lambda test_fact: test_fact['_id'] == fact['_id'], test_data))

        assert len(match) == 1


# def test_list_response_contains_text(api_list_data):
#     fact, *other = api_list_data

