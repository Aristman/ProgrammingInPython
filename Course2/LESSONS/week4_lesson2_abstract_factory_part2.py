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


def create_hero(factory, name):
    hero = factory.create_hero(name)

    weapon = factory.create_weapon()
    spell = factory.create_spell()

    hero.add_weapon(weapon)
    hero.add_spell(spell)
    return hero


player = create_hero(AssassinFactory(), 'Атлант')

player.hit()
player.cast()

player2 = create_hero(WarriorFactory(), 'Конан')

player2.hit()
player2.cast()
