"""

"""


MAIL_BODY = """**{trade_pair}**
title\t\t\t| previous\t| current
last price:\t\t| {prev_last_price}\t\t| {curr_last_price}
highest_buy:\t| {prev_highest_buy}\t\t| {curr_highest_buy}
lowest_sell:\t| {prev_lowest_sell}\t\t| {curr_lowest_sell}
____________________________"""

SHELL_COMMAND = 'STR=$\'{body}\' && echo "$STR" | mail -s "OCCE Market" {mailto}'
