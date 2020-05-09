from abc import ABC, abstractmethod


class NotifyManager:
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for subscribe in self.__subscribers:
            subscribe.update(message)


class AbstractObserver(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def update(self, message):
        pass

class MessageNotifier(AbstractObserver):
    def update(self, message):
        print(f'{self._name} Прошло сообщение !')

class PrintNotifier(AbstractObserver):
    def update(self, message):
        print(f'Для {self._name} пришло сообщение {message}')


notifier = MessageNotifier('Notirier1')
printer1 = PrintNotifier('printer1')
printer2 = PrintNotifier('Printer2')
manager = NotifyManager()

manager.subscribe(notifier)
manager.subscribe(printer1)
manager.subscribe(printer2)

manager.notify('Сообщение Привет!')