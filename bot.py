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
import os
import openai
from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token = '5944753434:AAFVSXlqguHeo6fFWb8pNzIf8NZaGkJKWQA')
dp = Dispatcher(bot)

openai.api_key = "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"

@dp.message_handler(commands = ['start', 'help'])
async def welcome(message: types.Message):
  await message.reply('Hello! Im GPT chat bot. Ask me something')

@dp.message_handler()
async def gpt(message: types.Message):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  await message.reply(response.choices[0].text)

if __name__ == '__main__':
  executor.start_polling(dp)


import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from transformers import pipeline

# Replace YOUR_BOT_TOKEN with your actual bot token
bot = telegram.Bot(token='5944753434:AAFVSXlqguHeo6fFWb8pNzIf8NZaGkJKWQA')
updater = Updater(
    token='5944753434:AAFVSXlqguHeo6fFWb8pNzIf8NZaGkJKWQA', use_context=True)
dispatcher = updater.dispatcher

# Define a function for handling the /start command


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Hi! I'm ChatGPT, a language model trained by OpenAI. You can chat with me and I'll try to respond as best I can.")

# Define a function for handling text messages


def reply(update, context):
    chat_id = update.effective_chat.id
    text = update.message.text

    # Use the GPT-3.5 pipeline to generate a response
    gpt = pipeline('text-generation', model='openai/GPT3.5B', device=0)
    response = gpt(text, max_length=100)[0]['generated_text']

    # Send the response to the user
    context.bot.send_message(chat_id=chat_id, text=response)


# Add the command and message handlers to the dispatcher
start_handler = CommandHandler('start', start)
reply_handler = MessageHandler(Filters.text & (~Filters.command), reply)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(reply_handler)

# Start the bot
updater.start_polling()
