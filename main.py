import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
import requests
import geocoder


API_KEY = 'INSERTKEYHERE'
location = geocoder.ip('me')
city = location.city

database_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_KEY + "&q=" + city

#Backup database for weather codes to reduce future requests per minute
weatherCodes = {   
    200:  'Thunderstorm',#light rain
    201:  'Thunderstorm',#rain
    202:  'Thunderstorm',#heavy rain
    210:  'Thunderstorm',#light storm
    211:  'Thunderstorm',#regular storm
    212:  'Thunderstorm',#heavy storm
    221:  'Thunderstorm',#ragged storm
    230:  'Thunderstorm',#light drizzle
    231:  'Thunderstorm',#drizzle
    232:  'Thunderstorm',#heavy drizzle

    300:	'Drizzle',# light intensity drizzle
    301:	'Drizzle',# drizzle
    302:	'Drizzle',# heavy intensity drizzle
    310:	'Drizzle',# light intensity drizzle rain
    311:	'Drizzle',# drizzle rain
    312:	'Drizzle',# heavy intensity drizzle rain
    313:	'Drizzle',# shower rain and drizzle
    314:	'Drizzle',# heavy shower rain and drizzle
    321:	'Drizzle',# shower drizzle

    500:	'Rain',# light rain
    501:	'Rain',# moderate rain
    502:	'Rain',# heavy intensity rain
    503:	'Rain',# very heavy rain
    504:	'Rain',# extreme rain
    511:	'Rain',# freezing rain
    520:	'Rain',# light intensity shower rain
    521:	'Rain',# shower rain
    522:	'Rain',# heavy intensity shower rain
    531:	'Rain',# ragged shower rain

    600:	'Snow',# light snow
    601:	'Snow',# Snow
    602:	'Snow',# Heavy snow
    611:	'Snow',# Sleet
    612:	'Snow',# Light shower sleet
    613:	'Snow',# Shower sleet
    615:	'Snow',# Light rain and snow
    616:	'Snow',# Rain and snow
    620:	'Snow',# Light shower snow
    621:	'Snow',# Shower snow
    622:	'Snow',# Heavy shower snow

    701:	'Mist',   #	mist
    711:    'Smoke',  #	Smoke
    721:	'Haze',   #	Haze
    731:	'Dust',   #	sand/ dust whirls
    741:	'Fog',    #	fog
    751:	'Sand',   #	sand
    761:	'Dust',   #	dust
    762:	'Ash',    #	volcanic ash
    771:	'Squall', #	squalls
    781:	'Tornado',#	tornado

    800:	'Clear', # clear sky
    801:	'Clouds',# few clouds: 11-25%
    802:	'Clouds',# scattered clouds: 25-50%
    803:	'Clouds',# broken clouds: 51-84%
    804:	'Clouds' # overcast clouds: 85-100%
    }



kivy.require('1.9.0') #Using 1.9.0 as a test version as it is compatible with older devices but can upgrade to 2.0.0 for newer Android versions

class MyRoot(BoxLayout):
    currTemp = 0

    def __init__(self):
        super(MyRoot, self).__init__()

    def getWeather(self):
        weather_data = requests.get(database_url).json()
        weather_code = weather_data['weather'][0]['id']

        self.weatherIcon.source = 'https://openweathermap.org/img/wn/'+ str(weather_data['weather'][0]['icon']) + '@2x.png'

        currTemp = kelvinToFarenheit(weather_data['main']['temp']) #Converting kelvin temp to celsius

        self.temperature.text = str(currTemp) + "°F" #Updating current temperature label
        self.weatherLabel.text = weatherCodes[weather_code]

class RainyDay(App):

    def build(self):#return the UI
        return MyRoot()

#This function converts Kelvin temperature to Celsius
#Returns Celsius temperature
def kelvinToCelsius(temperature):
    temperature -= 273.15
    temperature = round(temperature, 2)
    return temperature


#This function converts Kelvin temperature to Farenheit
#Returns Farenheit temperature
def kelvinToFarenheit(temperature):
    temperature = temperature * (9/5) - 459.67
    temperature = round(temperature, 2)
    return temperature
    




rainyDay = RainyDay()
rainyDay.run()
