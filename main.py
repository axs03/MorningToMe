import os
from TimezoneFunctions import TimezoneFunctions
from sms_function import SMS
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()

    times = TimezoneFunctions.convertTimeZone("America/New_York")
    local_time, india_time = times['curr_time'], times['india_times']

    day = TimezoneFunctions.getCurrentDay()


    subject = """ {day}'s Report """

    sms_body = """
                The current local time is {local_time}. \n 
                The current time in India is {india_time}. \n
    """

    sms = SMS(os.getenv("from_email"), os.getenv("email_passwd"), os.getenv("to_email"), subject=subject, body=sms_body)
    sms.newSMS()