import aiogram

import player


def process_message(message: aiogram.types.Message) -> str:
    p = player.Player(message.from_user)
    return p.process_message(message.text)
