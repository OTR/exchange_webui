"""

"""
import json
import os
import pickle
from time import sleep
from urllib.request import urlopen


PAIRS = {
    "LB": {"slug": "ltv_btc", "module": 8},
    "LD": {"slug": "ltv_doge", "module": 0},
    "DB": {"slug": "doge_btc", "module": 8}
}

MAILTO = "crotosphera@gmail.com"


def get(pair, module=0):
    """"""
    url = "https://www.occe.io/api/v2/public/info/{}"
    url = url.format(pair)
    resp = urlopen(url).read()
    price_json = json.loads(resp)
    coin_info = price_json["coinInfo"][0]
    last_price = int(coin_info["lastPrice"] * 10 ** module)
    highest_buy = int(coin_info["highestBuy"] * 10 ** module)
    lowest_sell = int(coin_info["lowestSell"] * 10 ** module)
    curr_pair_data = {"last_price": last_price, "highest_buy": highest_buy,
                      "lowest_sell": lowest_sell}
    return curr_pair_data


def check():
    """"""
    curr_data = {}
    for key, value in PAIRS.items():
        curr_pair_data = get(value["slug"], module=value["module"])
        curr_data[key] = curr_pair_data
        sleep(1)
    stored_data_file = os.path.join(os.getcwd(),
                                    "../.app_data/prev_state_fork.dat")
    if os.path.exists(stored_data_file):
        mailbody = ""
        with open(stored_data_file, "rb") as f1:
            prev_data = pickle.load(f1)
        if not curr_data == prev_data:
            for key, value in curr_data.items():
                curr_pair_data = value
                mailbody += """**{6}**
title\t\t\t| previous\t| current
last price:\t\t| {3}\t\t| {0}
highest_buy:\t| {4}\t\t| {1}
lowest_sell:\t| {5}\t\t| {2}
____________________________
""".format(
                    curr_pair_data["last_price"],
                    curr_pair_data["highest_buy"],
                    curr_pair_data["lowest_sell"],
                    prev_data[key]["last_price"],
                    prev_data[key]["highest_buy"],
                    prev_data[key]["lowest_sell"],
                    PAIRS[key]["slug"])

            with open(stored_data_file, "wb") as f1:
                pickle.dump(curr_data, f1)
            mail_command = 'STR=$\'{body}\' && echo "$STR" | mail -s "OCCE Market" {mailto}'
            os.system(mail_command.format(mailto=MAILTO, body=mailbody))
        else:
            pass  # mailbody += ">>>"
    # print(mailbody)
    else:
        with open(stored_data_file, "wb") as f1:
            pickle.dump(curr_data, f1)


if __name__ == "__main__":
    # while True:
    check()
# sleep(60)
