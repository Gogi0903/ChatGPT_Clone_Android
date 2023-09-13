import openai
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from Custom_Layouts import BgBoxLayout

Window.size = (480, 800)

file = "./key.txt"


class Interface(BgBoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.questions = list()
        self.bot_responses = list()
        self.messages = list()
        system_prompt = 'Answer as concisely as possible in hungarian language.'
        self.messages.append({'role': 'system', 'content': system_prompt})

    @staticmethod
    def openai_authenticate(keyfile):
        # az API key-t olvassa ki a txt file-ból
        with open(keyfile) as f:
            api_key = f.read().strip('\n')
            assert api_key.startswith('sk-')
        openai.api_key = api_key

    openai_authenticate(file)

    def question(self):
        # a szövegmezőbe írt text-et adja vissza, reseteli a text inputot
        question = self.ids.input_text.text
        self.ids.input_text.text = str()
        return question

    def add_textbox_to_scr(self, text_in):
        # az aktuális üzenetet írja ki a kijelzőre
        new_txt_box = BgBoxLayout(hex_code='#574bc9', alpha=0.2, size_hint=(.9, None),
                                  height=self.minimum_height)
        label = Label(text=text_in)
        new_txt_box.add_widget(label)
        self.ids.conversation.add_widget(new_txt_box)

    def msg_to_chatgpt(self):
        # a "küldés" gomb funkciója. Ez kommunikál a ChatGPT-vel, valamint naplózza a korábbi kérdéseket és válaszokat.
        current_question = self.question()
        self.add_textbox_to_scr(current_question)
        self.messages.append({'role': 'user', 'content': current_question})
        self.questions.append(current_question)
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=self.messages,
            temperature=0.7,
            max_tokens=2000
        )
        current_response = response.choices[0]['message']['content']
        self.bot_responses.append(current_response)
        self.messages.append({'role': 'assistant', 'content': current_response})
        self.add_textbox_to_scr(current_response)


class CloneTestApp(App):
    ...


if __name__ == '__main__':
    CloneTestApp().run()
