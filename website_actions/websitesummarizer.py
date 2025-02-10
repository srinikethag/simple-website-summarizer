import requests
from bs4 import BeautifulSoup


class WebsiteSummarizer:

    def __init__(self, url, model):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/117.0.0.0 Safari/537.36"
        }
        self.model = model
        self.messages = [
            {"role": "system", "content": "You are a snarky assistant"},
            {"role": "user", "content": "What is 2 + 2?"}
        ]

    def extract_website_data(self):
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
        return {
            "title": title,
            "text": text
        }

    def summarize_website(self):
        """Extracts website content and uses AI to summarize it."""
        website_data = self.extract_website_data()
        summary = self.model.summarize(website_data)
        return summary
