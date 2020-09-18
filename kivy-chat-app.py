import kivy
from kivy.app import App
# put texts on screen
from kivy.uix.label import Label
# to organize widgets
from kivy.uix.gridlayout import GridLayout
# text from user
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
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


class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(halign="center", valign="middle", font_size=30)
        self.message.bind(width=self.update_text_width)
        self.add_widget(Self.message)

    def update_info(self, message):
        self.message.text = message

    def update_text_width(self, *_):
        self.message.text_size(self.message.width*0.9, None)

class EpicApp(App):
    # initiallization method
    def build(self):
        self.screen_manager = ScreenManager()

        self.connect_page = ConnectPage()
        screen = Screen(name="Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        self.info_page = InfoPage()
        screen = Screen(name="Info")
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == "__main__":
    EpicApp().run()
