from requests import get


original_params = {
    'date_from': '2016-01-01',
    'date_to': '2016-01-10',
    'origin': 'CNSGH',
    'destination': 'north_europe_main'
}


def test_one_empty_parameter():
    """Test request passing empty value to 'date_from'"""

    params = original_params

    params['date_from'] = ""

    result = get(
        "http://localhost/rates", params=params)

    assert result.status_code == 400
    assert result.json()["errors"] == {
        "date_from": [
            "The parameter should not be empty."
        ]
    }

def test_two_empty_parameters():
    """Test request passing empty value to 'date_from' and 'origin'"""

    params = original_params

    params['date_from'] = ""
    params['origin'] = ""

    result = get(
        "http://localhost/rates", params=params)

    assert result.status_code == 400
    assert result.json()["errors"] == {
        "date_from": [
            "The parameter should not be empty."
        ],
        "origin": [
            "The location should not be empty."
        ]
    }