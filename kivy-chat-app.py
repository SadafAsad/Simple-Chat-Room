import kivy
from kivy.app import App
# put texts on screen
from kivy.uix.label import Label
# to organize widgets
from kivy.uix.gridlayout import GridLayout
# text from user
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import os

class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        # if the file exists
        if os.path.isfile("prev_details.txt"):
            with open("prev_details.txt", "r") as f:
                d = f.read().split(",")
                prev_ip = d[0]
                prev_port = d[1]
                prev_username = d[2]
        else:
            prev_ip = ""
            prev_port = ""
            prev_username = ""

        # row n1
        self.add_widget(Label(text="IP:"))

        self.ip = TextInput(text=prev_ip, multiline=False)
        self.add_widget(self.ip)

        # row n2
        self.add_widget(Label(text="Port:"))

        self.port = TextInput(text=prev_port, multiline=False)
        self.add_widget(self.port)

        # row n3
        self.add_widget(Label(text="Username:"))

        self.username = TextInput(text=prev_username, multiline=False)
        self.add_widget(self.username)

        # row n4
        self.join = Button(text="Join")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())
        self.add_widget(self.join)

    def join_button(self, instance):
        ip = self.ip.text
        port = self.port.text
        username = self.username.text

        print(f"attempting to join {ip}:{port} as {username}")

        with open("prev_details.txt", "w") as f:
            f.write(f"{ip},{port},{username}")

class EpicApp(App):
    # initiallization method
    def build(self):
        return ConnectPage()


if __name__ == "__main__":
    EpicApp().run()
