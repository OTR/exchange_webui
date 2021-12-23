"""

"""
from .public_api import BASE_URL

# Get information about user balance
USER_BALANCE_QUERY = "/v2/account/balance"

USER_BALANCE_URL = BASE_URL + USER_BALANCE_QUERY

# Get user's opened orders by pair
USER_OPEN_ORDERS_BY_PAIR_QUERY = "/v2/account/orders/open/"

USER_OPEN_ORDERS_BY_PAIR_PATTERN = BASE_URL + USER_OPEN_ORDERS_BY_PAIR_QUERY +\
                                   "{pair}"
