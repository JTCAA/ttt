# JTC 20181011

from datetime import datetime
from sys import argv

#today = datetime.now().weekday()
#print(today)

print("YYYYMMDD", end=' ')
Y = input()
week = datetime.strptime(Y,"%Y%m%d").weekday()


#print(week+1)
w = (week+1)

if w == 7:
	x = 'Sunday'
elif w == 1:
	x = 'Monday'
elif w == 2:
	x = 'Tuesday' 
elif w == 3:
	x = 'Wednesday' 
elif w == 4:
	x = 'Thursday'
elif w == 5:
	x = 'Friday'
elif w == 6:
	x = 'Saturday'	

#print(f"Today is week {week+1}")
print(f"{Y} is {x}")