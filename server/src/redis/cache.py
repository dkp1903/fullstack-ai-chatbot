from rejson import Path


class Cache:
    def __init__(self, json_client):
        self.json_client = json_client

    def get_chat_history(self, token: str):
        print("st")
        data = self.json_client.jsonget(
            str(token), Path.rootPath())

        return data
