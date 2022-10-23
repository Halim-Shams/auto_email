import datetime as dt


now = dt.datetime.now()
year = now.year
month = now.month
day = now.weekday()
# YOU CAN MODIFY YOU BIRTH DAY HERE 👇
dob = dt.datetime(year=2003, month=11, day=19, hour=6)
print(dob)