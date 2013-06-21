import datetime

count = 0
daysinmonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
curdate = datetime.date(1901, 1, 1)
while curdate.year < 2001:
   if curdate.weekday() == 6:
      count += 1
   curdate += datetime.timedelta(daysinmonth[curdate.month]-1)
   if curdate.year % 4 == 0 and (curdate.year % 100 != 0 or curdate.year % 400 == 0):
      curdate += datetime.timedelta(1)
 
   
print count