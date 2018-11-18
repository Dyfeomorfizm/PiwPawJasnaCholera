import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.label import Label

from app import run_app

class MyApp(App):
    def build(self):
        return Label(text=run_app())


if __name__ == '__main__':
    MyApp().run()
