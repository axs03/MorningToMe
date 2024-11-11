from datetime import datetime
from pytz import all_timezones, timezone


class TimezoneFunctions:
    def convertTimeZone(zone_name: str) -> dict:
        india_tz = timezone("Asia/Calcutta")
        india_time = datetime.now(india_tz)

        curr_zone = timezone(zone_name)
        time_in_zone = datetime.now(curr_zone)

        tz_dict = {"curr_time": time_in_zone.strftime("%H:%M"), "india_time": india_time.strftime("%H:%M")}
        return tz_dict
    
    def getCurrentDay() -> str:
        return datetime.now().strftime("%A, %d %B")
