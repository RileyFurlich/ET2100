from colorama import Fore

class NPC:
    def __init__(self, name, dialogue, quest_id=None):
        self.name = name
        self.dialogue = dialogue
        self.quest_id = quest_id

    def talk(self, player, quest_manager):
        print(Fore.MAGENTA + f"\n💬 [{self.name}]: \"{self.dialogue}\"")
        if self.quest_id:
            quest = quest_manager.quests.get(self.quest_id)
            if quest and not quest.active:
                quest.active = True
                print(Fore.YELLOW + f"[New Quest Accepted] {quest.title}")
            elif quest and quest.completed:
                print(Fore.GREEN + f"[{self.name}] Thank you for fulfilling my request!")
                player.gold += quest.reward_gold
                player.gain_xp(quest.reward_xp)
                quest.active = False # Clear quest once rewarded

def get_npcs():
    return {
        "Guard Captain": NPC("Guard Captain", "Monsters threaten our town! Clear the Slimes near Town Square.", "main_1"),
        "Old Veteran": NPC("Old Veteran", "Goblins are advancing! Go deeper into the Wilds to stop them.", "main_2"),
        "Town Priest": NPC("Town Priest", "I need 2 Herbs to make healing medicine. Can you bring them?", "side_herbs"),
        "Bounty Merchant": NPC("Bounty Merchant", "Bring me 2 Goblin Ears, and I'll pay handsomely.", "side_ears"),
        "Dungeon Warden": NPC("Dungeon Warden", "The Dark Lord awaits inside the Dungeon! End his terror!", "main_3")
    }