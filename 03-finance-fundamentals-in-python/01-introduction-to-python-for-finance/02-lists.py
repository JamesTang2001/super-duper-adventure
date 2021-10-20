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



# Slicing multiple list elements
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
Lists can also contain other lists. In the example shown below, x is a nested list consisting of three lists:
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

You can use indexing to subset lists within a nested list. To extract the first list within x, you can use the following command:
x[0]
[1, 2, 3]

The two lists names and prices you created earlier are available in your workspace.

Instructions
-Create a list named stocks consisting of the lists names and prices, in that order.
-Use list indexing to subset the list prices from stocks (Remember that prices is the second element in stocks).
'''
# Create and print the nested list stocks
stocks = [names, prices]
print(stocks)

# Use list indexing to obtain the list of prices
print(stocks[1])



# Subset a nested list
'''
You can also extract an element from the list you extracted. To do this, you use two indices. The first index is the position of the list, and the second index is the position of the element within the list.
For example, if you want to extract 7 from x, you can use the following command:
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x[2][0]
7

Here the first index 2 refers to the third list in x and the second index 0 refers to the first element of the third list in x.
The nested list stocks you created in the last exercise is available in your workspace and is printed in the IPython shell on the right.

Instructions
-From the nested list stocks, subset 'Coca-Cola'.
-From the nested list stocks, subset the price for Walmart stock, i.e., 71.17.
'''
# Use indexing to obtain company name Coca-Cola
print(stocks[0][1])

# Use indexing to obtain 71.17
print(stocks[1][2])



# List methods and functions
'''
Video
'''



# Exploring list methods and functions
'''
Lists methods and functions are useful for analyses. Functions take objects as inputs or are "passed" an object. Methods, in contrast, act on objects. For lists, useful functions include max() and min(), which identify the maximum or minimum value in a list. A useful list method is .sort() which sorts the elements in a list.

Instructions 1/2
-Using the method .sort(), sort and print the prices in the list prices.
Instructions 2/2
-Identify the maximum price in prices using the function max().
'''
# Print the sorted list prices
prices = [159.54, 37.13, 71.17]
prices.sort()
print(prices)

# Find the maximum price in the list price
prices = [159.54, 37.13, 71.17]
price_max = max(prices)
print(price_max)



# Using list methods to add data
'''
You can use the .append() and .extend() methods to add elements to a list.
The .append() method increases the length of the list by one, so if you want to add only one element to the list, you can use this method.
x = [1, 2, 3]
x.append(4)
x
[1, 2, 3, 4]

The .extend() method increases the length of the list by the number of elements that are provided to the method, so if you want to add multiple elements to the list, you can use this method.
x = [1, 2, 3]
x.extend([4, 5])
x
[1, 2, 3, 4, 5]

Instructions
-Add a single element, 'Amazon.com', to the names.
-Add the list more_elements which consists of two elements to names.
'''
# Append a name to the list names
names.append('Amazon.com')
print(names)

# Extend list names
more_elements = ['DowDuPont', 'Alphabet Inc']
names.extend(more_elements)
print(names)



# Finding stock with maximum price
'''
Another useful list method is .index(), which returns the index of the element specified. For example, to get the index of 2 in x, you would use:
x = [1, 2, 3, 4]
x.index(2)
1

You can then use this result to subset another list, as you will do in this exercise.
The lists prices and names are available in your workspace.

Instructions
-Identify the index of max_price in the list prices.
-Use this index on the names list to identify the company with maximum stock price.
'''
# Do not modify this
max_price = max(prices)

# Identify index of max price
max_index = prices.index(max_price)

# Identify the name of the company with max price
max_stock_name = names[max_index]

# Fill in the blanks 
print('The largest stock price is associated with ' + max_stock_name + ' and is $' + str(max_price) + '.')
 