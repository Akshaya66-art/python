import calendar
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
cal = calendar.month(year, month)
print(f"\nCalendar for {calendar.month_name[month]} {year}:\n")
print(cal)