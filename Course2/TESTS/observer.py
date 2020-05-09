from abc import ABC, abstractmethod


class ObservableEngine(Engine):
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

    def __init__(self):
        self.achievements = set()
        self.message_titles = list()

    def isnottitles(self, title):
        if title not in self.message_titles:
            self.message_titles.append(title)
            return True
        return False

    @abstractmethod
    def update(self, message):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def update(self, message):
        if self.isnottitles(message['title']):
            self.achievements.add(message['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        super().__init__()
        self.achievements = list()

    def update(self, message):
        if self.isnottitles(message['title']):
            self.achievements.append(message)
