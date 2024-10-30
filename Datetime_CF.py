import datetime
now = datetime.datetime.now()
"""
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
microsecond = now.microsecond

print(now)

print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
print(f"Hour: {hour}")
print(f"Minute: {minute}")
print(f"Second: {second}")
print(f"Microsecond: {microsecond}")


specific_date = datetime.datetime(2023, 10, 5, 14, 30)
print(specific_date)
   
now = datetime.datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

date_string = "2023-10-05 14:30:00"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(parsed_date)

now = datetime.datetime.now()
tomorrow = now + datetime.timedelta(days=1)
print(tomorrow)

date1 = datetime.datetime(2023, 10, 5)
date2 = datetime.datetime(2023, 10, 10)
difference = date2 - date1
print(difference.days)
print(date1 == date2)  # Check if they are equal
print(date1 != date2)  # Check if they are not equal
print(date1 < date2)   # Check if date1 is earlier than date2
print(date1 > date2)   # Check if date1 is later than date2
print(date1 <= date2)  # Check if date1 is earlier than or equal to date2
print(date1 >= date2)  # Check if date1 is later than or equal to date2
"""

date_string = "2024-10-25"

# Convert the string to a date object
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
# convert datetime to string
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

              

"""
%Y - year 4 digit
%y - year last 2 digit
%m - month
%d - day
%H - Hour
%M - minute
%S - second
%f - Micro Second

%B - Month Name
%b - Month Name shorter form


"""
# %B -month name, %b month short name, %Y four
print(datetime.date.strftime(now, "%m/%d/%Y"))
