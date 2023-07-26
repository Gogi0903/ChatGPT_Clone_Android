from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from Custom_Layouts import BgBoxLayout


class Interface(BgBoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def send(self):
        txt_label = Label(text=self.ids.textInput.text)
        new_txt_box = BgBoxLayout(orientation='vertical', hex_code='#574bc9', alpha=0.2, padding=(10, 10, 10, 10))
        new_txt_box.add_widget(txt_label)
        self.ids.stackLayout.add_widget(new_txt_box)
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
