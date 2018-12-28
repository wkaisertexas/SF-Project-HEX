# this is the absolute GUI file for the HEX program
import turtle
import kivy  # this is for the GUI package

from kivy.app import App
from kivy.uix.label import Label


# constants
screen_x = 1000
screen_y = 2000


class Window(App):

    def build(self):
        return Label(text='Hello World')


Window.run()