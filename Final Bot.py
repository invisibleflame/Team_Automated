# TOKEN = '1123378208:AAFnDmS4CA5aRsJYHYfvm8e-s_E6YIRYxxo'
TOKEN = '1237103929:AAH-UDwFKEuS_NlZGJifnv2tavcTXsF0gg4'
import telegram
import time
import random
# import RPi.GPIO as GPIO
import csv
import datetime
import smtplib
from email.message import EmailMessage
from newsapi import NewsApiClient
import requests
from gtts import gTTS
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.response_selection import get_first_response

cbot = ChatBot('cBot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': "chatterbot.logic.BestMatch",
            'statement_comparison_function': 'chatterbot.comparisons.levenshtein_distance',
            'response_selection_method': get_first_response
        }
    ],
    trainer='chatterbot.trainers.ListTrainer')
trainer = ListTrainer(cbot)

omkar1=["Hi",
"Hello, how are you ?",
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

omkar4=["Hi there",
"Hello, how it's going?",
"A bit sad and worried",
"Just be patient, things will improve",
"Can I ask you a Question?",
"What is your Question",
"In which country do you live",
"I was made in India"]

fhand1=open('my-data/conversation.yml').readlines()
fhand2=open('my-data/conversation.yml').readlines()
fhand3=open('my-data/Artificial_intelligence.yml').readlines()
fhand4=open('my-data/conversation.yml').readlines()
fhand5=open('my-data/emotion.yml').readlines()
fhand6=open('my-data/film.yml').readlines()
fhand7=open('my-data/food.yml').readlines()
fhand9=open('my-data/GK.yml').readlines()
fhand10=open('my-data/IT.yml').readlines()
fhand11=open('my-data/jokes_fun.yml').readlines()
fhand12=open('my-data/market_money.yml').readlines()
fhand13=open('my-data/psychology.yml').readlines()
fhand14=open('my-data/space_and_science.yml').readlines()
fhand15=open('my-data/Sport_games.yml').readlines()

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
trainer.train(omkar4)

newsapi = NewsApiClient(api_key='1cec50aadff94c538a68e0d626bdb1f4')



jokes_list=["Q: What’s the difference between England and a tea bag? "
            "A: The tea bag stays in the cup longer.",
            "A dyslexic man walks into a bra.",
            "A man walks into a bar with a roll of tarmac under his arm and says: “Pint please… and one for the road.",
            "I went to the doctor the other day and said: “Have you got anything for wind?” So he gave me a kite.",
            "I went to the zoo the other day. There was only a dog in it – it was a shihtzu.",
            "Two fish in a tank. One says: “How do you drive this thing?”",
            "A woman gets on a bus with her baby.   The driver says “Ugh – that’s the ugliest baby I’ve ever seen!”   "
            "The woman walks to the back of the bus and sits down."
            " She says to the man next to her: “The driver just insulted me!”"
            "The man says: “You go up there and tell him off. Go on. I’ll hold your monkey for you.",
            "Two men walk into a bar.   The third one DUCKS",
            "Why was six afraid of 7?   Because 7 ate 9",
            "You can't trust atoms! They make up everything.",
            "Why do potatoes argue?  Because they can't see eye to eye!",
            "Did u get a haircut? No I got them all cut!",
            "Why did the cat run away from the tree? because it was afraid of the bark!",
            "Why don't eggs tell each other jokes?   Because they would crack each other up!"]
city_list=['port blair', 'andhra pradesh', 'adoni', 'amaravati', 'anantapur', 'chandragiri', 'chittoor', 'dowlaiswaram', 'eluru', 'guntur', 'kadapa', 'kakinada', 'kurnool', 'machilipatnam', 'nagarjunako??a', 'rajahmundry', 'srikakulam', 'tirupati', 'vijayawada', 'visakhapatnam', 'vizianagaram', 'yemmiganur', 'arunachal pradesh', 'itanagar', 'assam', 'dhuburi', 'dibrugarh', 'dispur', 'guwahati', 'jorhat', 'nagaon', 'sibsagar', 'silchar', 'tezpur', 'tinsukia', 'bihar', 'ara', 'baruni', 'begusarai', 'bettiah', 'bhagalpur', 'bihar sharif', 'bodh gaya', 'buxar', 'chapra', 'darbhanga', 'dehri', 'dinapur nizamat', 'gaya', 'hajipur', 'jamalpur', 'katihar', 'madhubani', 'motihari', 'munger', 'muzaffarpur', 'patna', 'purnia', 'pusa', 'saharsa', 'samastipur', 'sasaram', 'sitamarhi', 'siwan', 'chandigarh (union territory)', 'chandigarh', 'chhattisgarh', 'ambikapur', 'bhilai', 'bilaspur', 'dhamtari', 'durg', 'jagdalpur', 'raipur', 'rajnandgaon', 'dadra and nagar haveli (union territory)', 'silvassa', 'daman and diu (union territory)', 'daman', 'diu', 'delhi (national capital territory)', 'delhi', 'new delhi', 'goa', 'madgaon', 'panaji', 'gujarat', 'ahmadabad', 'amreli', 'bharuch', 'bhavnagar', 'bhuj', 'dwarka', 'gandhinagar', 'godhra', 'jamnagar', 'junagadh', 'kandla', 'khambhat', 'kheda', 'mahesana', 'morvi', 'nadiad', 'navsari', 'okha', 'palanpur', 'patan', 'porbandar', 'rajkot', 'surat', 'surendranagar', 'valsad', 'veraval', 'haryana', 'ambala', 'bhiwani', 'chandigarh', 'faridabad', 'firozpur jhirka', 'gurgaon', 'hansi', 'hisar', 'jind', 'kaithal', 'karnal', 'kurukshetra', 'panipat', 'pehowa', 'rewari', 'rohtak', 'sirsa', 'sonipat', 'himachal pradesh', 'bilaspur', 'chamba', 'dalhousie', 'dharmshala', 'hamirpur', 'kangra', 'kullu', 'mandi', 'nahan', 'shimla', 'una', 'jammu and kashmir', 'anantnag', 'baramula', 'doda', 'gulmarg', 'jammu', 'kathua', 'leh', 'punch', 'rajauri', 'srinagar', 'udhampur', 'jharkhand', 'bokaro', 'chaibasa', 'deoghar', 'dhanbad', 'dumka', 'giridih', 'hazaribag', 'jamshedpur', 'jharia', 'rajmahal', 'ranchi', 'saraikela', 'karnataka', 'badami', 'ballari', 'bangalore', 'belgavi', 'bhadravati', 'bidar', 'chikkamagaluru', 'chitradurga', 'davangere', 'halebid', 'hassan', 'hubballi-dharwad', 'kalaburagi', 'kolar', 'madikeri', 'mandya', 'mangaluru', 'mysuru', 'raichur', 'shivamogga', 'shravanabelagola', 'shrirangapattana', 'tumkuru', 'kerala', 'alappuzha', 'badagara', 'idukki', 'kannur', 'kochi', 'kollam', 'kottayam', 'kozhikode', 'mattancheri', 'palakkad', 'thalassery', 'thiruvananthapuram', 'thrissur', 'madhya pradesh', 'balaghat', 'barwani', 'betul', 'bharhut', 'bhind', 'bhojpur', 'bhopal', 'burhanpur', 'chhatarpur', 'chhindwara', 'damoh', 'datia', 'dewas', 'dhar', 'guna', 'gwalior', 'hoshangabad', 'indore', 'itarsi', 'jabalpur', 'jhabua', 'khajuraho', 'khandwa', 'khargon', 'maheshwar', 'mandla', 'mandsaur', 'mhow', 'morena', 'murwara', 'narsimhapur', 'narsinghgarh', 'narwar', 'neemuch', 'nowgong', 'orchha', 'panna', 'raisen', 'rajgarh', 'ratlam', 'rewa', 'sagar', 'sarangpur', 'satna', 'sehore', 'seoni', 'shahdol', 'shajapur', 'sheopur', 'shivpuri', 'ujjain', 'vidisha', 'maharashtra', 'ahmadnagar', 'akola', 'amravati', 'aurangabad', 'bhandara', 'bhusawal', 'bid', 'buldana', 'chandrapur', 'daulatabad', 'dhule', 'jalgaon', 'kalyan', 'karli', 'kolhapur', 'mahabaleshwar', 'malegaon', 'matheran', 'mumbai', 'nagpur', 'nanded', 'nashik', 'osmanabad', 'pandharpur', 'parbhani', 'pune', 'ratnagiri', 'sangli', 'satara', 'sevagram', 'solapur', 'thane', 'ulhasnagar', 'vasai-virar', 'wardha', 'yavatmal', 'manipur', 'imphal', 'meghalaya', 'cherrapunji', 'shillong', 'mizoram', 'aizawl', 'lunglei', 'nagaland', 'kohima', 'mon', 'phek', 'wokha', 'zunheboto', 'odisha', 'balangir', 'baleshwar', 'baripada', 'bhubaneshwar', 'brahmapur', 'cuttack', 'dhenkanal', 'keonjhar', 'konark', 'koraput', 'paradip', 'phulabani', 'puri', 'sambalpur', 'udayagiri', 'puducherry (union territory)', 'karaikal', 'mahe', 'puducherry', 'yanam', 'punjab', 'amritsar', 'batala', 'chandigarh', 'faridkot', 'firozpur', 'gurdaspur', 'hoshiarpur', 'jalandhar', 'kapurthala', 'ludhiana', 'nabha', 'patiala', 'rupnagar', 'sangrur', 'rajasthan', 'abu', 'ajmer', 'alwar', 'amer', 'barmer', 'beawar', 'bharatpur', 'bhilwara', 'bikaner', 'bundi', 'chittaurgarh', 'churu', 'dhaulpur', 'dungarpur', 'ganganagar', 'hanumangarh', 'jaipur', 'jaisalmer', 'jalor', 'jhalawar', 'jhunjhunu', 'jodhpur', 'kishangarh', 'kota', 'merta', 'nagaur', 'nathdwara', 'pali', 'phalodi', 'pushkar', 'sawai madhopur', 'shahpura', 'sikar', 'sirohi', 'tonk', 'udaipur', 'sikkim', 'gangtok', 'gyalsing', 'lachung', 'mangan', 'tamil nadu', 'arcot', 'chengalpattu', 'chennai', 'chidambaram', 'coimbatore', 'cuddalore', 'dharmapuri', 'dindigul', 'erode', 'kanchipuram', 'kanniyakumari', 'kodaikanal', 'kumbakonam', 'madurai', 'mamallapuram', 'nagappattinam', 'nagercoil', 'palayankottai', 'pudukkottai', 'rajapalaiyam', 'ramanathapuram', 'salem', 'thanjavur', 'tiruchchirappalli', 'tirunelveli', 'tiruppur', 'tuticorin', 'udhagamandalam', 'vellore', 'telangana', 'hyderabad', 'karimnagar', 'khammam', 'mahbubnagar', 'nizamabad', 'sangareddi', 'warangal', 'tripura', 'agartala', 'uttar pradesh', 'agra', 'aligarh', 'amroha', 'ayodhya', 'azamgarh', 'bahraich', 'ballia', 'banda', 'bara banki', 'bareilly', 'basti', 'bijnor', 'bithur', 'budaun', 'bulandshahr', 'deoria', 'etah', 'etawah', 'faizabad', 'farrukhabad-cum-fatehgarh', 'fatehpur', 'fatehpur sikri', 'ghaziabad', 'ghazipur', 'gonda', 'gorakhpur', 'hamirpur', 'hardoi', 'hathras', 'jalaun', 'jaunpur', 'jhansi', 'kannauj', 'kanpur', 'lakhimpur', 'lalitpur', 'lucknow', 'mainpuri', 'mathura', 'meerut', 'mirzapur-vindhyachal', 'moradabad', 'muzaffarnagar', 'partapgarh', 'pilibhit', 'prayagraj', 'rae bareli', 'rampur', 'saharanpur', 'sambhal', 'shahjahanpur', 'sitapur', 'sultanpur', 'tehri', 'varanasi', 'uttarakhand', 'almora', 'dehra dun', 'haridwar', 'mussoorie', 'nainital', 'pithoragarh', 'west bengal', 'alipore', 'alipur duar', 'asansol', 'baharampur', 'bally', 'balurghat', 'bankura', 'baranagar', 'barasat', 'barrackpore', 'basirhat', 'bhatpara', 'bishnupur', 'budge budge', 'burdwan', 'chandernagore', 'darjiling', 'diamond harbour', 'dum dum', 'durgapur', 'halisahar', 'haora', 'hugli', 'ingraj bazar', 'jalpaiguri', 'kalimpong', 'kamarhati', 'kanchrapara', 'kharagpur', 'koch bihar', 'kolkata', 'krishnanagar', 'malda', 'midnapore', 'murshidabad', 'navadwip', 'palashi', 'panihati', 'purulia', 'raiganj', 'santipur', 'shantiniketan', 'shrirampur', 'siliguri', 'siuri', 'tamluk', 'titagarh']
topics=["current affairs",
        "tech", "food", "healthcare", "politics", "fiction",
        "bollywood", "books", "crime", "space", "religion",
        "geography", "history","general", "economy", "economics",
        "corona", "education", "movies", "movie", "international",
        "local", "sports", "music", "gadgets", "electronics", "business",
        "elections", "weather", "cities", "art", "weddings"]
bot = telegram.Bot(TOKEN)
print(bot.get_me())
bot = telegram.Bot(TOKEN)
i = 0
prevmessage = 'dds'
ids = {}
fan = 10
lights = 10


def save_pass_to_file(pas):
    f = open('r.txt', 'w')
    f.write(str(pas))
    f.close()


def load_pass_from_file():
    f = open('r.txt', 'r')
    dat = f.read()
    f.close()
    return dat


password = load_pass_from_file()


def save_dict_to_file(dic):
    f = open('dict.txt', 'w')
    f.write(str(dic))
    f.close()


def load_dict_from_file():
    f = open('dict.txt', 'r')
    data = f.read()
    f.close()
    return eval(data)


def get_key(val):
    for key, value in ids.items():
        if val == value:
            return key

    return "key doesn't exist"


text = ''

passed_ids = []


def password_check(t):
    q = t
    g = 0
    prevmessage = ''
    while (True):
        updates = bot.get_updates()
        message = [u.message.text for u in updates]
        chat_id = bot.get_updates()[-1].message.chat_id

        while (q < 1):  # first time initialize
            prevmessage = message[-1]
            q = q + 1

        if (message[-1] == prevmessage):  # to prevent it from sending messages even if user hasn't send any message
            continue
        else:
            prevmessage = message[-1]
        chat_id = bot.get_updates()[-1].message.chat_id
        bot.send_message(chat_id, "Enter Password")
        time.sleep(10)
        ud = bot.get_updates()
        mesage = [u.message.text for u in ud]
        if mesage[-1] == password:
            bot.send_message(chat_id, "Password Accepted!")
            passed_ids.append(chat_id)
            time.sleep(10)
            break

        else:
            bot.send_message(chat_id, "Incorrect Password! Try Again")
            prevmessage = "boom"
            g = g + 1
            if g > 10:
                prevmessage = message[-1]
            continue
    pass
def password_check_for_new(t):
    q = t
    g = 0
    prevmessage = ''
    while (True):
        updates = bot.get_updates()
        message = [u.message.text for u in updates]
        chat_id = bot.get_updates()[-1].message.chat_id

        while (q < 1):  # first time initialize
            prevmessage = message[-1]
            q = q + 1

        if (message[-1] == prevmessage):  # to prevent it from sending messages even if user hasn't send any message
            continue
        else:
            prevmessage = message[-1]
        chat_id = bot.get_updates()[-1].message.chat_id
        bot.send_message(chat_id, "Enter old Password")
        time.sleep(10)
        ud = bot.get_updates()
        mesage = [u.message.text for u in ud]
        if mesage[-1] == password:
            bot.send_message(chat_id, "Password Accepted!Enter new password")
            passed_ids.append(chat_id)
            time.sleep(10)
            break

        else:
            bot.send_message(chat_id, "Incorrect Password! Try Again")
            prevmessage = "boom"
            g = g + 1
            if g > 10:
                prevmessage = message[-1]
            continue
    pass


password_check(0)

while (True):
    ids = load_dict_from_file()
    updates = bot.get_updates()
    message = [u.message.text for u in updates]
    recentmessage = message[-1]
    # chat_id = bot.get_updates()[-1].message.chat_id
    # bot.send_message(chat_id, "sda")

    if message[-1] == prevmessage:
        continue
    else:
        prevmessage = message[-1]

    print(message)

    chat_id = bot.get_updates()[-1].message.chat_id
    if chat_id not in passed_ids:
        password_check(1)
        continue
    # bot.send_message(chat_id,"lod")

    if chat_id not in ids.values():
        bot.send_message(chat_id, "Please enter your full name")
        time.sleep(10)
        ud = bot.get_updates()
        mesage = [u.message.text for u in ud]
        naam = mesage[-1]
        ids[naam] = chat_id
        save_dict_to_file(ids)
        prevmessage = naam
        bot.send_message(chat_id, "Hi {}! How can I help you!".format(naam))
        time.sleep(15)
        continue

    # if 'hi' in recentmessage.lower():
    #     ref = "Hello, how can I help you"
    #     bot.send_message(chat_id, ref)
    #
    # elif 'hello' in recentmessage.lower():
    #     ref = 'Hello, how can I help you'
    #     bot.send_message(chat_id, ref)
    #
    # elif 'bye' in recentmessage.lower():
    #     ref = "See you again"
    #     bot.send_message(chat_id, ref)

    elif 'do' in recentmessage.lower():
        if 'what' in recentmessage.lower():
            ref = "I can help you turn on / off your devices. Enter the command and the name of device "
            bot.send_message(chat_id, ref)
        elif 'can' in recentmessage.lower():
            ref = "I can help you turn on / off your devices. Enter the command and the name of device "
            bot.send_message(chat_id, ref)
        continue
    elif 'password' in recentmessage.lower():
        if 'change' in recentmessage.lower():
            prevmessage = recentmessage
            password_check_for_new(1)
            #bot.send_message(chat_id, "Please enter the new password ")
            uf = bot.get_updates()
            mesge = [u.message.text for u in uf]
            password = mesge[-1]

            prevmessage = mesge[-1]
            save_pass_to_file(password)
            nm = get_key(chat_id)

            # send email
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            msg = EmailMessage()
            contacts = ['bhuvanaggarwal9@gmail.com', 'omkarghugarkar7@gmail.com', 'akshatszalte@gmail.com',
                        'divyansh.natani@gmail.com']
            msg['Subject'] = "Password Change Detected!!"
            msg['From'] = "team.automatediitb@gmail.com"
            msg['To'] = contacts
            # msg.set_content('The password was changed')
            msg.add_alternative(f"""\
            <!DOCTYPE html>
            <html>
            <body>
            <div class="pass-change" style="font-family:'Times New Roman', Times, serif;    background-color: rgb(31, 20, 20);    text-align: center;    border-radius: 10px;    padding: 10px;">
            <p class="header" style="font-family: Georgia, 'Times New Roman', Times, serif;        font-size: 40px;        font-weight: bold;            color: white;">Hello, Team Automated!!</p>
            <p class="second-head" style="font-size: 30px;        font-weight: bold;        color: red;">An important mail from SASHA.</p>
            <p class="content" style="  font-size: 20px;        color: wheat;"> The password for SASHA is changed to '{password}' by {nm} at {datetime.datetime.now()}. </p>
             </div>
            <div class="footer" style=" text-align: center;    color: black;">
            This is an auto-generated mail. Do not reply to this thread. <br>
            Copyright &copy; SASHA, Team_Automated, 2020.
            </div>
            </body>
            </html>
            """, subtype='html')

            server.login("team.automatediitb@gmail.com", "SASHAsasha")
            server.send_message(msg)
            server.quit()
            bot.send_message(chat_id, "Password changed successfully!! Please enter your command now!")
            continue
    elif 'weather' in recentmessage.lower():
        found=False
        for i in range(539):
            if city_list[i] in recentmessage.lower():
                city=city_list[i]
                found=True
                break
        if not found:
            bot.send_message(chat_id, "Please check the name of the city entered and try again")
            continue
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=3c44c91488c5b35ec2dc81d21cbc95ae'
        json_data = requests.get(url).json()

        # formatted_data= json_data['weather'][0]['main'] for just weather title
        formatted_data = [json_data['weather'][0]['description'], json_data['main']['temp'],
                          json_data['main']['pressure'], json_data['main']['humidity'], "dsf",
                          json_data['wind']['speed']]
        lol = f'''Current weather conditons in {city}:
        Cloudiness: {formatted_data[0]}
        Temperature: {formatted_data[1]} K
        Pressure: {formatted_data[2]} hpa
        Humidity: {formatted_data[3]} %
        Windspeed: {formatted_data[5]} m/s'''
        bot.send_message(chat_id, lol)
        continue

    elif "news" in recentmessage.lower():
        found = False
        for i in range(31):
            if topics[i] in recentmessage.lower():
                topic = topics[i]
                found = True
                break
        if not found:
            topic="current affairs"
        newsapi = NewsApiClient(api_key='1cec50aadff94c538a68e0d626bdb1f4')

        all_articles = newsapi.get_everything(topic, sources='the-times-of-india', sort_by='relevancy')
        results = []
        for i in range(10):
            results.append(all_articles['articles'][i]['title'])

        text = f'''Here is your news:
        1. {results[0]}
        2. {results[1]}
        3. {results[2]}
        4. {results[3]}
        5. {results[4]}
        6. {results[5]}
        7. {results[6]}
        8. {results[7]}
        9. {results[8]}
        10. {results[9]}'''
        language = 'en'
        myobj = gTTS(text=text, lang=language, slow=False)
        myobj.save("welcome.mp3")
        bot.send_message(chat_id, text)
        bot.send_audio(chat_id=chat_id, audio=open('welcome.mp3', 'rb'))
        continue
    elif "jokes" in recentmessage.lower() or "joke" in recentmessage.lower() or "humor" in recentmessage.lower() or "humour" in recentmessage.lower():
        random_joke=random.choice(jokes_list)
        bot.send_message(chat_id, random_joke)
        continue

    elif "on" in recentmessage.lower() or "off" in recentmessage.lower():
        name = get_key(chat_id)
        text = "Hi {}! Your command is loading please wait!".format(name)
        bot.send_message(chat_id, text)
        time.sleep(3)

        with open('log.csv', 'a+', newline='') as file:  # logging in csv
            writer = csv.writer(file)
            writer.writerow([name, message[-1], datetime.datetime.now()])

        if 'on' in recentmessage.lower():
            ref = "Turned on "
            if 'led' in recentmessage.lower():
                ref = ref + "led" + ", Task Completed!!"
                if lights == 1:
                    bot.send_message(chat_id, "Lights are already ON!!")
                else:
                    # GPIO.output(led, 1)
                    bot.send_message(chat_id, ref)
                    lights = 1
                continue

            if 'fan' in recentmessage.lower():
                ref = ref + "fan" + ", Task Completed!!"
                if fan == 1:
                    bot.send_message(chat_id, "Fan is already ON!!")
                else:
                    # GPIO.output(led, 1)
                    bot.send_message(chat_id, ref)
                    fan = 1
                continue

            if 'light' in recentmessage.lower():
                ref = ref + "light" + ", Task Completed!!"
                if lights == 1:
                    bot.send_message(chat_id, "Lights are already ON!!")
                else:
                    # GPIO.output(led, 1)
                    bot.send_message(chat_id, ref)
                    lights = 1
                continue
            else:
                bot.send_message(chat_id, "Invalid command, please try again and specify the appliance properly!")

        if 'off' in recentmessage.lower():
            ref = "Turned off "
            if 'led' in recentmessage.lower():
                ref = ref + "led" + ", Task Completed!!"
                if lights == 0:
                    bot.send_message(chat_id, "Lights are already OFF!!")
                else:
                    # GPIO.output(led, 1)
                    bot.send_message(chat_id, ref)
                    lights = 0
                continue

            if 'fan' in recentmessage.lower():
                ref = ref + "fan" + ", Task Completed!!"
                if fan == 0:
                    bot.send_message(chat_id, "Fan is already OFF!!")
                    print(456)
                else:
                    # GPIO.output(led, 1)
                    bot.send_message(chat_id, ref)
                    fan = 0
                continue

            if 'light' or 'lights' in recentmessage.lower():
                ref = ref + "light" + ", Task Completed!!"
                if lights == 0:
                    bot.send_message(chat_id, "Lights are already OFF!!")
                else:
                    # GPIO.output(led, 1)
                    bot.send_message(chat_id, ref)
                    lights = 0
                continue
            else:
                bot.send_message(chat_id, "Invalid command, please try again and specify the appliance properly!")

    else:
        user_input= recentmessage
        bot_response= str(cbot.get_response(user_input))
        bot.send_message(chat_id, bot_response)

        