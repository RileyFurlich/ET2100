from colorama import Fore
from item import ITEMS_DB

class CombatSystem:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def start_battle(self):
        print(Fore.RED + f"\n⚔️ A wild {self.monster.name} appears! ⚔️")
        
        while self.player.hp > 0 and self.monster.is_alive():
            print(Fore.CYAN + f"\nPlayer HP: {self.player.hp}/{self.player.max_hp} | {self.monster.name} HP: {self.monster.hp}/{self.monster.max_hp}")
            print("1. Basic Attack")
            print("2. Cast Skill")
            print("3. Use Health Potion")
            print("4. Attempt Escape")
            
            choice = input("Action (1-4): ").strip()
            
            # Reset/update skill cooldowns turn-by-turn
            for s in self.player.skills:
                s.update_cooldown()

            if choice == "1":
                dmg = self.player.atk
                self.monster.take_damage(dmg)
                print(Fore.GREEN + f"You attack {self.monster.name} for {dmg} damage!")
            elif choice == "2":
                print("\nAvailable Skills:")
                for idx, sk in enumerate(self.player.skills):
                    cd_str = "Ready" if sk.is_ready() else f"{sk.current_cd} turns CD"
                    print(f"{idx + 1}. {sk.name} [{cd_str}]")
                sk_choice = input("Select Skill #: ").strip()
                if sk_choice.isdigit() and 1 <= int(sk_choice) <= len(self.player.skills):
                    selected_skill = self.player.skills[int(sk_choice) - 1]
                    success = selected_skill.use(self.player, self.monster)
                    if not success:
                        continue
                else:
                    print(Fore.RED + "Invalid skill selection! Turn lost.")
            elif choice == "3":
                if self.player.inventory.remove_item("Health Potion", 1):
                    self.player.hp = min(self.player.max_hp, self.player.hp + 40)
                    print(Fore.GREEN + "You consumed a Health Potion and healed 40 HP!")
                else:
                    print(Fore.RED + "You don't have any Health Potions!")
                    continue
            elif choice == "4":
                print(Fore.YELLOW + "You managed to flee from combat!")
                return False
            else:
                print(Fore.RED + "Invalid choice! Turn wasted.")

            # Monster Counter-attack if alive
            if self.monster.is_alive():
                m_dmg = self.monster.atk
                self.player.hp = max(0, self.player.hp - m_dmg)
                print(Fore.RED + f"{self.monster.name} hits you for {m_dmg} damage!")

        # Resolution
        if self.player.hp <= 0:
            print(Fore.RED + "\n☠️ You have been slain in battle...")
            return False
        else:
            print(Fore.GREEN + f"\n🏆 You defeated {self.monster.name}!")
            self.player.gain_xp(self.monster.xp_reward)
            self.player.gold += self.monster.gold_reward
            print(Fore.YELLOW + f"Looted {self.monster.gold_reward} gold!")
            if self.monster.item_drop:
                self.player.inventory.add_item(self.monster.item_drop, 1)
                print(Fore.MAGENTA + f"Monster dropped: {self.monster.item_drop}!")
            return True