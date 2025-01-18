class restaurantMenu:
    def _init_(self):
      self.meu_items = {}

    def add_item(self, name, price):
      self.menu_items[name] = price

    def get_price(self, name):
      return self.menu_items.get(name, None)

def main():
  menu = RestaurantMenu()
  # add initiral menu items
  menu.add_item("gurger", 10.99)
  menu add_item("fries", 4.99)

if_name_== "_main_":
  main()










