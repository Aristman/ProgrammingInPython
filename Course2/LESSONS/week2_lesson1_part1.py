from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def do_somthing(self):
        print('Привет')

class B(A):

    def anothe_do_somthing(self):
        print('Экземпляр B')

    def do_somthing(self):
        print('Новая реализация')

a = B()
a.do_somthing()
a.anothe_do_somthing()