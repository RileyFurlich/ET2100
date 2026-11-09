from colorama import Fore

class Inventory:
    def __init__(self):
        self.items = {}  # item_name: count

    def add_item(self, item_name, count=1):
        self.items[item_name] = self.items.get(item_name, 0) + count

    def remove_item(self, item_name, count=1):
        if item_name in self.items and self.items[item_name] >= count:
            self.items[item_name] -= count
            if self.items[item_name] == 0:
                del self.items[item_name]
            return True
        return False

    def display(self):
        print(Fore.CYAN + "\n--- Inventory ---")
        if not self.items:
            print("Your inventory is empty.")
            return
        for item_name, qty in self.items.items():
            print(f"- {item_name} x{qty}")

    def to_dict(self):
        return self.items

    def from_dict(self, data):
        self.items = data or {}