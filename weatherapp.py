#weatherapp
# we want this program to run on windows too!!
import requests
import json
import os
city = input("Enter the city name : \n")
url = f'http://api.weatherapi.com/v1/current.json?key=c798733495ea461ead0135236240801&q={city}'
r =requests.get(url)
#print(r.text)
wdic = json.loads(r.text)
w = wdic['current']['temp_c']
print(w)
os.system(f'say temperature in {city} is {w} degree celcius')
