from colorama import Fore
from map_manager import MapManager
from monster import Slime, Goblin, Skeleton, Orc, DarkLordBoss
from combat import CombatSystem
from quest import QuestManager
from npc import get_npcs
from shop import Shop
from item import ITEMS_DB

class GameEngine:
    def __init__(self, player, db_manager, username):
        self.player = player
        self.db_manager = db_manager
        self.username = username
        self.map_manager = MapManager()
        self.quest_manager = QuestManager()
        self.npcs = get_npcs()
        self.shop = Shop()

    def load_saved_state(self, saved_data):
        if saved_data:
            self.player.from_dict(saved_data["player"])
            self.quest_manager.from_dict(saved_data.get("quests"))

    def save_state(self):
        state = {
            "player": self.player.to_dict(),
            "quests": self.quest_manager.to_dict()
        }
        self.db_manager.save_game(self.username, state)
        print(Fore.GREEN + "\n💾 Progress saved successfully to TinyDB!")

    def play(self):
        print(Fore.YELLOW + "\n==========================================")
        print(Fore.CYAN +   "   WELCOME TO THE SHADOWS OF THE REALM    ")
        print(Fore.YELLOW + "==========================================")
        print("Story Intro: Dark forces surround your kingdom. Complete quests,")
        print("slay monsters, build your strength, and defeat the Dark Lord!\n")

        while self.player.hp > 0:
            self.map_manager.draw_map(self.player.current_map, self.player.x, self.player.y)
            print("\nOptions: (W/A/S/D) Move | (I)nventory | (C)haracter | (Q)uests | (T)ravel Map | (Save) | (Exit)")
            cmd = input("Action: ").strip().lower()

            if cmd in ["w", "a", "s", "d"]:
                dx, dy = 0, 0
                if cmd == "w": dy = -1
                elif cmd == "s": dy = 1
                elif cmd == "a": dx = -1
                elif cmd == "d": dx = 1

                new_x = self.player.x + dx
                new_y = self.player.y + dy

                if self.map_manager.is_valid_move(self.player.current_map, new_x, new_y):
                    self.player.x = new_x
                    self.player.y = new_y
                    self.check_tile_events()
                else:
                    print(Fore.RED + "Blocked! You cannot walk through walls or out of bounds.")

            elif cmd == "i":
                self.player.inventory.display()
            elif cmd == "c":
                self.player.display_status()
            elif cmd == "q":
                self.quest_manager.display_quests()
            elif cmd == "t":
                if self.player.current_map == "Town Square":
                    self.player.current_map = "Dungeon"
                else:
                    self.player.current_map = "Town Square"
                self.player.x, self.player.y = 1, 1
                print(Fore.CYAN + f"Traveled to {self.player.current_map}!")
            elif cmd == "save":
                self.save_state()
            elif cmd == "exit":
                self.save_state()
                print(Fore.YELLOW + "Game saved. Exiting program...")
                break

    def check_tile_events(self):
        layout = self.map_manager.get_layout(self.player.current_map)
        tile = layout[self.player.y][self.player.x]

        if tile == "N":
            npc_name = "Guard Captain" if self.player.current_map == "Town Square" else "Dungeon Warden"
            if npc_name in self.npcs:
                self.npcs[npc_name].talk(self.player, self.quest_manager)
                # Check for item quest completions
                if self.quest_manager.quests["side_herbs"].active:
                    if self.player.inventory.remove_item("Herb", 2):
                        self.quest_manager.update_progress("side_herbs", 2)
                if self.quest_manager.quests["side_ears"].active:
                    if self.player.inventory.remove_item("Goblin Ear", 2):
                        self.quest_manager.update_progress("side_ears", 2)

        elif tile == "S":
            self.shop.enter(self.player)

        elif tile == "M":
            monster = Slime() if self.player.current_map == "Town Square" else Skeleton()
            combat = CombatSystem(self.player, monster)
            if combat.start_battle():
                if isinstance(monster, Slime):
                    self.quest_manager.update_progress("main_1", 1)
                elif isinstance(monster, Skeleton):
                    self.quest_manager.update_progress("main_2", 1)

        elif tile == "B":
            print(Fore.RED + "\n⚠️ You step into the lair of the Final Boss!")
            boss = DarkLordBoss()
            combat = CombatSystem(self.player, boss)
            if combat.start_battle():
                self.quest_manager.update_progress("main_3", 1)
                print(Fore.YELLOW + "\n=============================================")
                print(Fore.GREEN +  "🎉 CONGRATULATIONS! YOU DEFEATED THE FINAL BOSS!")
                print(Fore.GREEN +  "        YOU HAVE SAVED THE REALM & WON!      ")
                print(Fore.YELLOW + "=============================================")
                exit()