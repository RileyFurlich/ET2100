from colorama import Fore

class Skill:
    def __init__(self, name, mp_cost, cooldown):
        self.name = name
        self.mp_cost = mp_cost
        self.cooldown = cooldown
        self.current_cd = 0

    def update_cooldown(self):
        if self.current_cd > 0:
            self.current_cd -= 1

    def is_ready(self):
        return self.current_cd == 0

    def use(self, caster, target):
        raise NotImplementedError("Subclasses must implement use()")

# Subclass 1: Fireball
class Fireball(Skill):
    def __init__(self):
        super().__init__("Fireball", mp_cost=15, cooldown=2)

    def use(self, caster, target):
        if not self.is_ready():
            print(Fore.YELLOW + f"{self.name} is on cooldown! ({self.current_cd} turns left)")
            return False
        damage = caster.atk * 2 + 10
        target.take_damage(damage)
        self.current_cd = self.cooldown
        print(Fore.RED + f"🔥 {caster.name} casts Fireball at {target.name} for {damage} damage!")
        return True

# Subclass 2: Heal
class Heal(Skill):
    def __init__(self):
        super().__init__("Heal", mp_cost=10, cooldown=3)

    def use(self, caster, target=None):
        if not self.is_ready():
            print(Fore.YELLOW + f"{self.name} is on cooldown! ({self.current_cd} turns left)")
            return False
        heal_amt = 35
        caster.hp = min(caster.max_hp, caster.hp + heal_amt)
        self.current_cd = self.cooldown
        print(Fore.GREEN + f"✨ {caster.name} casts Heal restoring {heal_amt} HP!")
        return True

# Subclass 3: Power Strike
class PowerStrike(Skill):
    def __init__(self):
        super().__init__("Power Strike", mp_cost=5, cooldown=1)

    def use(self, caster, target):
        if not self.is_ready():
            print(Fore.YELLOW + f"{self.name} is on cooldown! ({self.current_cd} turns left)")
            return False
        damage = int(caster.atk * 1.5)
        target.take_damage(damage)
        self.current_cd = self.cooldown
        print(Fore.RED + f"💥 {caster.name} uses Power Strike on {target.name} for {damage} damage!")
        return True