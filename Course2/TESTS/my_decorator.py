from abc import ABC, abstractmethod
from inspect import isabstract


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


class AbstractEffect(ABC):
    def __init__(self, base):
        self.base = base
        self.changes = {}

    @abstractmethod
    def get_positive_effects(self):
        self.base.get_positive_effects()

    @abstractmethod
    def get_negative_effects(self):
        self.base.get_negative_effects()

    def get_stats(self):
        stats = self.base.get_stats()
        for it in self.changes:
            stats[it] += self.changes[it]
        return stats


class AbstractPositive(AbstractEffect):
    def __init__(self, base):
        super(AbstractPositive, self).__init__(base)

    @abstractmethod
    def get_positive_effects(self):
        super(AbstractPositive, self).get_positive_effects()

    def get_negative_effects(self):
        super(AbstractPositive, self).get_negative_effects()


class AbstractNegative(AbstractEffect):
    def get_positive_effects(self):
        super(AbstractNegative, self).get_positive_effects()

    @abstractmethod
    def get_negative_effects(self):
        super(AbstractNegative, self).get_negative_effects()


class Berserk(AbstractPositive):
    def __init__(self):
        super().__init__(self)
        self.stats = {
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
        pass


class Blassing(AbstractPositive):
    pass


class Weakness(AbstractNegative):
    pass


class EvilEye(AbstractNegative):
    pass


class Course(AbstractNegative):
    pass

hero = Hero()
print(hero.get_stats())
berserk = Berserk()
