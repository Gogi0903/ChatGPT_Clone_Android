import openai
from kivy.app import App
from kivy.core.window import Window
from Custom_Layouts import BgBoxLayout

Window.size = (540, 800)

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

    def msg_to_chatgpt(self):
        current_question = self.question()
        self.ids.conversation.text += f"- Én:\n{current_question}\n\n"
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
        self.ids.conversation.text += f"- ChatGPT:\n{current_response}\n\n"


class CloneTestApp(App):
    ...


if __name__ == '__main__':
    CloneTestApp().run()
