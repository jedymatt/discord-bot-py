import json
from cogs.utils import api


class Character:
    _url = '/api/characters'

    def __init__(self, discord_id, level, exp, money, location=None) -> None:
        self.discord_id = discord_id
        self.level = level
        self.exp = exp
        self.money = money
        self.location = location

    @classmethod
    def find_by_discord_id(cls, discord_id: int):
        response = api.get_request(
            f'{cls._url}?filters[discordId][$eq]={discord_id}'
        )
    
        print(response.json())
        data: dict = response.json()['data'] or []

        if len(data) == 0:
            return cls(discord_id, 1, 0, 0)

        attributes = data[0]['attributes']

        return cls(
            discord_id=attributes['discordId'],
            level=attributes['level'],
            exp=attributes['exp'],
            money=attributes['money'],
        )

    def all():
        pass
