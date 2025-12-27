class FoodOrder:
    def __init__(self, order_number, items_list, vip=False):
        self.order_number = order_number
        self.items_list = items_list
        self.is_vip = vip


class KitchenQueue:
    def __init__(self):
        self.orders = []  

    def add_order(self, order):
        if order.is_vip:
            self.orders.insert(0, order)  
        else:
            self.orders.append(order)      
        print(f"Order {order.order_number} added successfully!")

    def process_order(self):
        if not self.orders:
            print("No orders to process right now.")
            return

        next_order = self.orders.pop(0)
        print(f"\nProcessing Order #{next_order.order_number}")
        print("Items in order:", next_order.items_list)

if __name__ == "__main__":
    kitchen = KitchenQueue()

    # Adding some orders
    kitchen.add_order(FoodOrder(101, ["Burger", "Fries"]))
    kitchen.add_order(FoodOrder(102, ["Pizza"]))
    kitchen.add_order(FoodOrder(103, ["Pasta"], vip=True))  # VIP
    kitchen.add_order(FoodOrder(104, ["Sandwich"]))

    kitchen.process_order()
    kitchen.process_order()
    kitchen.process_order()
