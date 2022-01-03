def backup(self):
    """"""
    with open(f"{self.lookup_time.timestamp()}.json", "wb") as f1:
        f1.write(self.raw_json)


if __name__ == '__main__':
    for row in rows:
        row.backup()
