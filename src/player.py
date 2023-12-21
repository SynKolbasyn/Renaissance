import json
import os.path

import aiogram


class Player:
    def __init__(self, player: aiogram.types.User):
        self.player_id = player.id
        self.first_name = player.first_name
        self.last_name = player.last_name
        self.username = player.username

        data = self.load_data()
        self.money = data["money"]
        self.exp = data["exp"]

    def load_data(self) -> dict:
        zero_player = json.load(open(f"../players_data/0.json", "r", encoding="utf-8"))
        if not os.path.exists(f"../players_data/{self.player_id}.json"):
            return zero_player

        data = json.load(open(f"../players_data/{self.player_id}.json", "r", encoding="utf-8"))
        for i in zero_player:
            if i not in data.keys():
                data[i] = zero_player[i]
        return data

    def save_data(self):
        json.dump(
            self.__dict__,
            open(f"../players_data/{self.player_id}.json", "w", encoding="utf-8"),
            ensure_ascii=False,
            indent=2
        )

    def process_message(self, message: str) -> str:
        self.save_data()
        return message
