import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# Your bot token
TOKEN = '5803187905:AAHIZObTimpE_Fgs80DHDgbC0-UFOrDEF8k'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def send_picture_with_caption(message: types.Message):
    # Get the argument from the command
    arg = message.get_args()

    # Construct the photo URL with the dynamic argument
    photo_url = f'https://source.unsplash.com/400x400/?nature,{arg}'

    # Caption text
    caption_text = 'Hello, this is the caption at the bottom!'

    # Send photo with caption
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo_url,
        caption=caption_text
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
