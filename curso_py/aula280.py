import calendar

print(calendar.calendar(2022))
print(calendar.month(2024, 10))

for week in calendar.monthcalendar(2024, 10):
    print(week)