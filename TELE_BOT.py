TOKEN = '1123378208:AAFnDmS4CA5aRsJYHYfvm8e-s_E6YIRYxxo'
import telegram
import time

# import RPi.GPIO as GPIO

bot = telegram.Bot(TOKEN)
print(bot.get_me())
bot = telegram.Bot(TOKEN)
i = 0
prevmessage = 'dds'
ids = {}

password = "freshies"


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
    q=t
    g=0
    while (True):

        updates = bot.get_updates()
        message = [u.message.text for u in updates]
        chat_id = bot.get_updates()[-1].message.chat_id
        prevmessage=''
        while (q < 1):  # first time initialize
            prevmessage = message[-1]
            q = q + 1


        if (message[-1] == prevmessage):  # to prevent it from sending messages even if
            continue
        else:
            prevmessage = message[-1]
        chat_id = bot.get_updates()[-1].message.chat_id
        bot.send_message(chat_id, "Enter Password")
        time.sleep(10)
        ud = bot.get_updates()
        mesage = [u.message.text for u in ud]
        if mesage[-1] == password:
            bot.send_message(chat_id, "Password Accepted! Enter your command")
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
        bot.send_message(chat_id, "Hi {}! Enter Your command!".format(naam))
        time.sleep(15)
        continue

    name = get_key(chat_id)
    text = "Hi {}! Your command is loading please wait!".format(name)
    bot.send_message(chat_id, text)
    time.sleep(3)

    if 'on' in recentmessage.lower():
        ref = "Turned on "
        if 'led' in recentmessage.lower():
            ref = ref + "led" + ", Task Completed!!"
            # GPIO.output(led, 1)
            bot.send_message(chat_id, ref)
            continue

        if 'fan' in recentmessage.lower():
            ref = ref + "fan" + ", Task Completed!!"
            # GPIO.output(fan, 1)
            bot.send_message(chat_id, ref)
            continue

        if 'light' in recentmessage.lower():
            ref = ref + "light" + ", Task Completed!!"
            # GPIO.output(led, 1)
            bot.send_message(chat_id, ref)
            continue
        else:
            bot.send_message(chat_id, "Invalid command, please try again and specify the appliance properly!")

    if 'off' in recentmessage.lower():
        ref = "Turned off "
        if 'led' in recentmessage.lower():
            ref = ref + "led" + ", Task Completed!!"
            # GPIO.output(led, 0)
            bot.send_message(chat_id, ref)
            continue

        if 'fan' in recentmessage.lower():
            ref = ref + "fan" + ", Task Completed!!"
            # GPIO.output(fan, 0)
            bot.send_message(chat_id, ref)
            continue

        if 'light' in recentmessage.lower():
            ref = ref + "light" + ", Task Completed!!"
            # GPIO.output(led, 0)
            bot.send_message(chat_id, ref)
            continue
        else:
            bot.send_message(chat_id, "Invalid command, please try again and specify the appliance properly!")

    else:
        bot.send_message(chat_id, "INVALID COMMAND! TRY AGAIN")
    time.sleep(4)
