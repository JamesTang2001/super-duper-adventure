# 04 Visualization in Python
'''
In this chapter, you will be introduced to the Matplotlib package for creating line plots, scatter plots, and histograms.
'''



# Visualization in Python
'''
Video
'''



# Importing matplotlib and pyplot
'''
Pyplot is a collection of functions in the popular visualization package Matplotlib. Its functions manipulate elements of a figure, such as creating a figure, creating a plotting area, plotting lines, adding plot labels, etc. Let's use the plot() function from pyplot to create a dashed line graph showing the growth of a company's stock. Remember, you can change the color of the line by adding the argument color and the linestlye by adding the argument linestyle.
Two lists, days (representing the days since the company became public), and prices (representing the price of the stock corresponding to that day) are available in your workspace.

Instructions
-Selectively import the pyplot module of matplotlib as plt.
-Plot days on the x-axis and prices on the y-axis as a red colored dashed line.
-Display the plot with the show() function.
'''
# Import matplotlib.pyplot with the alias plt
import matplotlib.pyplot as plt

# Plot the price of stock over time
plt.plot(days, prices, color="red", linestyle="--")

# Display the plot
plt.show()



# Adding axis labels and titles
'''
It is important to add labels to your plot so it's clear to other people what information it is trying to convey. In this exercise, you will add labels to the plot you created in the last one.

Instructions
-Add the following labels:
    -x-axis: 'Days'
    -y-axis: 'Prices, $'
    -title: 'Company Stock Prices Over Time'
'''
import matplotlib.pyplot as plt

# Plot price as a function of time
plt.plot(days, prices, color="red", linestyle="--")

# Add x and y labels
plt.xlabel('Days')
plt.ylabel('Prices, $')

# Add plot title
plt.title('Company Stock Prices Over Time')

# Show plot
plt.show()



# Multiple lines on the same plot
'''
You can also plot multiple datasets as different lines. To do so, you can use the plot() function multiple times. Let's plot the stocks of two companies over time.
matplotlib.pyplot is imported as plt and lists days, prices1, and prices2 are available in your workspace.

Instructions
-Plot prices1 data with a red line, and prices2 data with a green line.
'''
# Plot two lines of varying colors 
plt.plot(days, prices1, color='red')
plt.plot(days, prices2, color='green')

# Add labels
plt.xlabel('Days')
plt.ylabel('Prices, $')
plt.title('Stock Prices Over Time')
plt.show()



# Scatterplots
'''
The pyplot module can also be used to make other types of plots, like scatterplots. Let's make a scatterplot of the company's stock prices over time.
Two lists, days and prices are available in your workspace.

Instructions
-Draw a scatterplot with days on the x-axis and prices on the y-axis with green markers.
-Display the plot with the show() function.
'''
# Import pyplot as plt
import matplotlib.pyplot as plt

# Plot price as a function of time
plt.scatter(days, prices, color='green', s=0.1)

# Show plot
plt.show()



# Histograms
'''
Video
'''



# What are applications of histograms in finance?
'''
In which of the following situations would you use histograms?

Possible Answers
-To understand if the sales of regional branches of a company are centered around the average.
-To identify the abnormal stock performances.
-To see if stock prices of a particular company are skewed relative to the average stock prices of the sector.
-All of the above

# All of the above
'''



# Is data normally distributed?
'''
A histogram is an efficient visual tool to examine whether your data is normally distributed, or centered around the mean.
matplotlib.pyplot is imported as plt and the array prices is available in your workspace.

Instructions
-Plot a histogram of prices with 100 bins to confirm that the data is normally distributed.
-Display the plot.
'''
# Plot histogram 
plt.hist(prices, bins=100)

# Display plot
plt.show()



# Comparing two histograms
'''
Histograms can also be used to compare the distributions of multiple datasets. In this exercise, you will compare the performance of two different stocks to find out which stock has the most fluctuation.
matplotlib.pyplot is imported as plt and lists stock_A and stock_B are available in your workspace.

Instructions
-Plot the histogram of stock_A with 100 bins and a transparency of 0.4.
-Plot the histogram of stock_B with 100 bins and a transparency of 0.4.
'''
# Plot histogram of stocks_A
plt.hist(stock_A, bins=100, alpha=0.4)

# Plot histogram of stocks_B 
plt.hist(stock_B, bins=100, alpha=0.4)

# Display plot
plt.show()



# Adding a legend
'''
A legend can be useful when plotting multiple datasets to identify which plot is associated with a specific dataset. To add a legend, you can use the label argument. To display the legend on the plot, you can use the function plt.legend().
matplotlib.pyplot is imported as plt and lists stock_A and stock_B are available in your workspace.

Instructions
-Plot histograms for stock_A and stock_B and add labels to each plot ('Stock A' and 'Stock B').
-Display the legend and the plot.
'''
# Plot stock_A and stock_B histograms
plt.hist(stock_A, bins=100, alpha=0.4, label="Stock A")
plt.hist(stock_B, bins=100, alpha=0.4, label="Stock B")

# Add the legend
plt.legend()

# Display the plot
plt.show()
