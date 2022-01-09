"""
A group of API end points that require user authentication by providing a
signature produces from private key of asymmetric encryption algorithm.

These calls return user specified information such as user balance,
trade history, open orders, withdraws etc. They also allow to make some
risky actions as place an order, that could unalterable affect your balance.

USE THEM WISELY!
"""
from .public_api import BASE_URL

# Get information about user balance
USER_BALANCE_QUERY = "/v2/account/balance"

USER_BALANCE_URL = BASE_URL + USER_BALANCE_QUERY

# Get user's opened orders by pair
USER_OPEN_ORDERS_BY_PAIR_QUERY = "/v2/account/orders/open/"

USER_OPEN_ORDERS_BY_PAIR_PATTERN = "".join(
    [
        BASE_URL,
        USER_OPEN_ORDERS_BY_PAIR_QUERY,
        "{pair}"
    ]
)
