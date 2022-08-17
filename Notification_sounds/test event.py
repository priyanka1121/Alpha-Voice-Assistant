import calendar
import datetime
from datetime import date
event_start = '2021-01-02T21:30:00+05:30'
date_extract = event_start.rsplit('T')
print(date_extract[0].split('-'))
MONTHS = { "01": "january", "02": "february", "03": "march", "04": "april", "05": "may", "06":"june", "07": "july", "08": "august", "09": "september", "10": "october", "11": "november",
          "12": "december"}
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
month = MONTHS[date_extract[0].split('-')[1]]
print(month)
day_of_week = date_extract[0].split('-')[2]
year = date_extract[0].split('-')[0]

now = datetime.datetime.now()
my_date =datetime.date(int(year),int(date_extract[0].split('-')[1]),int(day_of_week))
weakday = calendar.day_name[my_date.weekday()]
monthNum = my_date.month
dayNum = my_date.day
year = my_date.year
MONTHS = ['January', 'February' , 'March' , 'April' , 'May' , 'June' ,
                   'July' , 'August' , 'September' , 'October' , 'November' ,'December']

ordinalNumbers = ['1st' , '2nd' , '3rd' , '4th' , '5th ', '6th' , '7th' , '8th' , '9th' , '10th' , '11th',
                      '12th' , '13th' , '14th' , '15th' , '16th' , '17th' ,'18th' , '19th' , '20th' , '21st' ,
                      '22nd', '23rd' , '24th' , '25th' , '26th', '27th' , '28th' , '29th' , '30th' , '31st'
                     ]

print('{} of {} {} {}'.format(ordinalNumbers[dayNum -1],MONTHS[monthNum -1], year , weakday))

