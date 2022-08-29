from requests import get

case_1_params = {
    'date_from': '2016-01-01',
    'date_to': '2016-01-10',
    'origin': 'CNSGH',
    'destination': 'north_europe_main'
}


def test_average_price_case_1():
    """Test request passing valid values"""

    result = get(
        "http://localhost/rates", params=case_1_params)

    assert result.status_code == 200
    assert result.json() == [
        {
            "day": "2016-01-01",
            "average_price": 1112
        },
        {
            "day": "2016-01-02",
            "average_price": 1112
        },
        {
            "day": "2016-01-04",
            "average_price": None
        },
        {
            "day": "2016-01-05",
            "average_price": 1142
        },
        {
            "day": "2016-01-06",
            "average_price": 1142
        },
        {
            "day": "2016-01-07",
            "average_price": 1137
        },
        {
            "day": "2016-01-08",
            "average_price": 1124
        },
        {
            "day": "2016-01-09",
            "average_price": 1124
        },
        {
            "day": "2016-01-10",
            "average_price": 1124
        }
    ]


case_2_params = {
    'date_from': '2016-01-01',
    'date_to': '2016-01-04',
    'origin': 'china_main',
    'destination': 'scandinavia'
}


def test_average_price_case_2():
    """Test request passing valid values"""

    result = get(
        "http://localhost/rates", params=case_2_params)

    assert result.status_code == 200
    assert result.json() == [
        {
            "day": "2016-01-01",
            "average_price": 1718
        },
        {
            "day": "2016-01-02",
            "average_price": 1718
        }
    ]
