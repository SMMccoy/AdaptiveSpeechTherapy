from Controller import Controller
import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from pyvent.lua.Module import spawn
import pyttsx3


class View(BaseWidget):
    instance = None
    controller = Controller()

    def __init__(self):
        if not self.initialized:
            super(View, self).__init__('Gui MVC Model')
            self.voiceOutput = VoiceOutput(150, 0)
            self._answer = ControlText('Answer')

            self.playButton = ControlButton("Play")
            self.playSlowButton = ControlButton("Play Slow")
            self._submitButton = ControlButton('Submit')
            self.formset = [('_answer'), ('playSlowButton', 'playButton'), '_submitButton']

            self.playButton.value = lambda: self.on_play_word(150)
            self.playSlowButton.value = lambda: self.on_play_word(50)
            self._submitButton.value = lambda: self.on_submit(self._answer.value)

    def __new__(cls):
        if cls.instance is None:
            cls.instance = BaseWidget.__new__(cls)
            cls.instance.initialized = False
        return cls.instance

    def on_speed_change(self, amount):
        self.voiceOutput.change_rate(amount)

    def on_play_word(self, rate):
        word = self.controller.getCurrentWord.invoke(None)
        self.voiceOutput.say_at_rate(word, rate)

    def before_close_event(self):
        self.controller.close.fire(None)

    def on_submit(self, submit):
        print(self.controller.submitAnswer.invoke(submit))


class VoiceOutput:

    def __init__(self, rate, voiceId):
        self.engine = pyttsx3.init(None, True)
        self.rate = rate
        self.engine.setProperty("rate", self.rate)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[voiceId].id)
        self.busy = False

    def say(self, word):
        if not self.busy:
            self.busy = True
            spawn(lambda: self._speak(word))

    def say_at_rate(self, word, rate):
        self.set_rate(rate)
        self.say(word)

    def _speak(self, word):
        self.engine.say(word)
        self.engine.runAndWait()
        self.busy = False

    def change_rate(self, amount):
        self.rate += amount
        self.engine.setProperty("rate", self.rate)

    def set_rate(self, amount):
        self.rate = amount
        self.engine.setProperty("rate", self.rate)


if __name__ == "__main__":
    pyforms.start_app(View)
