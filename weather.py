import requests

url='http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=3c44c91488c5b35ec2dc81d21cbc95ae'
json_data=requests.get(url).json()

# formatted_data= json_data['weather'][0]['main'] for just weather title
formatted_data= [ json_data['weather'][0]['description'],json_data['main']['temp'], json_data['main']['pressure'], json_data['main']['humidity'], "dsf" ,json_data['wind']['speed']]
# this for weather discription
city_list=["delhi", "mumbai", "chandigarh", "panchkula", "jaipur", "kanpur", "chennai", "kolkata", "amritsar", "meerut", "srinagar", "lucknow", "gwalior", "gurgaon", "nagpur", "srinagar", "pune", "kurukshetra", ""]
city_lists=[
"mumbai",
"delhi",
"bangalore",
"hyderabad",
"ahmedabad",
"chennai",
"kolkata",
"surat",
"pune",
"jaipur",
"visakhapatnam","nagpur","lucknow","kanpur","thane","bhopal","indore","pimpri-chinchwad","patna","vadodara","ghaziabad"
"ludhiana",
"agra","nashik","faridabad","meerut",]
print(json_data)
lol=f'''Current weather conditons in {city}:
Cloudiness: {formatted_data[0]}
Temperature: {formatted_data[1]} K
Pressure: {formatted_data[2]} hpa
Humidity: {formatted_data[3]} %
Windspeed: {formatted_data[5]} m/s'''
print(lol)