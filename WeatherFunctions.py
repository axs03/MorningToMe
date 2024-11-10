from datetime import datetime
from geopy.geocoders import Nominatim
import requests
import math


class WeatherFunctions:
    # used by geopy
    locator = Nominatim(user_agent="GetLoc")

    @staticmethod
    def kelvinToCelsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def kelvinToFahrenheit(kelvin):
        return (kelvin - 273.15) * (9 / 5) + 32

    @staticmethod
    def CtoF(celsius):
        return math.ceil((celsius * 9 / 5) + 32)

    @staticmethod
    def getCurrentLocation(location):
        getLocation = WeatherFunctions.locator.geocode(location)
        print(getLocation.address)
        print("Latitude = ", getLocation.latitude, "\n")
        print("Longitude = ", getLocation.longitude)
        return {"long": getLocation.latitude, "lat": getLocation.longitude}

    @staticmethod
    def getWeather():
        # extracting json from openWeather
        dataframe = requests.get(keys.coord_url).json()
        curr_weather = dataframe['weather'][0]['main']
        curr_temp = WeatherFunctions.CtoF(dataframe['main']['temp'])
        curr_low = WeatherFunctions.CtoF(dataframe['main']['temp_min'])
        curr_high = WeatherFunctions.CtoF(dataframe['main']['temp_max'])

        # Dictionary for current weather
        weather_dict = {"temp": str(curr_temp) + " F", "high": str(curr_high) + " F", "low": str(curr_low) + " F",
                        "weather": str(curr_weather) + " F"}
        return weather_dict
        pass

    @staticmethod
    def bringUmbrella(weather_dictionary):
        if weather_dictionary["weather"] == 'Rain':
            return "Bring it"
        return "Don't Need it"
