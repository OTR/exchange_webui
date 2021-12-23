def populate_order_table(self):
    """"""
    state, b_created = OrderBookState.objects.get_or_create(
        lookup_time=self.lookup_time)

    for order_type, order_set in (
            ("sell", self.sell_orders), ("buy", self.buy_orders)
    ):
        for row in order_set:
            date_as_int = float(
                "{}.{}".format(row["date"][:10], row["date"][10:])
            )
            date = datetime.fromtimestamp(date_as_int)
            if order_type == "sell":
                _Model = SellOrder
            else:
                _Model = BuyOrder
            obj, created = _Model.objects.get_or_create(
                amount=row["amount"],
                date=date,
                label=row["label"],
                order_id=row["orderId"],
                price=row["price"],
                total=row["total"])
            if not created:
                print("Cannot create Order coz already created")
            if order_type == "sell":
                state.sell_orders.add(obj)
            else:
                state.buy_orders.add(obj)


if __name__ == '__main__':
    for row in rows:
        row.poulate_order_table()