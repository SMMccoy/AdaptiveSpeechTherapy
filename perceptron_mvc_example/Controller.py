import perceptron_mvc_example.Model
from pyvent.example_patterns.Singleton import Singleton
from pyvent.event.Module import BindableEvent
from pyvent.event.Module import InvokeableFunction
from perceptron_mvc_example.Model import Model

class Controller(Singleton):
    _MODEL = Model()

    def __init__(self):
        if not self.initialized:
            super().__init__()
            self.submit_answer = InvokeableFunction(self._MODEL.on_submit_answer)
            self.get_current_word = InvokeableFunction(self._MODEL.get_current_word)
