import requests

class DiscordNotifier:
    def __init__(self, webhook) -> None:
        self.webhook = webhook
    
    def send(self, message: str):
        requests.post(self.webhook, data={"content": message})