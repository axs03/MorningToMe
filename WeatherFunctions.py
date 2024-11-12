from geopy.geocoders import Nominatim
import requests
import math
from dotenv import load_dotenv
import os


class WeatherFunctions():
    def __init__(self):
        load_dotenv()

        # locater is used by geopy
        self.locator = Nominatim(user_agent="GetLoc")

        self.longitude = ""
        self.latitude = ""
        self.openWeatherAPI = os.getenv("openWeatherAPI")
        self.coord_url = ""

    def kelvinToCelsius(kelvin: float) -> float:
        return kelvin - 273.15


    def kelvinToFahrenheit(kelvin: float) -> float:
        return (kelvin - 273.15) * (9 / 5) + 32


    def __CtoF(celsius: float) -> float:
        return math.ceil((celsius * 9 / 5) + 32)


    def getCurrentLocation(self,location) -> dict:
        getLocation = self.locator.geocode(location)
        return {"long": getLocation.latitude, "lat": getLocation.longitude}

    def __setCurrentLocation(self, location_dcitionary):
        self.longitude, self.latitude = location_dcitionary["long"], location_dcitionary["lat"]
        

    def getWeather(self):
        # setting the latitude and longitude for the reques to make
        self.__setCurrentLocation(self.getCurrentLocation(os.getenv("curr_city")))
        self.coord_url = "https://api.openweathermap.org/data/2.5/weather?lat={self.latitude}&lon={self.longitude}&appid={self.openWeatherAPI}&units=metric"

        # extracting json from openWeather
        dataframe = requests.get(self.coord_url).json()
        curr_weather = dataframe['weather'][0]['main']
        curr_temp = WeatherFunctions.__CtoF(dataframe['main']['temp'])
        curr_low = WeatherFunctions.__CtoF(dataframe['main']['temp_min'])
        curr_high = WeatherFunctions.__CtoF(dataframe['main']['temp_max'])

        # Dictionary for current weather
        weather_dict = {"temp": str(curr_temp) + " F", "high": str(curr_high) + " F", "low": str(curr_low) + " F",
                        "weather": str(curr_weather) + " F"}
        return weather_dict


    def bringUmbrella(weather_dictionary):
        return "bring an Umbrella" if weather_dictionary["weather"] == 'Rain' else "don't bring an Umbrella"
        