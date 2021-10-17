# 01 Common data problems
'''
In this chapter, you'll learn how to overcome some of the most common dirty data problems. You'll convert data types, apply range constraints to remove future data points, and remove duplicated data points to avoid double-counting.
'''



# Data type constraints
'''
Video
'''



# Common data types
'''
Manipulating and analyzing data with incorrect data types could lead to compromised analysis as you go along the data science workflow.
When working with new data, you should always check the data types of your columns using the .dtypes attribute or the .info() method which you'll see in the next exercise. Often times, you'll run into columns that should be converted to different data types before starting any analysis.
In this exercise, you'll first identify different types of data and correctly map them to their respective types.

Instructions
-Assign each card to what type of data you think it is.
'''
# Drag the items into the correct
'''
Drop items into the correct bucket
'''

# Numeric data types
'''
Number of points on customer loyalty card
Salary earned monthly
Number of items bought in a basket
'''

# Text
'''
Shipping address of a customer
City of residence
First name
'''

# Dates
'''
Birthdates of clients
Order date of a product
'''



# Numeric data or ... ?
'''
In this exercise, and throughout this chapter, you'll be working with bicycle ride sharing data in San Francisco called ride_sharing. It contains information on the start and end stations, the trip duration, and some user information for a bike sharing service.
The user_type column contains information on whether a user is taking a free ride and takes on the following values:
    -1 for free riders.
    -2 for pay per ride.
    -3 for monthly subscribers.
In this instance, you will print the information of ride_sharing using .info() and see a firsthand example of how an incorrect data type can flaw your analysis of the dataset. The pandas package is imported as pd.

Instructions 1/3
-Print the information of ride_sharing.
-Use .describe() to print the summary statistics of the user_type column from ride_sharing.

Instructions 2/3
By looking at the summary statistics - they don't really seem to offer much description on how users are distributed along their purchase type, why do you think that is?

Possible Answers
-The user_type column is not of the correct type, it should be converted to str.
-The user_type column has an infinite set of possible values, it should be converted to category.
-The user_type column has an finite set of possible values that represent groupings of data, it should be converted to category.

# The user_type column has an finite set of possible values that represent groupings of data, it should be converted to category.

Instructions 3/3
-Convert user_type into categorical by assigning it the 'category' data type and store it in the user_type_cat column.
-Make sure you converted user_type_cat correctly by using an assert statement.
'''
# Print the information of ride_sharing
print(ride_sharing.info())

# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe())

# 

# Print the information of ride_sharing
print(ride_sharing.info())

# Print summary statistics of user_type column
print(ride_sharing['user_type'].describe())

# Convert user_type from integer to category
ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype("category")

# Write an assert statement confirming the change
assert ride_sharing['user_type_cat'].dtype == 'category'

# Print new summary statistics 
print(ride_sharing['user_type_cat'].describe())



# Summing strings and concatenating numbers
'''
In the previous exercise, you were able to identify that category is the correct data type for user_type and convert it in order to extract relevant statistical summaries that shed light on the distribution of user_type.
Another common data type problem is importing what should be numerical values as strings, as mathematical operations such as summing and multiplication lead to string concatenation, not numerical outputs.
In this exercise, you'll be converting the string column duration to the type int. Before that however, you will need to make sure to strip "minutes" from the column in order to make sure pandas reads it as numerical. The pandas package has been imported as pd.

Instructions
-Use the .strip() method to strip duration of "minutes" and store it in the duration_trim column.
-Convert duration_trim to int and store it in the duration_time column.
-Write an assert statement that checks if duration_time's data type is now an int.
-Print the average ride duration.
'''
# Strip duration of minutes
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip('minutes')

# Convert duration to integer
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')

# Write an assert statement making sure of conversion
assert ride_sharing['duration_time'].dtype == 'int'

# Print formed columns and calculate average ride duration 
print(ride_sharing[['duration','duration_trim','duration_time']])
print(ride_sharing['duration_time'].mean())



# Data range constraints
'''
Video
'''



# 