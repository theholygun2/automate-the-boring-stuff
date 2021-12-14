#! python 3
# getOpenWeather.py - Prints the weather foar a location from the command line.

APPID = [youweathertoken]

import json,requests,sys

# Compute location from command line arguments .

if len(sys.argv)<2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ','.join(sys.argv[1:])

print(location)

'''Download the JSON Data'''
url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' %(location, APPID)

response = requests.get(url)
response.raise_for_status()

print(response.text)

#Load JSON data into a Python variable.
weatherData = json.loads(response.text)
w = weatherData['weather']

print()
print(weatherData.keys())

print('current weather in %s' %(location))
print()
print(w[0])
