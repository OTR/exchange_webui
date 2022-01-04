
PATH_TO_SERIALIZED = os.path.join(os.getcwd(), "../.app_data/prev_state.dat")

if os.path.exists(PATH_TO_SERIALIZED):
    with open(PATH_TO_SERIALIZED, "rb") as f1:
        prev_data = pickle.load(f1)
    if not curr_data == prev_data:
        print("""mailbody""")
else:
    with open(PATH_TO_SERIALIZED, "wb") as f1:
        pickle.dump(curr_data, f1)
