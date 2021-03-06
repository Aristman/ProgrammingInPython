from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()

    def get_all(self):
        print(self.get_stats())
        print(self.get_positive_effects())
        print(self.get_negative_effects())


class AbstractEffect(ABC, Hero):
    def __init__(self, base):
        super(Hero).__init__()
        self.base = base
        self.changes = {}

    @abstractmethod
    def get_positive_effects(self):
        return self.base.get_positive_effects()

    @abstractmethod
    def get_negative_effects(self):
        return self.base.get_negative_effects()

    def get_stats(self):
        stats = self.base.get_stats()
        for it in self.changes:
            stats[it] += self.changes[it]
        return stats


class AbstractPositive(AbstractEffect):
    def get_negative_effects(self):
        return self.base.get_negative_effects()


class AbstractNegative(AbstractEffect):
    def get_positive_effects(self):
        return self.base.get_positive_effects()


class Berserk(AbstractPositive):
    def __init__(self, base):
        super().__init__(base)
        self.changes = {
            "HP": 50,  # health points
            "Strength": 7,  # сила
            "Perception": -3,  # восприятие
            "Endurance": 7,  # выносливость
            "Charisma": -3,  # харизма
            "Intelligence": -3,  # интеллект
            "Agility": 7,  # ловкость
            "Luck": 7  # удача
        }

    def get_positive_effects(self):
        return self.base.get_positive_effects() + ['Berserk']


class Blessing(AbstractPositive):
    def __init__(self, base):
        super().__init__(base)
        self.changes = {
            "Strength": 2,  # сила
            "Perception": 2,  # восприятие
            "Endurance": 2,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 2,  # интеллект
            "Agility": 2,  # ловкость
            "Luck": 2  # удача
        }

    def get_positive_effects(self):
        return self.base.get_positive_effects() + ['Blessing']


class Weakness(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)
        self.changes = {
            "Strength": -4,  # сила
            "Endurance": -4,  # выносливость
            "Agility": -4,  # ловкость
        }

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ['Weakness']


class EvilEye(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)
        self.changes = {
            "Luck": -10  # удача
        }

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ['EvilEye']


class Curse(AbstractNegative):
    def __init__(self, base):
        super().__init__(base)
        self.changes = {
            "Strength": -2,  # сила
            "Perception": -2,  # восприятие
            "Endurance": -2,  # выносливость
            "Charisma": -2,  # харизма
            "Intelligence": -2,  # интеллект
            "Agility": -2,  # ловкость
            "Luck": -2  # удача
        }

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ['Curse']


hero = Hero()
print(hero.get_stats())
berserk = Berserk(hero)
besrerk1 = Berserk(berserk)
ber2 = Berserk(besrerk1)
print(berserk.get_stats())
print(berserk.get_positive_effects())
print(berserk.get_negative_effects())
print(besrerk1.get_positive_effects())


bl1 = Blessing(ber2)
ber3 = Berserk(bl1)
print(ber3.get_positive_effects())
print('------------------')
print(hero.get_stats())
print(besrerk1.get_stats())
print(ber2.get_stats())
print(ber3.get_stats())
print(bl1.get_stats())
print('----------------')
weak = Weakness(bl1)
weak.get_all()
print('-----------------')
cour = Curse(weak)
cour.get_all()