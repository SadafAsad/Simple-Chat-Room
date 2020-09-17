import kivy
from kivy.app import App
# put texts on screen
from kivy.uix.label import Label
# to organize widgets
from kivy.uix.gridlayout import GridLayout
# text from user
from kivy.uix.textinput import TextInput

class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        # row n1
        self.add_widget(Label(text="IP:"))

        self.ip = TextInput(multiline=False)
        self.add_widget(self.ip)

        # row n2
        self.add_widget(Label(text="Port:"))

        self.port = TextInput(multiline=False)
        self.add_widget(self.port)

        # row n3
        self.add_widget(Label(text="Username:"))

        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

class EpicApp(App):
    # initiallization method
    def build(self):
        return ConnectPage()


if __name__ == "__main__":
    EpicApp().run()
