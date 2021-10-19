# 03 Decorrelating your data and dimension reduction
'''
Dimension reduction summarizes a dataset using its common occuring patterns. In this chapter, you'll learn about the most fundamental of dimension reduction techniques, "Principal Component Analysis" ("PCA"). PCA is often used before supervised learning to improve model performance and generalization. It can also be useful for unsupervised learning. For example, you'll employ a variant of PCA will allow you to cluster Wikipedia articles by their content!
'''



# Visualizing the PCA transformation
'''
Video
'''



# Correlated data in nature
'''
You are given an array grains giving the width and length of samples of grain. You suspect that width and length will be correlated. To confirm this, make a scatter plot of width vs length and measure their Pearson correlation.

Instructions
-Import:
    -matplotlib.pyplot as plt.
    -pearsonr from scipy.stats.
-Assign column 0 of grains to width and column 1 of grains to length.
-Make a scatter plot with width on the x-axis and length on the y-axis.
-Use the pearsonr() function to calculate the Pearson correlation of width and length.
'''
# Perform the necessary imports
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Assign the 0th column of grains: width
width = grains[:,0]

# Assign the 1st column of grains: length
length = grains[:,1]

# Scatter plot width vs length
plt.scatter(width, length)
plt.axis('equal')
plt.show()

# Calculate the Pearson correlation
correlation, pvalue = pearsonr(width, length)

# Display the correlation
print(correlation)



# Decorrelating the grain measurements with PCA
'''

'''
