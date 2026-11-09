class Item:
    def __init__(self, name, item_type, val, cost, description):
        self.name = name
        self.item_type = item_type  # 'potion', 'equipment', 'quest'
        self.val = val              # Healing amount or stat boost
        self.cost = cost
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "item_type": self.item_type,
            "val": self.val,
            "cost": self.cost,
            "description": self.description
        }

    @staticmethod
    def from_dict(d):
        return Item(d["name"], d["item_type"], d["val"], d["cost"], d["description"])

# Global item dictionary template
ITEMS_DB = {
    "Health Potion": Item("Health Potion", "potion", 40, 20, "Restores 40 HP."),
    "Mega Potion": Item("Mega Potion", "potion", 100, 50, "Restores 100 HP."),
    "Iron Sword": Item("Iron Sword", "equipment", 10, 60, "Increases attack damage."),
    "Goblin Ear": Item("Goblin Ear", "quest", 0, 5, "Proof of a slain Goblin."),
    "Herb": Item("Herb", "quest", 0, 3, "A rare medicinal plant.")
}