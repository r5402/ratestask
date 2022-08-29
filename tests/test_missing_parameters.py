from requests import get

from utils import exclude_dictionary_keys


original_params = {
    'date_from': '2016-01-01',
    'date_to': '2016-01-10',
    'origin': 'CNSGH',
    'destination': 'north_europe_main'
}


def test_one_parameter_missing():
    """Test request without passing 'date_from'"""

    params = exclude_dictionary_keys(original_params, {"date_from"})

    result = get(
        "http://localhost/rates", params=params)

    assert result.status_code == 400
    assert result.json()["errors"] == {
        "date_from": [
            "Missing data for required field."
        ]
    }


def test_all_parameters_missing():
    """Test request without passing any parameter"""

    params = exclude_dictionary_keys(
        original_params, {"date_from", "date_to", "origin", "destination"})

    result = get(
        "http://localhost/rates", params=params)

    assert result.status_code == 400
    assert result.json()["errors"] == {
        "destination": [
            "Missing data for required field."
        ],
        "date_from": [
            "Missing data for required field."
        ],
        "date_to": [
            "Missing data for required field."
        ],
        "origin": [
            "Missing data for required field."
        ]
    }
