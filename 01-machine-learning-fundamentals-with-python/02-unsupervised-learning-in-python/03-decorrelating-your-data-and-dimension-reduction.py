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
You observed in the previous exercise that the width and length measurements of the grain are correlated. Now, you'll use PCA to decorrelate these measurements, then plot the decorrelated points and measure their Pearson correlation.

Instructions
-Import PCA from sklearn.decomposition.
-Create an instance of PCA called model.
-Use the .fit_transform() method of model to apply the PCA transformation to grains. Assign the result to pca_features.
-The subsequent code to extract, plot, and compute the Pearson correlation of the first two columns pca_features has been written for you, so hit 'Submit Answer' to see the result!
'''
# Import PCA
from sklearn.decomposition import PCA

# Create PCA instance: model
model = PCA()

# Apply the fit_transform method of model to grains: pca_features
pca_features = model.fit_transform(grains)

# Assign 0th column of pca_features: xs
xs = pca_features[:,0]

# Assign 1st column of pca_features: ys
ys = pca_features[:,1]

# Scatter plot xs vs ys
plt.scatter(xs, ys)
plt.axis('equal')
plt.show()

# Calculate the Pearson correlation of xs and ys
correlation, pvalue = pearsonr(xs, ys)

# Display the correlation
print(correlation)



# Principal components
'''
On the right are three scatter plots of the same point cloud. Each scatter plot shows a different set of axes (in red). In which of the plots could the axes represent the principal components of the point cloud?
Recall that the principal components are the directions along which the the data varies.

Possible Answers
-None of them.
-Both plot 1 and plot 3.
-Plot 2

# Both plot 1 and plot 3.
'''



# Intrinsic dimension
'''
Video
'''



# The first principal component
'''

'''