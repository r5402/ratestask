from requests import get


original_params = {
    'date_from': '2016-01-01',
    'date_to': '2016-01-10',
    'origin': 'CNSGH',
    'destination': 'north_europe_main'
}


def test_invalid_origin():
    """Test request passing invalid value to 'origin'"""

    params = original_params

    params['origin'] = "Oslo"

    result = get(
        "http://localhost/rates", params=params)

    assert result.status_code == 400
    assert result.json()["errors"] == {
        "origin": [
            "'Oslo' is not a valid location."
        ]
    }

def test_invalid_origin_destination():
    """Test request passing invalid value to 'origin' and 'destination'"""

    params = original_params

    params['origin'] = "Oslo"
    params['destination'] = "København"

    result = get(
        "http://localhost/rates", params=params)

    assert result.status_code == 400
    assert result.json()["errors"] == {
        "destination": [
            "'København' is not a valid location."
        ],
        "origin": [
            "'Oslo' is not a valid location."
        ]
    }