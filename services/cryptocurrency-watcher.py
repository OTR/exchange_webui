"""

"""
import json
from urllib.request import urlopen
import pickle
import os
import winsound
import sys


URL = "https://www.occe.io/api/v2/public/info/ltv_btc"
resp = urlopen(URL).read()
price_json = json.loads(resp)
coin_info = price_json["coinInfo"][0]
last_price = int(coin_info["lastPrice"] * 10**8)
highest_buy = int(coin_info["highestBuy"] * 10**8)
lowest_sell = int(coin_info["lowestSell"] * 10**8)

curr_data = {"last_price": last_price, "highest_buy": highest_buy,
             "lowest_sell": lowest_sell}
# print(curr_data)
stored_data_file = os.path.join(os.getcwd(), "../.app_data/prev_state.dat")

if os.path.exists(stored_data_file):
    with open(stored_data_file, "rb") as f1:
        prev_data = pickle.load(f1)
    if not curr_data == prev_data:
        print("""title\t\t\t| previous\t| current
    last price:\t\t| {3}\t\t| {0}
    highest_buy:\t| {4}\t\t| {1}
    lowest_sell:\t| {5}\t\t| {2}""".format(curr_data["last_price"],
                                           curr_data["highest_buy"],
                                           curr_data["lowest_sell"],
                                           prev_data["last_price"],
                                           prev_data["highest_buy"],
                                           prev_data["lowest_sell"]))
    try:
        while True:
            winsound.PlaySound("SystemExclamation", winsound.SND_LOOP)
    except KeyboardInterrupt as err:
        sys.exit()
else:
    with open(stored_data_file, "wb") as f1:
        pickle.dump(curr_data, f1)
