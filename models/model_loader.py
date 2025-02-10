from abc import ABC, abstractmethod
from dotenv import load_dotenv

from prompts.system_prompts import system_prompt


class AIModel(ABC):

    def __init__(self, model):
        load_dotenv(override=True)

    @abstractmethod
    def load_model(self):
        pass

    @abstractmethod
    def summarize(self, website):
        pass

    @staticmethod
    def user_prompt_for(website):
        user_prompt = f"You are looking at a website titled {website['title']}"
        user_prompt += "\nThe contents of this website is as follows; \
    please provide a short summary of this website in markdown. \
    If it includes news or announcements, then summarize these too.\n\n"
        user_prompt += website['text']
        return user_prompt

    def messages_for(self, website):
        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": self.user_prompt_for(website)}
        ]
