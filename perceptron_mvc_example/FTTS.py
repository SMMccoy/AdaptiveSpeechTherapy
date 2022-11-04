import pyttsx3
from pyvent.lua.Module import spawn
from pyvent.event.Module import BindableEvent

class FTTS:
    def __init__(self):
        self.engine = pyttsx3.init(None, True)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.busy = False

    def _text_to_speech(self, text, rate):
        self.engine.setProperty("rate", rate)
        self.engine.say(text)
        self.engine.runAndWait()
        self.busy = False

    def say(self, text, rate):
        if not self.busy:
            self.busy = True
            spawn(lambda: self._text_to_speech(text, rate))


