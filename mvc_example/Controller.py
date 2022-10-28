from pyvent.event.Module import *
from pyvent.data.Module import *
from mvc_example.WordList import word_list

class Controller:
    instance = None
    model = None

    def __init__(self):
        if not self.initialized:
            self.submitAnswer = InvokeableFunction(self.model.on_submit)
            self.getCurrentWord = InvokeableFunction(self.model.get_current_word)
            self.close = BindableEvent()

    def __new__(cls):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
            cls.instance.initialized = False
            cls.model = _Model()
        return cls.instance


class _Model:
    instance = None

    def __init__(self):
        if not self.initialized:
            self.voiceRate = 150
            self.currentWordIndex = 0
            self.word_list = word_list["index_of_words"]
    def __new__(cls):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
            cls.instance.initialized = False
        return cls.instance

    def on_speed_change(self, bundle):
        amount = bundle.get("amount")
        self.voiceRate += amount
        return_bundle = Bundle()
        return_bundle.add("rate", amount)
        return return_bundle

    def get_current_word(self, bundle):
        return self.word_list[self.currentWordIndex]

    def on_submit(self, submit):
        print("Submitted")
        if submit.lower() == self.get_current_word(None).lower():
            print("wOAH")
            self.currentWordIndex += 1
            if self.currentWordIndex >= len(word_list):
                self.currentWordIndex = 0
            print(self.currentWordIndex)
            return True
        else:
            print("REEEE")
            return False

