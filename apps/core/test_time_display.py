''' 
THIS CODE IS UNFINISHED AND MAY BE UNNECESSARY
Testing utc modification and conversion into human readable format
'''
import datetime
import pytz
import re

# GETTING CURRENT TIMESTAMP in seconds
# define epoch, the beginning of times in the UTC timestamp world
epoch = datetime.datetime(1970,1,1,0,0,0)

now = datetime.datetime.utcnow()
print('\nUTC now: ', now)

# subtracting datetime objects result in a datetime.timedelta object which can be expressed in seconds.
timestamp = (now - epoch).total_seconds()
print('Timestamp in seconds: ', timestamp, "\n")


# Removes T and Z characters from HereMaps "feedCreated" time format
feed_creation ="2019-12-03T22:18:37.794Z"
print("Date before cleaning: ", feed_creation)
# date_stripped = re.sub("T|Z", " ", feed_creation)
# print("Cleaned date: ", date_stripped, "\n")
strip1 = feed_creation.replace("Z", "" )
date_stripped = strip1.replace("T", " ")
print("Cleaned date: ", date_stripped, "\n")


# Converts time format into timestamp
feed_creation_object = datetime.datetime.strptime(date_stripped,'%Y-%m-%d %H:%M:%S.%f')
print("Current Feed Object: ", feed_creation_object)
timestamp = (feed_creation_object - epoch).total_seconds()
print('Current Feed Timestamp(seconds): ', timestamp, "\n")


# Modifying timestamp to adjusted time

# Returning modified timestamp as human-readable time format