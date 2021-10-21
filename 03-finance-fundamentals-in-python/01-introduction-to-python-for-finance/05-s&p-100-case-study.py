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



# Filtering arrays
'''
In this lesson, you will focus on two sectors:
    -Information Technology
    -Consumer Staples
numpy is imported as np and S&P 100 data is stored as arrays: names, sectors, and pe (price to earnings ratio).

Instructions 1/2
-Create a boolean array to determine which elements in sectors are 'Information Technology'.
-Use the boolean array to subset names and pe in the Information Technology sector.
Instructions 2/2
-Create a boolean array to determine which elements in sectors are 'Consumer Staples'.
-Use the boolean array to subset names and pe in the Consumer Staples sector.
'''
# Create boolean array 
boolean_array = (sectors == 'Information Technology')

# Subset sector-specific data
it_names = names[boolean_array]
it_pe = pe[boolean_array]

# Display sector names
print(it_names)
print(it_pe)

# Create boolean array 
boolean_array = (sectors == "Consumer Staples")

# Subset sector-specific data
cs_names = names[boolean_array]
cs_pe = pe[boolean_array]

# Display sector names
print(cs_names)
print(cs_pe)



# Summarizing sector data
'''
In this exercise, you will calculate the mean and standard deviation of P/E ratios for Information Technology and Consumer Staples sectors. numpy is imported as np and the it_pe and cs_pe arrays from the previous exercise are available in your workspace.

Instructions 1/2
-Calculate the mean and standard deviation of the P/E ratios (it_pe) for the Industrial Technology sector.
Instructions 2/2
-Calculate the mean and standard deviation of the P/E ratios (cs_pe) for the Consumer Staples sector.
'''
# Calculate mean and standard deviation
it_pe_mean = np.mean(it_pe)
it_pe_std = np.std(it_pe)

print(it_pe_mean)
print(it_pe_std)

# Calculate mean and standard deviation
cs_pe_mean = np.mean(cs_pe)
cs_pe_std = np.std(cs_pe)

print(cs_pe_mean)
print(cs_pe_std)



# Plot P/E ratios
'''
Let's take a closer look at the P/E ratios using a scatter plot for each company in these two sectors.
The arrays it_pe and cs_pe from the previous exercise are available in your workspace. Also, each company name has been assigned a numeric ID contained in the arrays it_id and cs_id.

Instructions
-Draw a scatter plot of it_pe ratios with red markers and 'IT' label.
-On the same plot, add the cs_pe ratios with green markers and 'CS' label.
-Add a legend to this plot.
-Display the plot.
'''
import matplotlib.pyplot as plt

# Make a scatterplot
plt.scatter(it_id, it_pe, color="red", label="IT")
plt.scatter(cs_id, cs_pe, color="green", label="CS")

# Add legend
plt.legend()

# Add labels
plt.xlabel('Company ID')
plt.ylabel('P/E Ratio')
plt.show()



# Visualizing trends
'''
Video
'''



# Histogram of P/E ratios
'''
To visualize and understand the distribution of the P/E ratios in the IT sector, you can use a histogram.
The array it_pe from the previous exercise is available in your workspace.

Instructions
-Selectively import the pyplot module of matplotlib as plt.
-Plot a histogram of it_pe with 8 bins.
-Add the x-label as 'P/E ratio' and y-label as 'Frequency'.
-Display the plot.
'''
# Import matplotlib.pyplot with the alias plt
import matplotlib.pyplot as plt

# Plot histogram 
plt.hist(it_pe, bins=8)

# Add x-label
plt.xlabel('P/E ratio')

# Add y-label
plt.ylabel('Frequency')

# Show plot
plt.show()



# Identify the outlier
'''
Histograms can help you to identify outliers or abnormal data points. Which P/E ratio in this histogram is an example of an outlier?

Possible Answers
-A stock with P/E ratio < 20.
-A stock with 20 < P/E ratio < 30.
-A stock with 30 < P/E ratio < 40.
-A stock with P/E ratio > 50.

# A stock with P/E ratio > 50.
'''



# Name the outlier
'''
You've identified that a company in the Industrial Technology sector has a P/E ratio of greater than 50. Let's identify this company.
numpy is imported as np, and arrays it_pe (P/E ratios of Industrial Technology companies) and it_names (names of Industrial Technology companies) are available in your workspace.

Instructions
-Identify the P/E ratio greater than 50 and assign it to outlier_price.
-Identify the company with P/E ratio greater than 50 and assign it to outlier_name.
'''
# Identify P/E ratio within it_pe that is > 50
outlier_price = it_pe[ it_pe > 50]

# Identify the company with PE ratio > 50
outlier_name = it_names[it_pe == outlier_price]

# Display results
print("In 2017, " + str(outlier_name[0]) + " had an abnormally high P/E ratio of " + str(round(outlier_price[0], 2)) + ".")
