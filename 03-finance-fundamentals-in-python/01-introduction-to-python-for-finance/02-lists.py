# 02 Lists
'''
This chapter introduces lists in Python and how they can be used to work with data.
'''



# Lists
'''
Video
'''



# Creating lists in Python
'''
A list in Python can contain any number of elements. You generally create a list using square brackets. For example, to create a list of integers, you can use the following command:
x = [1, 2, 3]

Instructions
-Create a list named names containing the strings 'Apple Inc', 'Coca-Cola', and 'Walmart', in that order.
-Print names.
-Create a list named prices containing the price of each stock, $159.54, $37.13, and $71.17, in that order.
-Print prices.
'''
# Create and print list names
names =["Apple Inc", "Coca-Cola", "Walmart"]
print(names)

# Create and print list prices
prices = [159.54, 37.13, 71.17]
print(prices)



# Indexing list items
'''
Each item in a list has an assigned indexed value. Remember that Python is a zero indexed language, and the first element in a list is stored at index zero. In this exercise, you will practice subsetting single elements from a list.
Lists names and prices for company names and stock prices are available in your workspace.

Instructions
-Print the first element in names.
-Print the second element in names.
-Using a negative index, print the last element in prices.
'''
# Print the first item in names
print(names[0])

# Print the second item in names
print(names[1])

# Print the last element in prices
print(prices[-1])



# 
'''
Slicing operations on a list are used to subset multiple elements from a list. The syntax for list slicing is as follows:
list[start:end]

Remember, this syntax indicates subsetting all elements from the start and up to but not including the end element.
Also, you can use extended slicing to efficiently select multiple elements from a list. For example, the following command returns all elements from the list except the first (at index 0):
x = [1, 2, 3, 4, 5]
x[1:]
[2, 3, 4, 5]

Similarly, the following command returns all elements from the list except the last two:
x[:-2]
[1, 2, 3]

Instructions 1/2
-Use list slicing to subset the last two elements from names.
Instructions 2/2
-Use extended slicing and specifying appropriate indices to subset the first two elements from prices.
'''
# names
names = ['Apple Inc', 'Coca-Cola', 'Walmart']

# Use slicing on list names
names_subset = names[-1:-3]
print(names_subset)

# prices
prices = [159.54, 37.13, 71.17]

# Use extended slicing on the list prices
prices_subset = prices[:3]
print(prices_subset)



# Nested lists
'''
Video
'''



# Stock up a nested list
'''

'''