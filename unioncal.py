import os.path
import pytz
import icalendar
import datetime
from urllib.request import urlopen

url1 = 'https://www.google.com/calendar/ical/loganlyf%40gmail.com/private-d45c0973da1e18ebc6394c484ac5bbfb/basic.ics'

url2 = 'https://www.google.com/calendar/ical/6v928aad58pqdh360ruh1t9dps%40group.calendar.google.com/private-b5a1100cbe0c252c82aed028c4d91c59/basic.ics'

cal1 = icalendar.Calendar.from_ical(urlopen(url1).read())
cal2 = icalendar.Calendar.from_ical(urlopen(url2).read())

def getAllEvents(calendar):
    events = []
    for comp in calendar.subcomponents:
        if type(comp) == icalendar.cal.Event:
            events.append(comp)
    return events

events1 = getAllEvents(cal1)
print(cal1.subcomponents[0]['tzid'])
print(events1[0]['summary'],events1[0]['dtstart'],events1[0]['dtend'])
