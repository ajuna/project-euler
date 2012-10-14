#How many Sundays fell on the first of the month during the twentienth century ()1 jan 1901 to 31 dec 2000

import datetime
sundays=0
for year in range(1901,2001):
  for month in range(1,13):
    d=datetime.date(year,month,1) 
    if d.weekday()==6:
      sundays=sundays+1
print sundays
