'''
    THIS CODE MAY NOT BE USED BUT IS FUNCTIONAL
    Basic Time retrieval and modification of utcTime
'''
from django.test import TestCase
# Create your tests here.
from datetime import datetime, timedelta
import time

heremaps_data = {
    "astronomy": {
        "astronomy": [
            {
                "sunrise": "7:04AM",
                "sunset": "4:35PM",
                "moonrise": "12:33PM",
                "moonset": "11:24PM",
                "moonPhase": 0.378,
                "moonPhaseDesc": "Waxing crescent",
                "iconName": "cw_waxing_crescent",
                "city": "Camden",
                "latitude": 39.93,
                "longitude": -75.1,
                "utcTime": "2019-12-03T00:00:00.000-05:00"
            }
        ],
        "country": "United States",
        "state": "Pennsylvania",
        "city": "Philadelphia",
        "latitude": 39.95233,
        "longitude": -75.16379,
        "timezone": -5
    },
    "feedCreation": "2019-12-03T22:18:37.794Z", # alternate:  2013-12-10T15:44:37.120
    "metric": 'true'   # error:undefined variable - - - added quotes to 'true' to run code
}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# BASIC RETRIEVAL from dictionary structure above
# utc retrieval
print('\nTesting retrieval from API data structure - - - - - -')
utc_time = heremaps_data["astronomy"]["astronomy"][0]["utcTime"]
print("UTC Time: ", utc_time)
# feed creation retrieval
feed_creation = heremaps_data["feedCreation"]
print("Feed Creation: ", feed_creation)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('\nActual current time retrieval - - - - - - - - - - - -')
current_time = datetime.now()
print('(UTC-full): ', current_time)
# Adjustment method for current local time
current_time = datetime.now().strftime('%H:%M:%S')
print(current_time)

time_adjustment = int(input("Number of minutes to adjust: "))
adjusted_time = (datetime.now() + timedelta(minutes=-time_adjustment)).strftime('%H:%M:%S')
print('Adjusted time: ', adjusted_time)



