import os
from TimezoneFunctions import TimezoneFunctions
from WeatherFunctions import WeatherFunctions
from sms_function import SMS
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()

    # Init of the classes and object
    # TimezoneFunctions is not a class
    weather_functions = WeatherFunctions()

    # Stuff for the Timzones and Dates
    times = TimezoneFunctions.convertTimeZone("America/New_York")
    local_time, india_time = times["curr_time"], times["india_time"]
    day = TimezoneFunctions.getCurrentDay()

    # Stuff for the Weather and Rain Probability
    weather_dict = weather_functions.getWeather()
    temperature = weather_dict["temp"]
    weather = weather_dict["weather"]
    need_umbrella = weather_functions.bringUmbrella()


    subject = """ {day} Report """

    sms_body = """
                The current local time is {local_time}. \n 
                The current time in India is {india_time}. \n
                The current tempersture locally is {temperature}. \n
                The current weather locally is {weather}. \n
                So, {need_umbrella}.
    """

    print(subject, sms_body)

    # sms = SMS(os.getenv("from_email"), os.getenv("email_passwd"), os.getenv("to_email"), subject=subject, body=sms_body)
    # sms.newSMS()