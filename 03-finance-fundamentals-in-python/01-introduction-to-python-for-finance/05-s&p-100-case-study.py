# 05 S&P 100 Case Study
'''
In this chapter, you will get a chance to apply all the techniques you learned in the course on the S&P 100 data.
'''



# Introducing the dataset
'''
Video
'''



# Lists
'''
Stocks in the S&P 100 are selected to represent sector balance and market capitalization. To begin, let's take a look at what data we have associated with S&P companies.
Four lists, names, prices, earnings, and sectors, are available in your workspace.

Instructions
-Print the first four items in names.
-Print the name, price, earning, and sector associated with the last company in the lists.
'''
# First four items of names
print(names[0:4])

# Print information on last company
print(names[-1])
print(prices[-1])
print(earnings[-1])
print(sectors[-1])



# Arrays and NumPy
'''
NumPy is a scientific computing package in Python that helps you to work with arrays. Let's use array operations to calculate price to earning ratios of the S&P 100 stocks.
The S&P 100 data is available as the lists: prices (stock prices per share) and earnings (earnings per share).

Instructions
-Import the numpy as np.
-Convert the prices and earnings lists to arrays, prices_array and earnings_array, respectively.
-Calculate the price to earnings ratio as pe.
'''
# Import numpy as np
import numpy as np

# Convert lists to arrays
prices_array = np.array(prices)
earnings_array = np.array(earnings)

# Calculate P/E ratio 
pe = prices_array / earnings_array
print(pe)



# A closer look at the sectors
'''
Video
'''