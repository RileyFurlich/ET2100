from colorama import Fore
from item import ITEMS_DB

class Shop:
    def __init__(self):
        self.catalog = ["Health Potion", "Mega Potion", "Iron Sword"]

    def enter(self, player):
        while True:
            print(Fore.YELLOW + f"\n=== Merchant Shop === (Your Gold: {player.gold}g)")
            for idx, item_name in enumerate(self.catalog):
                item = ITEMS_DB[item_name]
                print(f"{idx + 1}. {item.name} - {item.cost}g ({item.description})")
            print("4. Exit Shop")
            
            choice = input("Select item to buy (1-4): ").strip()
            if choice in ["1", "2", "3"]:
                item_name = self.catalog[int(choice) - 1]
                item = ITEMS_DB[item_name]
                if player.gold >= item.cost:
                    player.gold -= item.cost
                    player.inventory.add_item(item.name, 1)
                    print(Fore.GREEN + f"Purchased 1x {item.name}!")
                    if item.item_type == "equipment":
                        player.atk += item.val
                        print(Fore.CYAN + f"Equipped {item.name}! ATK increased by {item.val}.")
                else:
                    print(Fore.RED + "You don't have enough gold!")
            elif choice == "4":
                break
            else:
                print(Fore.RED + "Invalid choice.")