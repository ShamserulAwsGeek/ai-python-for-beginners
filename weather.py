import requests

url = 'http://api.weatherapi.com/v1/current.json?key=d801ce183c514fa8ae7122728252906&q=Bengaluru&aqi=no'

response = requests.get(url)

weather_json = response.json()

temp = weather_json.get('current').get('temp_c')

description = weather_json.get('current').get('condition').get('text')

print("Todays's weather in Bengaluru is ", description , temp, 'degress' )