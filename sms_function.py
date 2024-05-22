from etext import send_sms_via_email
import misc_funcs
from misc_funcs import WeatherFunctions
import keys

sender_credentials = (keys.email, keys.email_passwd)

subject = "Daily Update"


def update_message(time_dict):
    message = ("Good morning! Lets have a good day today!"
               "\nThe time in India is " + (time_dict["india_time"]) +
               "\nThe Current Time in your timezone is " + (time_dict["curr_time"]) +
               "\nHere is the weather:"
               # "\n + Bring Umbrella? : " + str(WeatherFunctions.bringUmbrella(misc_funcs.weather)) +
               "\n + Current  : " + str(misc_funcs.weather['temp']) +
               "\n + High : " + str(misc_funcs.weather['high']) +
               "\n + Low : " + str(misc_funcs.weather['low']) +
               "\nHere are some things we have to do today:"
               "\n - ")

    # message = "This is a short message and the time is " + time_dict["curr_time"]
    # return message
    print(message)


def send_sms():
    send_sms_via_email(
        keys.my_number, update_message(), keys.provider, sender_credentials, subject
    )
