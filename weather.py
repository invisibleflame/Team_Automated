import requests
city='Mumbai'
url='http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=3c44c91488c5b35ec2dc81d21cbc95ae'
json_data=requests.get(url).json()

# formatted_data= json_data['weather'][0]['main'] for just weather title
formatted_data= [ json_data['weather'][0]['description'],json_data['main']['temp'], json_data['main']['pressure'], json_data['main']['humidity'], json_data['visibility'],json_data['wind']['speed']]
# this for weather discription
lol=f'''Current weather conditons in {city}:
Cloudiness: {formatted_data[0]}
Temperature: {formatted_data[1]} K
Pressure: {formatted_data[2]} hpa
Humidity: {formatted_data[3]} %
Visibility: {formatted_data[4]} m
Windspeed: {formatted_data[5]} m/s'''
print(lol)