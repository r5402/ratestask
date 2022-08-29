from flask import Flask, jsonify, request
from utils import RatesQueryParametersSchema, get_location_codes, query_database
from marshmallow import (
    ValidationError
)

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


@app.route("/rates")
def get_rates():
    rates_query_parameters_schema = RatesQueryParametersSchema()

    raw_args = request.args.to_dict()

    try:
        result = rates_query_parameters_schema.load(raw_args)
    except ValidationError as errors:
        return {
            "errors": errors.messages
        }, 400

    origin_codes = get_location_codes(result.get("origin"))
    destination_codes = get_location_codes(result.get("destination"))

    average_prices = get_average_prices(result.get("date_from"), result.get(
        "date_to"), origin_codes, destination_codes)

    for average_price in average_prices:
        average_price["day"] = str(average_price["day"])
        average_price["average_price"] = int(
            average_price["average_price"]) if average_price["average_price"] is not None else None

    return jsonify(average_prices)


def get_average_prices(date_from, date_to, origin, destination):
    raw_average_prices = query_database(
        f"""
        SELECT day,
                CASE
                    WHEN COUNT(price) >= 3 THEN ROUND(AVG(price), 0)
                    WHEN COUNT(price) < 3 THEN NULL
                END AS average_price
        FROM prices
        WHERE orig_code in ({origin})
            AND dest_code in ({destination})
            AND day >= '{date_from}'
            AND day <= '{date_to}'
        GROUP BY day
        ORDER BY day
        """
    )

    average_prices = [dict(zip(['day', 'average_price'], price))
                      for price in raw_average_prices]

    return average_prices
