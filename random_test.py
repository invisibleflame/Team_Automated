#
# def save_pass_to_file(dic):
#     f = open('r.txt', 'w')
#     f.write(str(dic))
#     f.close()
#
#
# def load_pass_from_file():
#     f = open('r.txt', 'r')
#     data = f.read()
#     f.close()
#     return data
#
# save_pass_to_file("text")
# password=load_pass_from_file()
# if lil=="text":
#     print(453)

# import smtplib
# from email.message import EmailMessage
# import datetime
# server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
# msg=EmailMessage()
# contacts=['bhuvanaggarwal9@gmail.com']
# msg['Subject']="Password Change Detected!!"
# msg['From']="team.automatediitb@gmail.com"
# msg['To']=contacts
# #msg.set_content('The password was changed')
# msg.add_alternative(f"""\
# <!DOCTYPE html>
# <html>
#     <body>
#         <h1 style="color:SlateGray; font-style:"bold"; font-family:"Comic Sans MS", cursive, sans-serif;"> {datetime.datetime.now()} is an HTML Email!</h1>
#     </body>
# </html>
# """, subtype='html')
#
# server.login("team.automatediitb@gmail.com", "SASHAsasha")
# server.send_message(msg)
# server.quit()
import string

# def find_substring(needle, haystack):
#   search_start = 0
#   while (search_start < len(haystack)):
#     index = haystack.find(needle, search_start)
#     if index == -1:
#       return False
#     is_prefix_whitespace = (index == 0 or haystack[index-1] in string.whitespace)
#     search_start = index + len(needle)
#     is_suffix_whitespace = (search_start == len(haystack) or haystack[search_start] in string.whitespace)
#     if (is_prefix_whitespace and is_suffix_whitespace):
#       return True
#   return False

# def find_substring(ssub_string, sstring):
#     search_start = 0
#     while (search_start < len(sstring)):
#       index = sstring.find(ssub_string, search_start)
#       if index == -1:
#         return False
#       is_prefix_whitespace = (index == 0 or sstring[index - 1] in string.whitespace)
#       search_start = index + len(ssub_string)
#       is_suffix_whitespace = (search_start == len(sstring) or sstring[search_start] in string.whitespace)
#       if (is_prefix_whitespace and is_suffix_whitespace):
#         return True
#     return False
#
#
# string1 = "on"
# string2 = "Fan on"
# print (find_substring("on", string2.lower()))
# print (find_substring("a", 'a b'))
# print (find_substring('b', 'a b'))
#
#
# string1 = "ADVANCE"
# string2 = "ADVANCED BUSINESS EQUIPMENT LTD"
# print (find_substring(string1, string2))
# print (find_substring('a', 'ab'))
# print (find_substring('b', 'ab'))


home1={"room1": [2,1,1,1], "room2": [1,1,1,0], "room3":[1,1,1,1]}
for key in home1:

    for i in range(1,home1[key][0] + 1):
        exec(f'{key}_light_{i} = 10')

    for o in range(home1[key][1]):
        exec(f'{key}_fan_{o} = 10')
    for p in range(home1[key][2]):
        exec (f'{key}_AC_{p} = 10')
    for u in range(home1[key][3]):
        exec (f'{key}_TV_{u} = 10')

try:
    print(room1_light_1)
    if room1_light_1 or room2_light_5 or room1_light_2 :
        print("lol1")
    if room1_fan_0:
        print("lol2")
    print(room1_light_2)


except: print("lol")