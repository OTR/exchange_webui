"""
`MAIL_BODY` - is a pattern to be formatted to combine email body, kind of ASCII
table with report about price change comparing to previous API request.

`SHELL_COMMAND` - a command to pass email body as stdin to Linux utility `mail`.

mail [-dEIinv ] [-a header ] [-b bcc-addr ] [-c cc-addr ] [-s subject ] to-addr

Where:
 `-s "foo"` - an option to set email subject as "foo". Specify subject on
 command line (only the first argument after the -s flag is used as a subject;
 be careful to quote subjects containing spaces).
 `to-addr` - an email address to send a letter to.

Reference: https://www.commandlinux.com/man-page/man1/Mail.1.html
"""


MAIL_BODY = """**{trade_pair}**
title\t\t\t| previous\t| current
last price:\t\t| {prev_last_price}\t\t| {curr_last_price}
highest_buy:\t| {prev_highest_buy}\t\t| {curr_highest_buy}
lowest_sell:\t| {prev_lowest_sell}\t\t| {curr_lowest_sell}
____________________________"""

SHELL_COMMAND = 'STR=$\'{body}\' && echo "$STR" | mail -s "{subject}" {mailto}'
