from colorama import Fore
from inventory import Inventory
from skill import Fireball, Heal, PowerStrike

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.xp_to_next_lvl = 50
        self.max_hp = 100
        self.hp = 100
        self.atk = 15
        self.gold = 30
        self.x = 1
        self.y = 1
        self.current_map = "Town Square"
        self.inventory = Inventory()
        self.skills = [PowerStrike()]  # Initial skill

    def gain_xp(self, amount):
        self.xp += amount
        print(Fore.GREEN + f"You gained {amount} XP!")
        if self.xp >= self.xp_to_next_lvl:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp -= self.xp_to_next_lvl
        self.xp_to_next_lvl = int(self.xp_to_next_lvl * 1.5)
        self.max_hp += 20
        self.hp = self.max_hp
        self.atk += 5
        print(Fore.MAGENTA + f"\n🎉 LEVEL UP! You are now Level {self.level}!")
        
        # Unlock new skills at higher levels
        if self.level == 2 and not any(s.name == "Heal" for s in self.skills):
            self.skills.append(Heal())
            print(Fore.YELLOW + "Learned new skill: Heal!")
        elif self.level == 3 and not any(s.name == "Fireball" for s in self.skills):
            self.skills.append(Fireball())
            print(Fore.YELLOW + "Learned new skill: Fireball!")

    def display_status(self):
        print(Fore.CYAN + f"\n=== {self.name}'s Status ===")
        print(f"Level: {self.level} | XP: {self.xp}/{self.xp_to_next_lvl}")
        print(f"HP: {self.hp}/{self.max_hp} | ATK: {self.atk}")
        print(f"Gold: {Fore.YELLOW}{self.gold}g{Fore.CYAN}")
        print(f"Map: {self.current_map} at ({self.x}, {self.y})")
        print("Skills: " + ", ".join([s.name for s in self.skills]))

    def to_dict(self):
        return {
            "name": self.name,
            "level": self.level,
            "xp": self.xp,
            "xp_to_next_lvl": self.xp_to_next_lvl,
            "max_hp": self.max_hp,
            "hp": self.hp,
            "atk": self.atk,
            "gold": self.gold,
            "x": self.x,
            "y": self.y,
            "current_map": self.current_map,
            "inventory": self.inventory.to_dict(),
            "skill_names": [s.name for s in self.skills]
        }

    def from_dict(self, d):
        self.level = d["level"]
        self.xp = d["xp"]
        self.xp_to_next_lvl = d["xp_to_next_lvl"]
        self.max_hp = d["max_hp"]
        self.hp = d["hp"]
        self.atk = d["atk"]
        self.gold = d["gold"]
        self.x = d["x"]
        self.y = d["y"]
        self.current_map = d["current_map"]
        self.inventory.from_dict(d["inventory"])
        
        # Restore skills based on saved names
        skill_map = {"Power Strike": PowerStrike, "Heal": Heal, "Fireball": Fireball}
        self.skills = [skill_map[s_name]() for s_name in d.get("skill_names", []) if s_name in skill_map]