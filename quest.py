from colorama import Fore

class Quest:
    def __init__(self, qid, title, description, reward_gold, reward_xp, target_count=1):
        self.qid = qid
        self.title = title
        self.description = description
        self.reward_gold = reward_gold
        self.reward_xp = reward_xp
        self.target_count = target_count
        self.progress = 0
        self.completed = False
        self.active = False

class QuestManager:
    def __init__(self):
        # 1 Multi-step Main Quest, 2 Side Quests
        self.quests = {
            "main_1": Quest("main_1", "Main Quest Step 1: Clear local Slimes", "Defeat 2 Slimes near Town Square", 30, 40, target_count=2),
            "main_2": Quest("main_2", "Main Quest Step 2: Clear Goblins", "Defeat 2 Goblins in the Wilds", 50, 70, target_count=2),
            "main_3": Quest("main_3", "Main Quest Step 3: Defeat the Dark Lord", "Slay the Dark Lord in Dungeon", 200, 300, target_count=1),
            "side_herbs": Quest("side_herbs", "Side Quest: Herbal Remedy", "Gather 2 Herbs for the Healer", 40, 30, target_count=2),
            "side_ears": Quest("side_ears", "Side Quest: Bounty Hunter", "Collect 2 Goblin Ears", 60, 50, target_count=2)
        }

    def update_progress(self, qid, amount=1):
        if qid in self.quests and self.quests[qid].active and not self.quests[qid].completed:
            q = self.quests[qid]
            q.progress += amount
            print(Fore.YELLOW + f"[QUEST PROGRESS] {q.title}: {q.progress}/{q.target_count}")
            if q.progress >= q.target_count:
                q.completed = True
                print(Fore.GREEN + f"✨ Quest Complete: {q.title}! Return to NPC for reward.")

    def display_quests(self):
        print(Fore.CYAN + "\n--- Quest Journal ---")
        for q in self.quests.values():
            if q.active:
                status = "COMPLETED" if q.completed else f"{q.progress}/{q.target_count}"
                print(f"- [{q.qid}] {q.title}: {status}")

    def to_dict(self):
        return {qid: {"active": q.active, "completed": q.completed, "progress": q.progress} for qid, q in self.quests.items()}

    def from_dict(self, data):
        if not data:
            return
        for qid, state in data.items():
            if qid in self.quests:
                self.quests[qid].active = state["active"]
                self.quests[qid].completed = state["completed"]
                self.quests[qid].progress = state["progress"]