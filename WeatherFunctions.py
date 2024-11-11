from geopy.geocoders import Nominatim
import requests
import math
from dotenv import load_dotenv


class WeatherFunctions():
    def __init__(self):
        load_dotenv()

        # used by geopy
        self.locator = Nominatim(user_agent="GetLoc")
        self.coord_url = "https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={openWeatherAPI}&units=metric"

    def kelvinToCelsius(kelvin: float) -> float:
        return kelvin - 273.15

    def kelvinToFahrenheit(kelvin: float) -> float:
        return (kelvin - 273.15) * (9 / 5) + 32


    def CtoF(celsius: float) -> float:
        return math.ceil((celsius * 9 / 5) + 32)


    def getCurrentLocation(self,location) -> dict:
        getLocation = self.locator.geocode(location)
        return {"long": getLocation.latitude, "lat": getLocation.longitude}


    def getWeather(self):
        # extracting json from openWeather
        dataframe = requests.get(self.coord_url).json()
        curr_weather = dataframe['weather'][0]['main']
        curr_temp = WeatherFunctions.CtoF(dataframe['main']['temp'])
        curr_low = WeatherFunctions.CtoF(dataframe['main']['temp_min'])
        curr_high = WeatherFunctions.CtoF(dataframe['main']['temp_max'])

        # Dictionary for current weather
        weather_dict = {"temp": str(curr_temp) + " F", "high": str(curr_high) + " F", "low": str(curr_low) + " F",
                        "weather": str(curr_weather) + " F"}
        return weather_dict


    def bringUmbrella(weather_dictionary):
        return "Bring It "if weather_dictionary["weather"] == 'Rain' else "Don't Need It"
        