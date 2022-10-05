import pyforms
from   pyforms.basewidget import BaseWidget
from   pyforms.controls import ControlText
from   pyforms.controls import ControlButton

import pyttsx3

class SimpleExample1(BaseWidget):


    def __init__(self):
        super(SimpleExample1,self).__init__('Simple example 1')

        # Define engine
        self.engine = pyttsx3.init()
        self.rate = 150
        self.engine.setProperty('rate', self.rate)

        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)


        #Definition of the forms fields
        self._answer = ControlText('Answer')

        self.speedDecreaseButton = ControlButton("-")

        self.playButton = ControlButton("Play")

        self.speedIncreaseButton = ControlButton("+")

        self._submitButton = ControlButton('Submit')

        self.formset = [('_answer'), ('speedDecreaseButton', 'playButton', 'speedIncreaseButton'), '_submitButton']

        self.playButton.value = self.playAction

        self.speedDecreaseButton.value = self.speedDecreaseAction
        self.speedIncreaseButton.value = self.speedIncreaseAction

        self._submitButton.value = self.__submitButtonAction

    def speedDecreaseAction(self):
        self.rate = self.rate - 25
        self.engine.setProperty('rate', self.rate)
        print(self.rate)

    def speedIncreaseAction(self):
        self.rate = self.rate + 25
        self.engine.setProperty('rate', self.rate)
        print(self.rate)

    def playAction(self):
        self.playButton.hide()
        self.engine.say('antidisestablishment')
        self.engine.runAndWait()
        self.playButton.show()

    def __submitButtonAction(self):
        ans = self._answer.value
        print(ans)

#Execute the application
if __name__ == "__main__": pyforms.start_app( SimpleExample1 )

