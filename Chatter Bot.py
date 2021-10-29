#!pip install chatterbot
#!pip install chatterbot-corpus

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import chatterbot
import chatterbot_corpus
bot = ChatBot('Bot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
            "statement_comparison_function": chatterbot.comparisons.levenshtein_distance,
            "response_selection_method": chatterbot.response_selection.get_first_response
        }
    ],
    trainer='chatterbot.trainers.ListTrainer')
trainer = ListTrainer(bot)

omkar1=["Hi",
"Hello, how are you ?",
        "I am happy",
"I am fine, what about you ?",
"I am fine too",
"What you think of life ?",
"Life is Beautiful",
"What is your name?",
"My name is SASHA",
"WHo created you ?",
"I was created by team Automated",
"What can you do",
"I can turn on your various devices such as fan, light,etc",
"Can I talk to you for long time",
"Yes you can talk to me for Long time",
"What our you?",
"I am a software cum Hardware combination for you betterment",
"What makes you different from others",
"I am more skilful than all others",
"Bye",
"Bye, It was great working for you"]

omkar2=["Hey",
"Hello, how are you ?",
"I am a little stressed, feeling sad",
"Just be patient, things will improve",
"Yes, thanks",
"Your's Welcome",
"Bye",
"Bye, It was great working for you"]

omkar3=["Hello",
"Hello, how it's going ?",
"Life is chill",
"Good to here",
"Where do you live ?",
"I live in ROM memory",
"Where are you from ?",
"I am from the world of great creativity for making world a Happy Space",
"Are you a Human?",
"No, I am not a Human...",
"Bye",
"Bye, It was great working for you"]

fhand1=open('conversations.yml').readlines()
fhand2=open('conversation.yml').readlines()
fhand3=open('Artificial_intelligence.yml').readlines()
fhand4=open('conversation.yml').readlines()
fhand5=open('emotion.yml').readlines()
fhand6=open('film.yml').readlines()
fhand7=open('food.yml').readlines()
fhand9=open('GK.yml').readlines()
fhand10=open('IT.yml').readlines()
fhand11=open('jokes_fun.yml').readlines()
fhand12=open('market_money.yml').readlines()
fhand13=open('psychology.yml').readlines()
fhand14=open('space_and_science.yml').readlines()
fhand15=open('Sport_games.yml').readlines()

trainer.train(fhand1)
trainer.train(fhand2)
trainer.train(fhand3)
trainer.train(fhand4)
trainer.train(fhand5)
trainer.train(fhand6)
trainer.train(fhand7)
trainer.train(fhand9)
trainer.train(fhand10)
trainer.train(fhand11)
trainer.train(fhand12)
trainer.train(fhand13)
trainer.train(fhand14)
trainer.train(fhand15)
trainer.train(omkar1)
trainer.train(omkar2)
trainer.train(omkar3)

while True :
  user_input = input()
  bot_response = bot.get_response(user_input)
  print(bot_response)
