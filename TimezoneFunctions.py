from datetime import datetime
import pytz


class TimezoneFunctions:
    zones = pytz.all_timezones

    @staticmethod
    def convertTimeZone(zone_name):
        india_tz = pytz.timezone("Asia/Calcutta")
        india_time = datetime.now(india_tz)

        curr_zone = pytz.timezone(zone_name)
        time_in_zone = datetime.now(curr_zone)

        tz_dict = {"curr_time": time_in_zone.strftime("%H:%M"), "india_time": india_time.strftime("%H:%M")}
        return tz_dict
