
PATH_TO_SERIALIZED = os.path.join(os.getcwd(), "uah_prev_state.dat")
if os.path.exists(PATH_TO_SERIALIZED):
    with open(PATH_TO_SERIALIZED, "rb") as f1:
        prev_data = pickle.load(f1)
    if not curr_data == prev_data:
        mailbody = """"""""

        shell_command = """"""
        os.system(shell_command.format(mailto=EMAIL_RECEIVER, body=mailbody))

        with open(PATH_TO_SERIALIZED, "wb") as f1:
            pickle.dump(curr_data, f1)
else:
    with open(PATH_TO_SERIALIZED, "wb") as f1:
        pickle.dump(curr_data, f1)
