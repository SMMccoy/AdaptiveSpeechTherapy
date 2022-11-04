from pyvent.example_patterns.Singleton import Singleton
from perceptron_mvc_example.Controller import Controller
import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from pyforms.controls import ControlSlider
from pyvent.event.Module import BindableEvent
from pyvent.data.Module import Bundle
from perceptron_mvc_example.FTTS import FTTS
import playsound


class View(BaseWidget):
    MAX_SIZE_X = 400
    MAX_SIZE_Y = 200
    MARGIN = 15
    SPEED_SLIDER_MAXIMUM = 10
    SPEED_SLIDER_MINIMUM = 1
    SPEED_SLIDER_DEFAULT = 7
    CONTROLLER = Controller()

    def __init__(self):
        super(View, self).__init__('Gui Perceptron MVC Model')
        self.FTTS = FTTS()
        self.speed_slider = ControlSlider(
            'Speed',
            default=self.SPEED_SLIDER_DEFAULT,
            minimum=self.SPEED_SLIDER_MINIMUM,
            maximum=self.SPEED_SLIDER_MAXIMUM,
            helptext="Change listening speed"
        )
        self._answer = ControlText('Answer', helptext="Enter your answer here")
        self.playButton = ControlButton("Listen", helptext="Listen to word")
        self.set_margin(self.MARGIN)
        self.setFixedSize(self.MAX_SIZE_X, self.MAX_SIZE_Y)
        self._submitButton = ControlButton('Submit', helptext="Submit your answer")
        self.formset = ['_answer', ('playButton', 'speed_slider'), '_submitButton']
        self.set_up_buttons()
        self.on_listen_to_word()

    def set_up_buttons(self):
        self._submitButton.value = lambda: self.on_submit(self._answer.value)
        self.playButton.value = self.on_listen_to_word

    def on_submit(self, answer):
        self._answer.value = ""
        bundle = self.CONTROLLER.submit_answer.invoke(answer)
        if bundle.get("result"):
            print("Correct")
        else:
            print("Failure")
        self.on_listen_to_word()

    def on_listen_to_word(self):
        word = self.CONTROLLER.get_current_word.invoke(None)
        speed = 200 * (self.speed_slider.value / 7)
        print("saying: ", word)
        self.FTTS.say(word, speed)


if __name__ == "__main__":
    pyforms.start_app(View, geometry=(100, 100, 350, 150))
