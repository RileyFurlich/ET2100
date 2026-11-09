class Monster:
    def __init__(self, name, hp, atk, xp_reward, gold_reward, item_drop=None):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.atk = atk
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward
        self.item_drop = item_drop

    def take_damage(self, amount):
        self.hp = max(0, self.hp - amount)

    def is_alive(self):
        return self.hp > 0

# 5 Monster Subclasses
class Slime(Monster):
    def __init__(self):
        super().__init__("Slime", hp=30, atk=5, xp_reward=15, gold_reward=5, item_drop="Herb")

class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", hp=50, atk=10, xp_reward=30, gold_reward=15, item_drop="Goblin Ear")

class Skeleton(Monster):
    def __init__(self):
        super().__init__("Skeleton", hp=75, atk=14, xp_reward=45, gold_reward=25, item_drop="Health Potion")

class Orc(Monster):
    def __init__(self):
        super().__init__("Orc", hp=110, atk=20, xp_reward=70, gold_reward=40, item_drop="Mega Potion")

class DarkLordBoss(Monster):
    def __init__(self):
        super().__init__("Dark Lord (FINAL BOSS)", hp=220, atk=28, xp_reward=200, gold_reward=150, item_drop="Iron Sword")