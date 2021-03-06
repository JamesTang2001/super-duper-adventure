# 02 Regression
'''
In the previous chapter, you used image and political datasets to predict binary and multiclass outcomes. But what if your problem requires a continuous outcome? Regression is best suited to solving such problems. You will learn about fundamental concepts in regression and apply them to predict the life expectancy in a given country using Gapminder data.
'''



# Introduction to regression
'''
Video
'''



# Which of the following is a regression problem?
'''
Andy introduced regression to you using the Boston housing dataset. But regression models can be used in a variety of contexts to solve a variety of different problems.
Given below are four example applications of machine learning. Your job is to pick the one that is best framed as a regression problem.

Possible Answers
-An e-commerce company using labeled customer data to predict whether or not a customer will purchase a particular item.
-A healthcare company using data about cancer tumors (such as their geometric measurements) to predict whether a new tumor is benign or malignant.
-A restaurant using review data to ascribe positive or negative sentiment to a given review.
-A bike share company using time and weather data to predict the number of bikes being rented at any given hour.

# A bike share company using time and weather data to predict the number of bikes being rented at any given hour.
'''



# Importing data for supervised learning
'''
In this chapter, you will work with Gapminder data that we have consolidated into one CSV file available in the workspace as 'gapminder.csv'. Specifically, your goal will be to use this data to predict the life expectancy in a given country based on features such as the country's GDP, fertility rate, and population. As in Chapter 1, the dataset has been preprocessed.
Since the target variable here is quantitative, this is a regression problem. To begin, you will fit a linear regression with just one feature: 'fertility', which is the average number of children a woman in a given country gives birth to. In later exercises, you will use all the features to build regression models.
Before that, however, you need to import the data and get it into the form needed by scikit-learn. This involves creating feature and target variable arrays. Furthermore, since you are going to use only one feature to begin with, you need to do some reshaping using NumPy's .reshape() method. Don't worry too much about this reshaping right now, but it is something you will have to do occasionally when working with scikit-learn so it is useful to practice.

Instructions
-Import numpy and pandas as their standard aliases.
-Read the file 'gapminder.csv' into a DataFrame df using the read_csv() function.
-Create array X for the 'fertility' feature and array y for the 'life' target variable.
-Reshape the arrays by using the .reshape() method and passing in -1 and 1.
'''
# Import numpy and pandas
import numpy as np
import pandas as pd

# Read the CSV file into a DataFrame: df
df = pd.read_csv("gapminder.csv")

# Create arrays for features and target variable
y = df.life
X = df.fertility

# Print the dimensions of y and X before reshaping
print("Dimensions of y before reshaping: ", y.shape)
print("Dimensions of X before reshaping: ", X.shape)

# Reshape X and y
y_reshaped = df.life.reshape(-1, 1)
X_reshaped = df.fertility.reshape(-1, 1)

# Print the dimensions of y_reshaped and X_reshaped
print("Dimensions of y after reshaping: ", y_reshaped.shape)
print("Dimensions of X after reshaping: ", X_reshaped.shape)



# Exploring the Gapminder data
'''
As always, it is important to explore your data before building models. On the right, we have constructed a heatmap showing the correlation between the different features of the Gapminder dataset, which has been pre-loaded into a DataFrame as df and is available for exploration in the IPython Shell. Cells that are in green show positive correlation, while cells that are in red show negative correlation. Take a moment to explore this: Which features are positively correlated with life, and which ones are negatively correlated? Does this match your intuition?
Then, in the IPython Shell, explore the DataFrame using pandas methods such as .info(), .describe(), .head().
In case you are curious, the heatmap was generated using Seaborn's heatmap function and the following line of code, where df.corr() computes the pairwise correlation between columns:
sns.heatmap(df.corr(), square=True, cmap='RdYlGn')
Once you have a feel for the data, consider the statements below and select the one that is not true. After this, Hugo will explain the mechanics of linear regression in the next video and you will be on your way building regression models!

Possible Answers
-The DataFrame has 139 samples (or rows) and 9 columns.
-life and fertility are negatively correlated.
-The mean of life is 69.602878.
-fertility is of type int64.
-GDP and life are positively correlated.

# fertility is of type int64.
'''



# fertility is of type int64.
'''
Video
'''



# 
'''

'''
