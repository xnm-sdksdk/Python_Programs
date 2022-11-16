import datetime

date = datetime.datetime.now()

first = "Today is %s-%s-%s" % (date.year, date.month, date.day)
second = " and it is %s:%s:%s." % (date.hour, date.minute, date.second)

print(first + second)