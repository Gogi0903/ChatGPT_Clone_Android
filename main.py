from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from Custom_Layouts import BgBoxLayout


class Interface(BgBoxLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        Clock.schedule_once(callback=self.send)

    def send(self, dt):

        txt = BoxLayout(text=self.ids.textInput.text)
        self.ids.conversationfield.add_widget(txt)


class ChatGPTCloneApp(App):
    ...


ChatGPTCloneApp().run()
