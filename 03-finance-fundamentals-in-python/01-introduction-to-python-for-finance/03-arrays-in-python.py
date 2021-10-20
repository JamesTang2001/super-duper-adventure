# 03 Arrays in Python
'''
This chapter introduces packages in Python, specifically the NumPy package and how it can be efficiently used to manipulate arrays.
'''



# Arrays
'''
Video
'''



# Create an array
'''
You can use the NumPy package to create arrays. NumPy arrays are optimized for numerical analyses and contain only a single data type. To convert a list to an array, you can use the array() function from NumPy.

import numpy as np
a_list = [1, 2, 3, 4]
a_list
[1, 2, 3, 4]

an_array = np.array(a_list)
an_array
array([1, 2, 3, 4])

Instructions
-Import numpy using the alias np.
-Create prices_array and earnings_array arrays from the lists prices and earnings, respectively.
'''
# Import numpy as np
import numpy as np

# Lists
prices = [170.12, 93.29, 55.28, 145.30, 171.81, 59.50, 100.50]
earnings = [9.2, 5.31, 2.41, 5.91, 15.42, 2.51, 6.79]

# NumPy arrays
prices_array = np.array(prices)
earnings_array = np.array(earnings)

# Print the arrays
print(prices_array)
print(earnings_array)



# Elementwise operations on arrays
'''
Arrays allow for efficient numerical manipulation of its elements. Let's explore element-wise mathematical operations by calculating price to earnings ratio using two arrays, prices_array and earnings_array from the previous exercise.
This price to earnings ratio, or PE ratio, is a financial indicator of the dollar amount an investor can expect to invest in a company in order to receive one dollar of that company’s earnings.
prices_array and earnings_array are available in your workspace.

Instructions
-Import numpy as np.
-Create pe_array by dividing prices_array by earnings_array.
'''
# Import numpy as np
import numpy as np

# Create PE ratio array
pe_array = np.array(prices_array / earnings_array)

# Print pe_array
print(pe_array)



# Subsetting elements from an array
'''
Subsetting arrays is similar to subsetting lists. In this exercise, you will practice just that.
numpy is imported as np and prices_array is available in your workspace.

Instructions 1/3
-Subset the first three elements from prices_array.
Instructions 2/3
-Subset the last three elements from the prices_array using negative index slicing.
Instructions 3/3
-Subset every third element from the prices_array using step slicing.
'''
# Subset the first three elements
prices_subset_1 = prices_array[0:3]
print(prices_subset_1)

# Subset last three elements 
prices_subset_2 = prices_array[-3:]
print(prices_subset_2)

# Subset every third element
prices_subset_3 = prices_array[0:7:3]
print(prices_subset_3)



# 2D arrays and functions
'''
Video
'''



# Creating a 2D array
'''
Multi-dimensional arrays can be useful for several tasks. In finance, for example, a 2D array may be used to store the prices and earnings for various companies. Let's create this 2D array, stock_array, from a list of prices and earnings.
numpy is imported as np and the two lists prices and earnings are available in your workspace.

Instructions 1/2
-Create a two dimensional array of prices and earnings (in that order) and assign it to stock_array.
-Print the shape of stock_array.
Instructions 2/2
-Transpose stock_array and assign the result to stock_array_transposed.
-Print the size of stock_array_transposed.
'''
# Create a 2D array of prices and earnings
stock_array = np.array([prices, earnings])
print(stock_array)

# Print the shape of stock_array
print(stock_array.shape)

# Print the size of stock_array
print(stock_array.size)

# Transpose stock_array
stock_array_transposed = np.transpose(stock_array)
print(stock_array_transposed)

# Print the shape of stock_array
print(stock_array_transposed.shape)

# Print the size of stock_array
print(stock_array_transposed.size)



# Subsetting 2D arrays
'''
Subsetting 2D arrays is similar to subsetting nested lists. In a 2D array, the indexing or slicing must be specific to the dimension of the array:
array[row_index, column_index]
numpy is imported as np and the 2D array stock_array_transposed (from the previous exercise) is available in your workspace.

Instructions 1/3
-Extract the first column from stock_array_transposed and assign it to prices.
Instructions 2/3
-Extract the second column from stock_array_transposed and assign it to earnings.
Instructions 3/3
-Subset the price and earning of the first company (row 0) from stock_array_transposed and assign it to company_1.
'''

# Subset prices from stock_array_transposed
prices = stock_array_transposed[:, 0]
print(prices)

# Subset earnings from stock_array_transposed
earnings = stock_array_transposed[:, 1]
print(earnings)

# Subset the price and earning for first company
company_1 = stock_array_transposed[0, :]
print(company_1)



# Calculating array stats
'''
Not only can you perform elementwise calculations on NumPy arrays, you can also calculate summary stats such as mean and standard deviation of arrays using functions from NumPy.
numpy is imported as np and the array prices (from the previous exercise) is available in your workspace.

Instructions 1/2
-Calculate the mean of prices.
Instructions 2/2
-Calculate the standard deviation of prices.
'''
# Calculate the mean 
prices_mean = np.mean(prices)
print(prices_mean)

# Calculate the standard deviation 
prices_std = np.std(prices)
print(prices_std)



# Generating a sequence of numbers
'''
You may want to create an array of a range of numbers (e.g., 1 to 10) without having to type in every single number. The NumPy function arange() is an efficient way to create numeric arrays of a range of numbers. The arguments for arange() include the start, stop, and step interval as shown below:
np.arange(start, stop, step)
numpy is imported as np.

Instructions
-Create an array company_ids containing the numbers 1 through 7 (inclusive).
-Create an array company_ids_odd containing only the odd numbers from 1 through 7 (inclusive).
'''
# Create and print company IDs
company_ids = np.arange(1, 8, 1)
print(company_ids)

# Use array slicing to select specific company IDs
company_ids_odd = np.arange(1, 8, 2)
print(company_ids_odd)



# Using arrays for analysis
'''
Video
'''



# Who's above average?
'''
Boolean arrays can be a very powerful way to subset arrays. In this exercise, you will identify the prices that are greater than average from a list of prices.
numpy is imported as np and the array prices is available in your workspace.

Instructions
-Find elements in prices that are greater than price_mean and assign the boolean result to boolean_array.
-Subset prices using boolean_array and assign the result to above_avg.
'''
# Find the mean
price_mean = np.mean(prices)

# Create boolean array
boolean_array = (price_mean < prices)
print(boolean_array)

# Select prices that are greater than average
above_avg = prices[boolean_array]
print(above_avg)



# Who's in health care?
'''
In this exercise, you are provided the names of companies with their associated sector, and your goal is to find all companies that are associated with health care sector.
numpy is imported as np and the arrays names and sectors are available in your workspace.

Instructions
-Find elements in sectors that are equivalent to 'Health Care' and assign the result to boolean_array.
-Subset names using boolean_array and assign the result to health_care.
'''
# Create boolean array
boolean_array = (sectors == "Health Care")
print(boolean_array)

# Print only health care companies
health_care = names[boolean_array]
print(health_care)
