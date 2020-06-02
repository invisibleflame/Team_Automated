# TOKEN = '1123378208:AAFnDmS4CA5aRsJYHYfvm8e-s_E6YIRYxxo'
TOKEN = '1237103929:AAH-UDwFKEuS_NlZGJifnv2tavcTXsF0gg4'
import telegram
import time
# import RPi.GPIO as GPIO
import csv
import datetime
import smtplib
from email.message import EmailMessage

bot = telegram.Bot(TOKEN)
print(bot.get_me())
bot = telegram.Bot(TOKEN)
i = 0
prevmessage = 'dds'
ids = {}
fan=10
lights=10
def save_pass_to_file(pas):
    f = open('r.txt', 'w')
    f.write(str(pas))
    f.close()


def load_pass_from_file():
    f = open('r.txt', 'r')
    dat = f.read()
    f.close()
    return dat
password=load_pass_from_file()


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

    if 'hi' in recentmessage.lower():
        ref = "Hello, how can I help you"
        bot.send_message(chat_id, ref)

    elif 'hello' in recentmessage.lower():
        ref = 'Hello, how can I help you'
        bot.send_message(chat_id, ref)

    elif 'bye' in recentmessage.lower():
        ref = "See you again"
        bot.send_message(chat_id, ref)

    elif 'do' in recentmessage.lower():
        if 'what' in recentmessage.lower():
            ref = "I can help you turn on / off your devices. Enter the command and the name of device "
            bot.send_message(chat_id, ref)
        elif 'can' in recentmessage.lower():
            ref = "I can help you turn on / off your devices. Enter the command and the name of device "
            bot.send_message(chat_id, ref)
        continue
    elif 'password' in recentmessage.lower():
        if 'change' or 'new' in recentmessage.lower():
            password_check(-1)
            bot.send_message(chat_id, "Please enter the new password ")
            uf = bot.get_updates()
            mesge = [u.message.text for u in uf]
            password=mesge[-1]

            prevmessage=mesge[-1]
            save_pass_to_file(password)

            #send email
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
            <p class="second-head" style="font-size: 30px;        font-weight: bold;        color: red;">An importand mail from SASHA.</p>
            <p class="content" style="  font-size: 20px;        color: wheat;"> The password for SASHA is changed to {password} by {name} at {datetime.datetime.now()}. </p>
             </div>
            <div class="footer" style=" text-align: center;    color: black;">
            This is a auto-generated mail. Do not reply to this thread. <br>
            Copyright &copy; SASHA, Team_Automated, 2020.
            </div>
            </body>
            </html>
            """, subtype='html')

            server.login("team.automatediitb@gmail.com", "SASHAsasha")
            server.send_message(msg)
            server.quit()
            continue

    else:
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
                if lights==1:
                    bot.send_message(chat_id, "Lights are already ON!!")
                else:
                    # GPIO.output(led, 1)
                    bot.send_message(chat_id, ref)
                    lights=1
                continue

            if 'fan' in recentmessage.lower():
                ref = ref + "fan" + ", Task Completed!!"
                if fan == 1:
                    bot.send_message(chat_id, "Fan is already ON!!")
                else:
                    # GPIO.output(led, 1)
                    bot.send_message(chat_id, ref)
                    fan=1
                continue

            if 'light' in recentmessage.lower():
                ref = ref + "light" + ", Task Completed!!"
                if lights == 1:
                    bot.send_message(chat_id, "Lights are already ON!!")
                else:
                    # GPIO.output(led, 1)
                    bot.send_message(chat_id, ref)
                    lights=1
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
                    lights=0
                continue

            if 'fan' in recentmessage.lower():
                ref = ref + "fan" + ", Task Completed!!"
                if fan == 0:
                    bot.send_message(chat_id, "Fan is already OFF!!")
                    print(456)
                else:
                    # GPIO.output(led, 1)
                    bot.send_message(chat_id, ref)
                    fan=0
                continue

            if 'light' or 'lights' in recentmessage.lower():
                ref = ref + "light" + ", Task Completed!!"
                if lights == 0:
                    bot.send_message(chat_id, "Lights are already OFF!!")
                else:
                    # GPIO.output(led, 1)
                    bot.send_message(chat_id, ref)
                    lights=0
                continue
            else:
                bot.send_message(chat_id, "Invalid command, please try again and specify the appliance properly!")

        else:
            bot.send_message(chat_id, "INVALID COMMAND! TRY AGAIN")

        time.sleep(4)
