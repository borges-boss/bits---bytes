class JournalView:
    def show_quests(self, quests):
        for quest in quests:
            print(f"Name: {quest.name}\nDescription: {quest.description}\n")