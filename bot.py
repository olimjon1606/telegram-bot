


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
