'''
    Using the data structure and format of the Here Maps Astronomy API,
    this code will get the time of either sunrise or sunset, recalculate 
    it and return an adjusted time for display. The calucluation currently
    depends on the programmer's input, but can be easily fixed as finite.
    Victor Sanchez,  December 2019 
'''
import re

# example of Here Maps API data structure
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
    "feedCreation": "2019-12-03T22:18:37.794Z",
    # "metric": true   # commented this out to run program
}


# DATA RETRIEVAL CHECK - - - - - - - - - - - - - - - - - - -
sunrise = heremaps_data["astronomy"]["astronomy"][0]["sunrise"]
sunset = heremaps_data["astronomy"]["astronomy"][0]["sunset"]
print("Sunrise at:", sunrise)
print("Sunset at:", sunset)

# * * * * * * * Possibly run both? Perhaps conditional?
# Starting with single hard-coded sample of 'sunset' as the ~value
suntime = sunset

def adjust_suntime():
    print('\nSpecified time:', suntime, '------------------------')
    print('\nStripping specified time  ---------------------------')

    # Assigns non-numeric elements from string to variables, numbers into integers
    am_pm = suntime[-2:]
    colon = suntime[-5]
    time_numbers = re.sub("AM|PM", "", suntime)
    hours_mins = time_numbers.split(":")
    print('hours, minutes =', hours_mins)
    
    hours = int(hours_mins[0])
    minutes = int(hours_mins[1])
    print('Non-numeric elements stripped  ---------------------------')

    # TIME ADJUSTMENT - - - - - - - - - - - - - - - - - - -
    adjusted_minutes = int(input("Adjustment in minutes: "))
    adjusted_hours = 0

    # Accounts for longer range of adjustment time
    if adjusted_minutes > 60:
        adjusted_hours = adjusted_minutes // 60
        adjusted_minutes = adjusted_minutes % 60
        if adjusted_hours > hours:
            hours = hours - adjusted_hours + 12 
            minutes -= adjusted_minutes
            if minutes < 0:
                minutes += 60
        else:
            hours -= adjusted_hours

    # Accounts for short range of adjustment time
    if adjusted_minutes > minutes:  
        hours -= 1
        minutes = minutes - adjusted_minutes + 60
    else:
        minutes -= adjusted_minutes

    # Convert adjusted times back to strings
    hours = str(hours)
    if minutes < 10:
        minutes = str(minutes)
        minutes = "0" + minutes
    else:
        minutes = str(minutes)
        
    
# TIME RECONSTRUCTION & DISPLAY- - - - - - - - - - - - - - - - - - -
    display_time = hours + colon + minutes + am_pm
    print('Display: "REMINDER @"', display_time)



adjust_suntime()
