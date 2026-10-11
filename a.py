class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        for item in self.items:
            print(item)


cart = ShoppingCart()
cart.add_item("Book")
cart.add_item("Pen")
cart.show_items()