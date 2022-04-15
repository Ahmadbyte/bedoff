import six

from filters.schema import base_query_params_schema
from filters.validations import (
    CSVofIntegers,
    IntegerLike,
    DatetimeWithTZ
)

# make a validation schema for players filter query params
bookings_query_schema = base_query_params_schema.extend(
    {
        "id": IntegerLike(),
        "status": IntegerLike()
    }
)