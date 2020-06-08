import requests
city='Mumbai'
url='http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=3c44c91488c5b35ec2dc81d21cbc95ae'
json_data=requests.get(url).json()

# formatted_data= json_data['weather'][0]['main'] for just weather title
formatted_data= json_data['weather'][0]['description']
# this for weather discription
print(formatted_data)
