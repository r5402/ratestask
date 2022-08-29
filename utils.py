from marshmallow import (
    Schema,
    ValidationError,
    fields
)
import psycopg
from os import environ

database_host = environ.get("DATABASE_HOST")
database_password = environ.get("DATABASE_PASSWORD")


def query_database(query):
    query_result = None

    with psycopg.connect(f"postgresql://postgres:{database_password}@{database_host}") as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)

            query_result = cursor.fetchall()

    return query_result


def get_location_codes(location):
    """Get location codes and formats them into a string separated by commas"""

    raw_location_codes = query_database(
        f"""
        SELECT ports.code
        FROM ports
        JOIN regions ON regions.slug = ports.parent_slug
        WHERE regions.parent_slug = '{location}'
            OR ports.code = '{location}'
            OR PORTS.parent_slug = '{location}'
        """
    )

    location_codes_list = [
        location_code for location_codes_tuple in raw_location_codes for location_code in location_codes_tuple]

    location_codes_string = ' ,'.join(
        f"'{location_code}'" for location_code in location_codes_list)

    return location_codes_string


def check_empty_parameter(value):
    if value is "":
        raise ValidationError(f"The parameter should not be empty.")


def check_location(location):
    """Check if the location parameter is empty and the location exists in the database"""

    if location is "":
        raise ValidationError(f"The location should not be empty.")

    location_codes = get_location_codes(location)

    if not location_codes:
        raise ValidationError(f"'{location}' is not a valid location.")


class RatesQueryParametersSchema(Schema):
    date_from = fields.String(required=True, validate=check_empty_parameter)
    date_to = fields.String(required=True, validate=check_empty_parameter)
    origin = fields.String(required=True, validate=check_location)
    destination = fields.String(required=True, validate=check_location)
