import unittest

import aiogram

import src.player as player


class MyTestCase(unittest.TestCase):
    def test_start(self):
        self.assertEqual(
            player.Player(
                aiogram.types.Message(
                    chat=aiogram.types.Chat(id=1234567890, type="text"),
                    date=10,
                    message_id=1234567890,
                    from_user=aiogram.types.User(first_name="zero", id=0, is_bot=False)
                ).from_user
            ).process_message("hi"),
            "hi"
        )


if __name__ == "__main__":
    unittest.main()
