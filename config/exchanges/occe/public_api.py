"""
Constants to combine URL queries to make calls to public API end points.

These API calls return non user specified information i.e. treating you as
an anonymous user.

Last Modified: 04.01.2022
"""

# Common part of each final URL
BASE_URL = "https://api.occe.io"

# Available trade pairs on the market
TRADE_PAIRS = [
    "doge_btc", "eth_btc", "btc_uah", "krb_btc", "doge_uah", "eth_uah",
    "rdd_btc", "tlr_btc", "ufo_btc", "krb_usdt", "uni_usdt", "ltv_usdt",
    "btc_usdt", "krb_uah", "krb_rub", "krb_tlr", "skyr_trx", "ufo_sugar",
    "vqr_trx", "pny_trx", "sapp_trx", "ufo_usdt", "rdd_uah", "rdd_rub",
    "krb_rdd", "tlr_usdt", "ufo_rub", "krb_ufo", "ufo_uah", "btc_rub",
    "uah_rub", "krb_xmr", "ufo_xmr", "xmr_uah", "usdt_rub", "usdt_uah",
    "tlr_uah", "tlr_rub", "ufo_doge", "azr_trx", "idna_uah", "idna_rub",
    "idna_usdt", "trx_uah", "bnb_uah", "sol_uah", "qrax_usdt", "pny_usdt",
    "matic_uah", "krb_trx", "ufo_trx"
]
# ______________________________________________________________________________
# What trade pair to use to make API requests
TRADE_PAIR = "skyr_trx"

# ______________________________________________________________________________
# Get active orders by a certain trade pair
ACTIVE_ORDERS_QUERY = "/public/orders/"

ACTIVE_ORDERS_URL_PATTERN = BASE_URL + ACTIVE_ORDERS_QUERY + "{pair}"
# ______________________________________________________________________________
# Get server time. Used for signature creation when making private API calls
SERVER_TIME_QUERY = "/public/tradeview/time"

SERVER_TIME_URL = BASE_URL + SERVER_TIME_QUERY
# ______________________________________________________________________________
# Get market trade history by given trade pair
TRADE_HIST_BY_PAIR_QUERY = "/public/info/"

TRADE_HISTORY_BY_PAIR_PATTERN = BASE_URL + TRADE_HIST_BY_PAIR_QUERY + "{pair}"
# ______________________________________________________________________________
