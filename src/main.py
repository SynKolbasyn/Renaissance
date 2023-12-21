import os
import logging
import asyncio

import aiogram

import router


dp = aiogram.Dispatcher()


@dp.message()
async def main_handler(message: aiogram.types.Message) -> None:
    answer = router.process_message(message)
    await message.reply(answer)


async def main() -> None:
    bot = aiogram.Bot(token=os.getenv("RENAISSANCE_TOKEN"))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s\t| %(message)s",
        handlers=[
            logging.FileHandler(filename="../logs/logs.log", mode="a"),
            logging.StreamHandler()
        ]
    )
    asyncio.run(main())
