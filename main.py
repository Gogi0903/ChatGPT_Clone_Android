import openai
from kivy.app import App
from kivy.clock import Clock
from custom_layouts import BgBoxLayout


file = "./key.txt"


class Interface(BgBoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.questions = list()
        self.bot_responses = list()
        self.messages = list()
        system_prompt = 'Answer as concisely as possible in hungarian language.'
        self.messages.append({'role': 'system', 'content': system_prompt})
        Clock.schedule_once(self.set_conversation_readonly, 0.1)

    def set_conversation_readonly(self, dt):
        # a párbeszédablakot csak olvashatóra állítja
        self.ids.conversation.readonly = True

    @staticmethod
    def openai_authenticate(keyfile):
        # az API key-t olvassa ki egy külön txt fileból
        with open(keyfile) as f:
            api_key = f.read().strip('\n')
            assert api_key.startswith('sk-')
        openai.api_key = api_key

    openai_authenticate(file)

    def question(self):
        # a szövegmezőbe írt text-et adja vissza
        question = self.ids.input_text.text
        self.ids.input_text.text = str()
        return question

    def users_msg(self):
        # a user kérdését kiírja a képernyőre és a GPTnek küldendő csomaghoz adja
        current_question = self.question()
        self.ids.conversation.text += (f"Én:\n- {current_question}"
                                       f"\n______________________\n")
        self.messages.append({'role': 'user', 'content': current_question})
        self.questions.append(current_question)

    def chatgpt_msg(self, dt):
        # elküldi a GPT-nek szánt csomagot és kiírja a választ a képernyőre
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=self.messages,
            temperature=0.7,
            max_tokens=2000
        )
        current_response = response.choices[0]['message']['content']
        self.bot_responses.append(current_response)
        self.messages.append({'role': 'assistant', 'content': current_response})
        self.ids.conversation.text += (f"ChatGPT:\n- {current_response}"
                                       f"\n______________________\n")

    def msg_to_chatgpt(self):
        # ez a function késlelteti a GPT válaszát, így a két fél szövege egymás után jelenik meg és nem egyszerre
        self.users_msg()
        Clock.schedule_once(self.chatgpt_msg, 1)


class CloneTestApp(App):
    ...


if __name__ == '__main__':
    CloneTestApp().run()
