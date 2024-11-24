import os
from TimezoneFunctions import TimezoneFunctions
from WeatherFunctions import WeatherFunctions
from sms_function import SMS
from newsapi import NewsApiClient
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()

    news_getter = NewsApiClient(api_key=os.getenv("NewsAPIv2_API"))
    news_data = news_getter.get_top_headlines(language="en", country="us", category="technology")

    ai_news = [article for article in news_data['articles']]

    news_titles = "\n\n".join([article['title'] for article in ai_news])

    # Init of the classes and object
    weather_functions = WeatherFunctions()

    # Stuff for the Timzones and Dates
    times = TimezoneFunctions.convertTimeZone("America/New_York")
    local_time, india_time = times["curr_time"], times["india_time"]
    day = TimezoneFunctions.getCurrentDay()

    # Stuff for the Weather and Rain Probability
    weather_dict = weather_functions.getWeather()
    temperature = weather_dict["temp"]

    need_umbrella = weather_functions.bringUmbrella(weather_dict)
    weather= weather_dict["weather"]

    subject = f""" {day} Report """

    sms_body = f"""
    The current time in in Middletown is {local_time}. \n 
    The current time in India is {india_time}. \n
    The current temperature in Middletown is {temperature}. \n
    The current weather locally is {weather}. \n
    So, {need_umbrella}. \n
    News Articles: \n
    \n{news_titles}
    """
    
    # for debug
    # print(subject, sms_body)

    sms = SMS(os.getenv("from_email"), os.getenv("email_passwd"), os.getenv("to_email"), subject=subject, body=sms_body)
    sms.newSMS()