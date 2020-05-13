from abc import ABC, abstractmethod

class HeroFactory(ABC):
    @abstractmethod
    def create_hero(self, name):
        pass

    @abstractmethod
    def create_spell(self):
        pass

    @abstractmethod
    def create_weapon(self):
        pass


class Warrior:
    def __init__(self, name):
        self.name = name
        self.spell = None
        self.weapon = None

    def add_weapon(self, weapon):
        self.weapon = weapon

    def add_spell(self, spell):
        self.spell = spell

    def hit(self):
        print(f'Воин {self.name} ударил оружием {self.weapon.hit()}')

    def cast(self):
        print(f'Воин {self.name} вызвал заклинание {self.spell.cast()}')


class Sword:
    def hit(self):
        return 'Меч'


class Power:
    def cast(self):
        return ('Удар')


class WarriorFactory(HeroFactory):
    def create_hero(self, name):
        return Warrior(name)

    def create_spell(self):
        return Power()

    def create_weapon(self):
        return Sword()


class Assassin:
    def __init__(self, name):
        self.name = name
        self.weapon = None
        self.armor = None
        self.spell = None

    def add_weapon(self, weapon):
        self.weapon = weapon

    def add_armor(self, armor):
        self.armor = armor

    def add_spell(self, spell):
        self.spell = spell

    def hit(self):
        print(f'Убийца {self.name} ударил оружием {self.weapon.hit()}')

    def cast(self):
        print(f'Убийца {self.name} вызвал заклинание {self.spell.cast()}')


class Invisibility:
    def cast(self):
        return 'Невидимость'


class Dagger:
    def hit(self):
        return 'Кинжал'


class AssasinFactory(HeroFactory):
    def create_hero(self, name):
        return Assassin(name)

    def create_spell(self):
        return Invisibility()

    def create_weapon(self):
        return Dagger()


def create_hero(factory, name):
    hero = factory.create_hero(name)

    weapon = factory.create_weapon()
    spell = factory.create_spell()

    hero.add_weapon(weapon)
    hero.add_spell(spell)
    return hero

player = create_hero(AssasinFactory(), 'Атлант')

player.hit()
player.cast()

player2 = create_hero(WarriorFactory(), 'Конан')

player2.hit()
player2.cast()
