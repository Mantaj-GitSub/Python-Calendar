import calendar

print("\n"+"*"*20,"\033[1;31m"," Calendar ","\033[1;0m","*"*20,"\n")

# User Input
year = int(input("Enter the year:\033[7;31m"))

# Printing Every month calendar
i = 1
while i<=12:
   print("\n")
   calendar.TextCalendar(calendar.SUNDAY).prmonth(year,i)
   print()
   i+=1






