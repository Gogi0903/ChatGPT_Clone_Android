from kivy.app import App
from kivy.uix.label import Label
from Custom_Layouts import BgBoxLayout


class Interface(BgBoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def send(self):

        self.ids.stackLayout.add_widget(Label(text=self.ids.textInput.text))
        self.ids.textInput.text = ''

    def answer(self):
        text = 'Ez lesz a chatgpt válasza'
        widget = Label(text=text)
        self.ids.stackLayout.add_widget(widget)
        self.ids.textInput.text = ''

    def clear(self):

        self.ids.stackLayout.clear_widgets()


class ChatGPTCloneApp(App):
    ...


if __name__ == '__main__':
    ChatGPTCloneApp().run()
