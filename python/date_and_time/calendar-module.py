import calendar

days = calendar.weekheader(10).split()
m, d, y = map(int, input().split())
day = calendar.weekday(y, m, d)
print(days[day].upper())
