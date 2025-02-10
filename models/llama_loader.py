import os
import ollama
from models.model_loader import AIModel


class LlamaLoader(AIModel):

    def __init__(self, model):
        super().__init__(model)
        self.ollama_url = os.getenv("OLLAMA_URL")
        self.model = os.getenv("LLAMA_MODEL")
        self.ollama = self.load_model()

    def load_model(self):
        return ollama

    def summarize(self, website):
        response = self.ollama.chat(model=self.model, messages=self.messages_for(website))
        return response['message']['content']
