from geopy.geocoders import Nominatim
import requests
import math


class WeatherFunctions():
    def __init__(self):
    # used by geopy
        self.locator = Nominatim(user_agent="GetLoc")

    def kelvinToCelsius(kelvin: float):
        return kelvin - 273.15

    def kelvinToFahrenheit(kelvin: float):
        return (kelvin - 273.15) * (9 / 5) + 32


    def CtoF(celsius: float):
        return math.ceil((celsius * 9 / 5) + 32)


    def getCurrentLocation(self,location):
        getLocation = self.locator.geocode(location)
        return {"long": getLocation.latitude, "lat": getLocation.longitude}


    def getWeather():
        # extracting json from openWeather
        dataframe = requests.get(keys.coord_url).json() # fix this
        curr_weather = dataframe['weather'][0]['main']
        curr_temp = WeatherFunctions.CtoF(dataframe['main']['temp'])
        curr_low = WeatherFunctions.CtoF(dataframe['main']['temp_min'])
        curr_high = WeatherFunctions.CtoF(dataframe['main']['temp_max'])

        # Dictionary for current weather
        weather_dict = {"temp": str(curr_temp) + " F", "high": str(curr_high) + " F", "low": str(curr_low) + " F",
                        "weather": str(curr_weather) + " F"}
        return weather_dict


    def bringUmbrella(weather_dictionary):
        if weather_dictionary["weather"] == 'Rain':
            return "Bring it"
        return "Don't Need it"
