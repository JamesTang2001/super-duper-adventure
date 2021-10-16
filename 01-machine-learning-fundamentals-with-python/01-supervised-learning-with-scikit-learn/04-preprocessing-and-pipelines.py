# 04 Preprocessing and pipelines
'''
This chapter introduces pipelines, and how scikit-learn allows for transformers and estimators to be chained together and used as a single unit. Preprocessing techniques will be introduced as a way to enhance model performance, and pipelines will tie together concepts from previous chapters.
'''



# Preprocessing data
'''
Video
'''



# Exploring categorical features
'''
The Gapminder dataset that you worked with in previous chapters also contained a categorical 'Region' feature, which we dropped in previous exercises since you did not have the tools to deal with it. Now however, you do, so we have added it back in!
Your job in this exercise is to explore this feature. Boxplots are particularly useful for visualizing categorical features such as this.

Instructions
-Import pandas as pd.
-Read the CSV file 'gapminder.csv' into a DataFrame called df.
-Use pandas to create a boxplot showing the variation of life expectancy ('life') by region ('Region'). To do so, pass the column names in to df.boxplot() (in that order).
'''
# Import pandas
import pandas as pd

# Read 'gapminder.csv' into a DataFrame: df
df = pd.read_csv("gapminder.csv")

# Create a boxplot of life expectancy per region
df.boxplot("life", "Region", rot=60)

# Show the plot
plt.show()



# Creating dummy variables
'''
As Andy discussed in the video, scikit-learn does not accept non-numerical features. You saw in the previous exercise that the 'Region' feature contains very useful information that can predict life expectancy. For example, Sub-Saharan Africa has a lower life expectancy compared to Europe and Central Asia. Therefore, if you are trying to predict life expectancy, it would be preferable to retain the 'Region' feature. To do this, you need to binarize it by creating dummy variables, which is what you will do in this exercise.

Instructions
-Use the pandas get_dummies() function to create dummy variables from the df DataFrame. Store the result as df_region.
-Print the columns of df_region. This has been done for you.
-Use the get_dummies() function again, this time specifying drop_first=True to drop the unneeded dummy variable (in this case, 'Region_America').
-Hit 'Submit Answer to print the new columns of df_region and take note of how one column was dropped!
'''
# Create dummy variables: df_region
df_region = pd.get_dummies(df)

# Print the columns of df_region
print(df_region.columns)

# Create dummy variables with drop_first=True: df_region
df_region = pd.get_dummies(df, drop_first=True)

# Print the new columns of df_region
print(df_region.columns)



# Regression with categorical features
'''
Having created the dummy variables from the 'Region' feature, you can build regression models as you did before. Here, you'll use ridge regression to perform 5-fold cross-validation.
The feature array X and target variable array y have been pre-loaded.

Instructions
-Import Ridge from sklearn.linear_model and cross_val_score from sklearn.model_selection.
-Instantiate a ridge regressor called ridge with alpha=0.5 and normalize=True.
-Perform 5-fold cross-validation on X and y using the cross_val_score() function.
-Print the cross-validated scores.
'''
# Import necessary modules
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

# Instantiate a ridge regressor: ridge
ridge = Ridge(alpha=0.5, normalize=True)

# Perform 5-fold cross-validation: ridge_cv
ridge_cv = cross_val_score(ridge, X, y, cv=5)

# Print the cross-validated scores
print(ridge_cv)



# Handling missing data
'''
Video
'''



# 