import math

import perceptron_mvc_example.Controller
from pyvent.example_patterns.Singleton import Singleton
from pyvent.event.Module import BindableEvent
from pyvent.event.Module import InvokeableFunction
from pyceptron.Module import Perceptron
from pyvent.data.Module import Bundle
from WordListHandler import get_words_in_level_range
from WordListHandler import calculate_word_difficulty
from WordListHandler import ban_word
import random
from ini_handler import ini

class Model(Singleton):
    RANGE = .75
    SCORE_RATE = .045
    POWER = 10

    def __init__(self):
        if not self.initialized:
            super().__init__()
            self.choice = 0
            self.machine = Perceptron(26 * 18, .01, 1, 0)
            self.current_word = ""
            self.ini_class = ini()
            self.level = self.ini_class.getLevel()
            self.choose_next_word()



    def get_current_word(self, bundle):
        return self.current_word

    def choose_next_word(self):
        words = get_words_in_level_range(self.level, self.RANGE)
        word_number = len(words)
        correct_words = []
        print(self.choice, self.machine.learned)
        for word in words:
            if self.machine.input(word):
                correct_words.append(word)
        print("Percentage of comprehension: ", len(correct_words), "/", word_number)
        if self.choice < 2 or self.machine.learned <= 20:
            print("Chose random word")
            self.choice += 1
            self.current_word = random.choice(words)
        else:
            self.choice = 0
            self.current_word = random.choice(words)
            random.shuffle(words)
            is_random = True
            for word in words:
                if not self.machine.input(word):
                    is_random = False
                    print("Chose word that you are bad at")
                    self.current_word = word
                    break

            if is_random:
                print("Chose random word could not find bad one to use")
        print("Word level: ", calculate_word_difficulty(self.current_word))



    def on_submit_answer(self, answer):
        return_bundle = Bundle()
        correct = self.current_word.lower() == str.lower(answer)
        return_bundle.add("result", correct)

        if correct:
            delta = math.pow(calculate_word_difficulty(self.current_word) / self.level, self.POWER)
            ban_word(self.current_word, 20)
            self.level += self.SCORE_RATE * delta
        else:
            delta = math.pow(self.level / calculate_word_difficulty(self.current_word), self.POWER)
            ban_word(self.current_word, 10)
            self.level -= self.SCORE_RATE * delta
        self.machine.learn(self.current_word, correct)
        self.choose_next_word()
        print("Level: ", self.level)
        self.ini_class.setLevel(self.level)
        return_bundle.add("next_word", self.current_word)
        return return_bundle
