import os
import telebot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer





# Set up the Telegram bot
my_secret = '6160231980:AAGz70x3VQqYgKnVgXGx6o3R5wZaJzdBBVs'
TOKEN = my_secret
bot = telebot.TeleBot(TOKEN)

# Set up the ChatBot
my_bot = ChatBot('MyBot')
trainer = ChatterBotCorpusTrainer(my_bot)



# Train the ChatBot with the English corpus
trainer.train("chatterbot.corpus.english")

# Export trained data
trainer.export_for_training('./mybot_corpus.json')

# Define the start function
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello there")

# Define the test function
@bot.message_handler(commands=['test'])
def test(message):
    bot.reply_to(message, "I am working as an AI")

# Define the function to handle incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Get the incoming message text
    message_text = message.text

    # Generate a response using the ChatBot
    response = my_bot.get_response(message_text)

    # Send the response back to the user
    bot.reply_to(message, str(response))

# Start the bot
bot.polling()
