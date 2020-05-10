QUEST_SPEAK, QUEST_HUNT, QUEST_CARRY = 'QSPEAK', 'QHUNT', 'QCARRY'


class Character:
    def __init__(self):
        self.name = 'Navigator'
        self.xp = 0
        self.passed_quests = set()
        self.taken_quests = set()


class Event:
    def __init__(self, kind):
        self.kind = kind


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, char, event):
        if self.__successor is not None:
            self.__successor.handle(char, event)

    @staticmethod
    def quest_action(quest_name, char, quest_xp):
        if quest_name not in (char.passed_quests | char.taken_quests):
            print(f'Квест "{quest_name}" получен!')
            char.taken_quests.add(quest_name)
        elif quest_name in char.taken_quests:
            print(f'Квест "{quest_name}" сдан!')
            char.passed_quests.add(quest_name)
            char.taken_quests.remove(quest_name)
            char.xp += quest_xp


class QuestSpeak(NullHandler):
    def handle(self, char, event):
        if event.kind == QUEST_SPEAK:
            self.quest_action('Поговорить в волшебником', char, quest_xp=100)
        else:
            print('Событие передано дальше')
            super().handle(char, event)


class QuestHunt(NullHandler):
    def handle(self, char, event):
        if event.kind == QUEST_HUNT:
            self.quest_action('Охота на медведя', char, quest_xp=200)
        else:
            print('Событие передано дальше')
            super().handle(char, event)


class QuestCarry(NullHandler):
    def handle(self, char, event):
        if event.kind == QUEST_CARRY:
            self.quest_action('Доставить посылку', char, quest_xp=50)
        else:
            print('Событие передано дальше')
            super().handle(char, event)


class QuestGiver:
    def __init__(self):
        self.handlers = QuestCarry(QuestHunt(QuestSpeak(NullHandler())))
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def handle_quests(self, charaster):
        for event in self.events:
            self.handlers.handle(charaster, event)


events = [Event(QUEST_CARRY), Event(QUEST_HUNT), Event(QUEST_SPEAK)]
quest_giver = QuestGiver()
for event in events:
    quest_giver.add_event(event)

player = Character()

quest_giver.handle_quests(player)
print('Получено:', player.taken_quests)
print('Сдано:', player.passed_quests)
player.taken_quests = {'Охота на медведя', 'Доставить посылку'}
quest_giver.handle_quests(player)
quest_giver.handle_quests(player)
