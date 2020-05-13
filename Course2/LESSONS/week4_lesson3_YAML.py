import yaml

hero_yaml = """
--- !Character
factory:
    !factory assassin
name:
    777444444
"""


class HeroFactory:
    @classmethod
    def create_hero(Class, name):
        return Class.Hero(name)

    @classmethod
    def create_spell(Class):
        return Class.Spell()

    @classmethod
    def create_weapon(Class):
        return Class.Weapon()


class WarriorFactory(HeroFactory):
    class Hero:
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

    class Weapon:
        def hit(self):
            return 'Меч'

    class Spell:
        def cast(self):
            return ('Удар')


class AssassinFactory(HeroFactory):
    class Hero:
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

    class Spell:
        def cast(self):
            return 'Невидимость'

    class Weapon:
        def hit(self):
            return 'Кинжал'


class Character(yaml.YAMLObject):
    yaml_tag = '!Character'

    def create_hero(self):
        hero = self.factory.create_hero(self.name)

        weapon = self.factory.create_weapon()
        spell = self.factory.create_spell()

        hero.add_weapon(weapon)
        hero.add_spell(spell)
        return hero


def factory_constructor(loader, node):
    data = loader.construct_scalar(node)
    if data == 'assassin':
        return AssassinFactory
    elif data == 'warrior':
        return WarriorFactory
    else:
        return None

loader = yaml.Loader
loader.add_constructor('!factory', factory_constructor)
hero = yaml.load(hero_yaml).create_hero()
hero.hit()
hero.cast()