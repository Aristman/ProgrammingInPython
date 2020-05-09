import re
from abc import ABC, abstractmethod


class System:
    def __init__(self, text):
        tmp = re.sub(r'\W', ' ', text.lower())
        tmp = re.sub(r' +', ' ', tmp).strip()
        self.text = tmp

    def get_processed_text(self, processor):
        result = processor.process_text(self.text)
        print(*result, sep='\n')


class TextProcessor(ABC):
    @abstractmethod
    def process_text(self, text):
        pass


class WordCounter:
    def count_words(self, text):
        self.__words = dict()
        for word in text.split():
            self.__words[word] = self.__words.get(word, 0) + 1

    def get_count(self, word):
        return self.__words.get(word, 0)

    def get_all_words(self):
        return self.__words.copy()

class WordCounterAdapter(TextProcessor):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def process_text(self, text):
        self.adaptee.count_words(text)
        words = self.adaptee.get_all_words().keys()
        return sorted(words, key=lambda x: self.adaptee.get_count(x), reverse=True)


text = """Marco Polo is famous for his journeys across Asia. He was one of the first Europeans to travel in Mongolia and China. He wrote a famous book called ‘The Travels’.

He was born in Venice, Italy in 1254. In 1272, when he was only 17 years old, he travelled to Asia with his father and uncle. The journey was very long. They visited a lot of places and saw wonderful things: eye glasses, ice-cream, spaghetti and the riches of Asia.

After three years they entered China through the Great Wall. In 1275 Kublai Khon, the Emperor of China, met the visitors at his Summer Palace in the capital of China at Xanadu. The palace was very beautiful. There were a lot of gold things and silk curtains. The Emperor gave a big banquet. There were more than a thousand people in the palace. On the emperor’s birthday 5,000 soldiers rode through the city to the palace on elephants. Marco Polo visited some huge markets, where merchants from all over the world bought and sold all kinds of things. He was happy to see one of the greatest cities of the thirteenth century and spent 18 years in China.

When he returned to Italy in 1295, he became a popular storyteller. People came to his home to hear stories about his journeys in the East. Many of them did not believe him. When he died, he said: ‘I haven’t told half of what I saw, because no one can believe it.’"""

system = System(text)
print(system.text)

counter = WordCounter()
adapter = WordCounterAdapter(counter)
system.get_processed_text(adapter)