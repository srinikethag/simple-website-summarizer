import os
from openai import OpenAI
from models.model_loader import AIModel


class OpenAiLoader(AIModel):

    def __init__(self, model):
        super().__init__(model)
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.openai = self.load_model()
        self.gpt_model = os.getenv("GPT_MODEL")

    def load_model(self):
        openai = OpenAI()
        return openai

    def summarize(self, website):
        response = self.openai.chat.completions.create(
            model=self.gpt_model,
            messages=self.messages_for(website)
        )
        return response.choices[0].message.content
