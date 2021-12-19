## Description

[OCCE API Documentation](https://www.occe.io/info#api)

Documentation at above link is outdated

This README file is last modified on 19.12.2021

Current version of API: v3

API v2 is deprecated

`public_api.py` - contains methods that doesn't require to have an account, 
api key, signature, authorization etc.

`BASE_URL = "https://api.occe.io"`

#### Supported trade pairs:

```json
"doge_btc", "eth_btc",

"btc_uah", "krb_btc", "doge_uah", "eth_uah", "rdd_btc", "tlr_btc", "ufo_btc",
"krb_usdt", "uni_usdt", "ltv_usdt", "btc_usdt", "krb_uah", "krb_rub", "krb_tlr",
"skyr_trx", "ufo_sugar", "vqr_trx", "pny_trx", "sapp_trx", "ufo_usdt", "rdd_uah",
"rdd_rub", "krb_rdd", "tlr_usdt", "ufo_rub", "krb_ufo", "ufo_uah", "btc_rub",
"uah_rub", "krb_xmr", "ufo_xmr", "xmr_uah", "usdt_rub", "usdt_uah", "tlr_uah",
"tlr_rub", "ufo_doge", "azr_trx", "idna_uah", "idna_rub", "idna_usdt", "trx_uah",
"bnb_uah", "sol_uah", "qrax_usdt", "pny_usdt", "matic_uah", "krb_trx", "ufo_trx",
```

## Public methods

### Server time

Return current server time as unix timestamp, could be used for authentication 
via TOTM, I suppose.

#### Request:

Method: `GET`

URL: `BASE_URL` + `/public/tradeview/time`

#### Response:

Headers:

```
Content-Type: application/json
access-control-allow-methods: OPTIONS,GET
```

OPTIONS?

Body: `1639938963`

Which is 2021.12.19 18:43:13 in GMT

### Trade history

TODO: fill description

#### Request

Method: `GET`

URL: `BASE_URL` + `/public/info`

#### Response

Headers: `Content-Type: application/json`

Body:

```json
{
  "result": "success",
  "data": {
    "pair": "krb_uah",
    "coinInfo": {
      "lastPrice": 3.57,
      "volume24h": 50,
      "highest24h": 3.57,
      "lowest24h": 3.57,
      "change24h": 0,
      "highestBuy": 3.53,
      "lowestSell": 3.59
    },
    "pair": "krb_btc",
    "coinInfo": {
      ...
    },
    ...
  }
}
```

### Trade history by pair

TODO: fill the description

#### Request

Method: `GET`

URL: `BASE_URL` + `/public/info/:pair`

Parameters:

`:pair` - `krb_btc`, full list of supported pairs see in description

#### Response:

Headers: ``

Body:

```json
    {
  "result": "success",
  "coinInfo": {
    "lastPrice": last price,
    "volume24h": volume for last 24h,
    "highest24h": highest price for last 24h,
    "lowest24h": lowest price for last 24h,
    "change24h": change for last 24h
  }
}
```

### Active orders

TODO: fill the description

#### Request

Method: `GET`

URL: `BASE_URL` + `/public/orders/:pair`

Parameters:

`:pair` - `krb_btc`, full list of supported pairs see in description

#### Response:

Headers: ``

Body:

```json
{
  "result": "success",
  "buyOrders": [
    {
      "type": "buy",
      "amount": volume of trading in BTC,
      "price": price for 1 BTC,
      "date": the time of placing the order,
      "pair": "krb_btc"
    }
  ],
  "sellOrders": [
    {
      "type": "sell",
      "amount": volume of trading in BTC,
      "price": price for 1 BTC,
      "date": the time of placing the order,
      "pair": "krb_btc"
    }
  ]
}
```