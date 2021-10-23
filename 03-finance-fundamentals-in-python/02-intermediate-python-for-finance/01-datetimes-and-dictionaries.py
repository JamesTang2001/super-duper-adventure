# 01 Datetimes and Dictionaries
'''
In this chapter, you’ll learn how to create and manipulate Python datetime objects to help you identify key financial events, such as Black Friday. You’ll also learn how to store and efficiently look up items using Python dictionaries.
'''



# Representing time with datetimes
'''
Video
'''



# Creating datetimes for dates
'''
Imagine that as a financial analyst, you are trying to understand the history of market crashes. In order to represent crashes in your code, you want to represent the times that they occurred. Two significant market crashes are the Kennedy Slide, also known as the Flash Crash, which started May 28, 1962, and the Black Monday crash of October 19th, 1987.

Instructions
-Create a datetime for the current time.
-Create a datetime to represent the time of the Flash Crash.
-Create a datetime to represent the time of the Black Monday Crash.
'''
import datetime

# Date and time now
now = datetime.datetime.now()
print(now)

# Flash crash May 28, 1962
flash_crash = datetime.datetime(1962, 5, 28)
print(flash_crash)

# Black Monday Oct 19, 1987
black_monday = datetime.datetime(1987, 10, 19)
print(black_monday)



# Datetimes from strings
'''
Often you get dates in different formats. There are many different sources of data that represent dates as strings. Scraping web pages, user input, and text files are just a few. The format strings for mapping datetimes are can be found at strftime. Suppose that you have found dates for the mini-crash of October 1989, given as the string crash_text, and the recession of July 3rd 1990, given as the string recession_text, in different formats. How would you represent both in your Python code?

Instructions
-Construct a format string that maps to the given text for the mini-crash of 1989.
-Construct a format string that maps to the text for the recession of 1990.
-Create a datetime representing the recession of 1990.
'''
crash_text = "Friday the 13th, Oct, 1989"

# Create a format string mapping the text
crash_format_str = "%A the %dth, %b, %Y"
min_crash = datetime.datetime.strptime(crash_text, crash_format_str)
print(min_crash)

recession_text = "07/03/90"

# Create format string
recession_format_str = "%m/%d/%y"

# Create datetime from text using format string
nineties_rec = datetime.datetime.strptime(recession_text, recession_format_str)
print(nineties_rec)



# Converting format with datetimes
'''
With datetimes, you can read a string with one format and output a string with a different format. This means that you can use datetimes to change the format of string dates. The format strings for mapping datetimes are can be found at strftime. Let's say you are asked to process the date of the British Black Wednesday crash into a new format that fits the reporting needs of your company.

Instructions
-Create a format string that fits the original string date, given as org_text.
-Create a datetime for Black Wednesday and save it as black_wednesday.
-Create a format string that fits the new format, 'Wednesday, September 16, 1992'.
-Create a new string date using the new format.
'''
org_text = "Sep 16 1992"

# Format string for original text
org_format = "%b %d %Y"

# Create datetime for Black Wednesday
black_wednesday = datetime.datetime.strptime(org_text, org_format)
print(black_wednesday)

# New format: 'Wednesday, September 16, 1992'
new_format = "%A, %B %d, %Y"

# String in new format
new_text = black_wednesday.strftime(new_format)
print(new_text)



# Working with datetimes
'''
Video
'''



# Accessing datetime attributes
'''
Suppose you are analyzing the tech bubble crash of 2000. For the sake of reporting, you need to assign the year, month, and day values to variables.
Use the attributes of a datetime object to assign the correct values to these variables.

Instructions
-Assign the year of the crash to the variable yr.
-Assign the month of the crash to the variable mth.
-Assign the day of the crash to the variable day.
'''
# March 10, 2000 Tech Bubble Crash
tech_bubble = datetime(2000, 3, 10)

# Access the year
yr  = tech_bubble.year

# Access the month
mth = tech_bubble.month

# Access the day
day = tech_bubble.day

print(f"Year: {yr}, Month: {mth}, Day: {day}")



# Comparing datetimes
'''
Imagine that you are trying to understand the events that made up the turbulent subprime crisis of 2008. You have a datetimes for some important dates. These include Lehman Brothers declaring bankruptcy, the passage of the TARP bill, and the movement of Goldman Sachs and Morgan Stanley out of investment banking.

Instructions 1/3
-Determine if the Lehman Brothers bankruptcy happened before Morgan Stanley left investment banking.
Instructions 2/3
-Determine if TARP was passed before Goldman Sachs left investment banking.
Instructions 3/3
-Determine if Goldman Sachs and Morgan Stanley left investment banking at the same time.
'''
# Lehman Brothers before Morgan Stanley?
lehman_first = lehman < morgan_stanley

print(f"It is {lehman_first} that Lehman Brothers declared bankruptcy first.") 

# Goldman Sachs after TARP?
tarp_first = goldman_sachs > tarp

print(f"It is {tarp_first} that TARP was approved first.")

# Goldman Sachs and Morgan Stanley same day?
same_time = goldman_sachs == morgan_stanley

print(f"It is {same_time} that Morgan Stanley and Goldman Sachs acted simultaneously")



# Making relative datetimes
'''
The Troubled Asset Relief Program (TARP) was passed in October of 2008 in an attempt to stablize the US financial system during the crisis of 2007-2008. To investigate the state of markets before and after the passage of TARP, you wish to create some datetimes for times before and after.

Instructions 1/3
-Create a datetime for one week before TARP was passed.
Instructions 2/3
-Create a datetime for one week after TARP passed.
Instructions 3/3
-Create a datetime for one year after TARP's passage.
'''
from datetime import datetime, timedelta

# TARP passed Oct 3 2008
tarp = datetime(2008, 10, 3)

# Seven days before TARP
week_before = tarp - timedelta(days = 7)

# Print week_before
print(week_before)

from datetime import datetime, timedelta

# TARP passed Oct 3 2008
tarp = datetime(2008, 10, 3)

# One week after TARP
week_after = tarp + timedelta(weeks = 1)

# Print week_after
print(week_after)

from datetime import datetime, timedelta

# TARP passed Oct 3 2008
tarp = datetime(2008, 10, 3)

# One year after TARP
year_after = tarp + timedelta(weeks = 52)

# Print year_after
print(year_after)



# Dictionaries
'''
Video
'''



# 