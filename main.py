import os
from dotenv import load_dotenv
from website_actions.websitesummarizer import WebsiteSummarizer
from models.model_factory import get_model

if __name__ == '__main__':
    load_dotenv(override=True)
    model_type = os.getenv("USE_MODEL")
    url = os.getenv("URL")

    model_instance = get_model(model_type)

    summarizer = WebsiteSummarizer(url, model_instance)

    print(summarizer.summarize_website())
