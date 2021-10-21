# 04 Discovering interpretable features
'''
In this chapter, you'll learn about a dimension reduction technique called "Non-negative matrix factorization" ("NMF") that expresses samples as combinations of interpretable parts. For example, it expresses documents as combinations of topics, and images in terms of commonly occurring visual patterns. You'll also learn to use NMF to build recommender systems that can find you similar articles to read, or musical artists that match your listening history!
'''



# Non-negative matrix factorization (NMF)
'''
Video
'''



# Non-negative data
'''
Which of the following 2-dimensional arrays are examples of non-negative data?
1.A tf-idf word-frequency array.
2.An array daily stock market price movements (up and down), where each row represents a company.
3.An array where rows are customers, columns are products and entries are 0 or 1, indicating whether a customer has purchased a product.

Possible Answers
-1 only
-2 and 3
-1 and 3

# 1 and 3
'''



# NMF applied to Wikipedia articles
'''
In the video, you saw NMF applied to transform a toy word-frequency array. Now it's your turn to apply NMF, this time using the tf-idf word-frequency array of Wikipedia articles, given as a csr matrix articles. Here, fit the model and transform the articles. In the next exercise, you'll explore the result.

Instructions
-Import NMF from sklearn.decomposition.
-Create an NMF instance called model with 6 components.
-Fit the model to the word count data articles.
-Use the .transform() method of model to transform articles, and assign the result to nmf_features.
-Print nmf_features to get a first idea what it looks like (.round(2) rounds the entries to 2 decimal places.)
'''
# Import NMF
from sklearn.decomposition import NMF

# Create an NMF instance: model
model = NMF(n_components=6)

# Fit the model to articles
model.fit(articles)

# Transform the articles: nmf_features
nmf_features = model.transform(articles)

# Print the NMF features
print(nmf_features.round(2))



# NMF features of the Wikipedia articles
'''
Now you will explore the NMF features you created in the previous exercise. A solution to the previous exercise has been pre-loaded, so the array nmf_features is available. Also available is a list titles giving the title of each Wikipedia article.
When investigating the features, notice that for both actors, the NMF feature 3 has by far the highest value. This means that both articles are reconstructed using mainly the 3rd NMF component. In the next video, you'll see why: NMF components represent topics (for instance, acting!).

Instructions
-Import pandas as pd.
-Create a DataFrame df from nmf_features using pd.DataFrame(). Set the index to titles using index=titles.
-Use the .loc[] accessor of df to select the row with title 'Anne Hathaway', and print the result. These are the NMF features for the article about the actress Anne Hathaway.
-Repeat the last step for 'Denzel Washington' (another actor).
'''
# Import pandas
import pandas as pd

# Create a pandas DataFrame: df
df = pd.DataFrame(nmf_features, index=titles)

# Print the row for 'Anne Hathaway'
print(df.loc["Anne Hathaway"])

# Print the row for 'Denzel Washington'
print(df.loc["Denzel Washington"])



# NMF reconstructs samples
'''
In this exercise, you'll check your understanding of how NMF reconstructs samples from its components using the NMF feature values. On the right are the components of an NMF model. If the NMF feature values of a sample are [2, 1], then which of the following is most likely to represent the original sample? A pen and paper will help here! You have to apply the same technique Ben used in the video to reconstruct the sample [0.1203 0.1764 0.3195 0.141].

Possible Answers
-[2.2, 1.1, 2.1].
-[0.5, 1.6, 3.1].
-[-4.0, 1.0, -2.0].

# [2.2, 1.1, 2.1].
'''



# NMF learns interpretable parts
'''
Video
'''