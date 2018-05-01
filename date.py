import datetime
import math

date1 = datetime.datetime.now()

print()
print("Current date and time using str method of datetime object:")
print(str(date1))

# print()
# print("Current date and time using instance attributes:")
# print("Current year: %d" % now.year)
# print("Current month: %d" % now.month)
# print("Current day: %d" % now.day)
# print("Current hour: %d" % now.hour)
# print("Current minute: %d" % now.minute)
# print("Current second: %d" % now.second)
# print("Current microsecond: %d" % now.microsecond)

# print()
# print("Current date and time using strftime:")
# print(now.strftime("%Y-%m-%d %H:%M"))

# print()
# print("Current date and time using isoformat:")
# print(now.isoformat())
# now.
x = 0
for i in range(0, 10000000):
    x += 1
    x += math.sqrt(i)

date2 = datetime.datetime.now()
print()
print("Current date and time using str method of datetime object:")
print(str(date2))

diff = date2 - date1

print("Diff:")
print(diff)
print(str(diff.total_days()))