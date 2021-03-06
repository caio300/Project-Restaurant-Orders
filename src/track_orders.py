from src.analyze_log import (
    favorite_order,
    never_ordered,
    days_never_visited,
)


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        return favorite_order(self.orders, costumer)

    def get_never_ordered_per_costumer(self, costumer):
        return never_ordered(self.orders, costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return days_never_visited(self.orders, costumer)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
