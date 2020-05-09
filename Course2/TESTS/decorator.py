from abc import ABC, abstractmethod

class AbstractEffect(ABC, Hero):
    def __init__(self, base):
        super(Hero).__init__()
        self.base = base

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
    @abstractmethod
    def get_positive_effects(self):
        return super().get_positive_effects()

    def get_negative_effects(self):
        return super().get_negative_effects()


class AbstractNegative(AbstractEffect):
    def get_positive_effects(self):
        return self.base.get_positive_effects()

    @abstractmethod
    def get_negative_effects(self):
        return self.base.get_negative_effects()


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
