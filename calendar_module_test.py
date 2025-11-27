import calendar
print(calendar.isleap(2025)) # False
print(calendar.isleap(2069)) # False
print(calendar.isleap(2072)) # True
print(calendar.isleap(2028)) # True

print(calendar.weekday(1991,3,23)) # 5 (Saturday)