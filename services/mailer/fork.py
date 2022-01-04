

def check():
    """"""
    curr_data = {}
    curr_pair_data = get_current_prices()
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
                mailbody += """""".format(
                    curr_pair_data["last_price"],
                    curr_pair_data["highest_buy"],
                    curr_pair_data["lowest_sell"],
                    prev_data[key]["last_price"],
                    prev_data[key]["highest_buy"],
                    prev_data[key]["lowest_sell"],
                    PAIRS[key]["slug"])

            with open(stored_data_file, "wb") as f1:
                pickle.dump(curr_data, f1)
            mail_command = ""
            os.system(mail_command.format(mailto=EMAIL_RECEIVER, body=mailbody))
        else:
            pass
    else:
        with open(stored_data_file, "wb") as f1:
            pickle.dump(curr_data, f1)


if __name__ == "__main__":
    # while True:
    check()
    # sleep(60)
