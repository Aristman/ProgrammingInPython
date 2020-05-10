class Character:
    def __init__(self):
        self.name = 'Navigator'
        self.xp = 0
        self.passed_quests = set()
        self.taken_quests = set()

class QuestGiver:
    def __init__(self):
        self.quests = []

    def add_quest(self, quest):
        self.quests.append(quest)

    def handle_quests(self, charaster):
        for quest in self.quests:
            quest(charaster)


def quest_action(quest_name, char, quest_xp):
    if quest_name not in (char.passed_quests | char.taken_quests):
        print(f'Квест "{quest_name}" получен!')
        char.taken_quests.add(quest_name)
    elif quest_name in char.taken_quests:
        print(f'Квест "{quest_name}" сдан!')
        char.passed_quests.add(quest_name)
        char.taken_quests.remove(quest_name)
        char.xp += quest_xp

def add_quest_speak(char):
    quest_action('Поговорить в волшебником', char, quest_xp=100)

def add_quest_hunt(char):
    quest_action('Охота на медведя', char, quest_xp=200)

def add_quest_carry(char):
    quest_action('Доставить посылку', char, quest_xp=50)


all_quest = [add_quest_carry, add_quest_hunt, add_quest_speak]
quest_giver = QuestGiver()
for quest in all_quest:
    quest_giver.add_quest(quest)

player = Character()
quest_giver.handle_quests(player)
print('Получено:', player.taken_quests)
print('Сдано:', player.passed_quests)
player.taken_quests = {'Охота на медведя', 'Доставить посылку'}
quest_giver.handle_quests(player)
quest_giver.handle_quests(player)