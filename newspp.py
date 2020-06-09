import requests
from gtts import gTTS

def NewsFromBBC():
    # BBC news api
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"

    # fetching data in json format
    open_bbc_page = requests.get(main_url).json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will
    # contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])

        # to read the news out loud for us
    # from win32com.client import Dispatch
    # speak = Dispatch("SAPI.Spvoice")
    # speak.Speak(results)
    language = 'en'
    text=f'''{results[0]}..
{results[1]}..
{results[2]}..
{results[3]}..
{results[4]}..
{results[5]}..
{results[6]}..
{results[7]}..
{results[8]}..
{results[9]}'''
    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=text, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("welcome.mp3")

# Driver Code
    # function call
NewsFromBBC()