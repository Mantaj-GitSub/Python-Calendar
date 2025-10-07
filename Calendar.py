import calendar

year = int(input("Enter the year: "))

print("\n\n***** Calendar *****")

i = 1

while i<=12:
   print("\n")
   calendar.TextCalendar(calendar.SUNDAY).prmonth(year,i)
   print()
   i+=1






