import datetime

date = datetime.date(*map(int, input().split(" ")))
# datetime.datetime.strptime(input(), "%Y %m %d")
date += datetime.timedelta(days=int(input()))
print(date.year, date.month, date.day)
