import config

import requests


class Session(requests.Session):
    def __init__(self) -> None:
        super().__init__()
        self.headers = {
            'Authorization': f'Bearer {config.API_TOKEN}',
        }

session = Session()
session.params = {}
