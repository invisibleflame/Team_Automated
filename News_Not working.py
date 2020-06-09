from newsapi import NewsApiClient
from gtts import gTTS


newsapi = NewsApiClient(api_key='1cec50aadff94c538a68e0d626bdb1f4')

all_articles = newsapi.get_everything(q='fiction', sources='the-times-of-india', sort_by='relevancy')
results=[]
for i in range(10):
    results.append(all_articles['articles'][i]['title'])

text=f'''1. {results[0]}
2. {results[1]}
3. {results[2]}
4. {results[3]}
5. {results[4]}
6. {results[5]}
7. {results[6]}
8. {results[7]}
9. {results[8]}
10. {results[9]}'''
language='en'
myobj = gTTS(text=text, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
myobj.save("welcome.mp3")
print(text)