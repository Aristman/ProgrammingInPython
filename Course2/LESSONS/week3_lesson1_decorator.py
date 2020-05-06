from abc import ABC, abstractmethod


class Creature(ABC):

    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def make_noise(self):
        pass


class Amimal(Creature):

    def feed(self):
        print('Я ем траву')

    def move(self):
        print('Я бегаю')

    def make_noise(self):
        print('МУУУУ!')


class AbstractDecorator(Creature):

    def __init__(self, base):
        self.base = base

    def move(self):
        self.base.move()

    def feed(self):
        self.base.feed()

    def make_noise(self):
        self.base.make_noise()


class Swimming(AbstractDecorator):

    def move(self):
        print('Я плаваю')

    def make_noise(self):
        print('...')


class Predator(AbstractDecorator):

    def feed(self):
        print('Я ем других зверей')


class Fast(AbstractDecorator):

    def move(self):
        self.base.move()
        print('Быстро!')

from inspect import isabstract

print(isabstract(AbstractDecorator))
animal = Amimal()
animal.move()
animal.feed()
animal.make_noise()

swiming = Swimming(animal)
swiming.move()
swiming.feed()
swiming.make_noise()

predator = Predator(swiming)
predator.move()
predator.feed()
predator.make_noise()

fast = Fast(predator)
fast.move()
fast.feed()
fast.make_noise()

faster = Fast(fast)
faster.move()
faster.feed()
faster.make_noise()

faster.base.base = faster.base.base.base
faster.move()
faster.feed()
faster.make_noise()
