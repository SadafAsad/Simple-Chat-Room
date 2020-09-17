import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class EpicApp(App):
    # initiallization method
    def build(self):
        return Label(text="Hey there!")


if __name__ == "__main__":
    EpicApp().run()
