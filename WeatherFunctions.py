# from geopy.geocoders import Nominatim
from opencage.geocoder import OpenCageGeocode # replaced Nominatim
import requests
import math
from dotenv import load_dotenv
import os


class WeatherFunctions():
    def __init__(self):
        load_dotenv()

        # locater is used by geopy
        # self.locator = Nominatim(user_agent="GetLoc")

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


    def getCurrentLocation(self, location) -> dict:
        api_key = os.getenv("OPENCAGE_API_KEY")
        geocoder = OpenCageGeocode(api_key)
        result = geocoder.geocode(location)
        if result:
            return {"long": result[0]['geometry']['lng'], "lat": result[0]['geometry']['lat']}
        else:
            raise Exception("Error fetching location")

    def __setCurrentLocation(self, location_dcitionary):
        self.longitude, self.latitude = location_dcitionary["long"], location_dcitionary["lat"]
        

    def getWeather(self):
        # setting the latitude and longitude for the request to make
        # self.__setCurrentLocation(self.getCurrentLocation(os.getenv("curr_city")))
        self.__setCurrentLocation(self.getCurrentLocation("New_York"))

        self.coord_url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.latitude}&lon={self.longitude}&appid={self.openWeatherAPI}&units=metric"

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


    def bringUmbrella(self, weather_dictionary: dict) -> str:
        return "bring an Umbrella" if weather_dictionary["weather"] == 'Rain' else "don't bring an Umbrella"
        