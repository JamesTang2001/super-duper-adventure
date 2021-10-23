# 01 Applying logistic regression and SVM
'''
In this chapter you will learn the basics of applying logistic regression and support vector machines (SVMs) to classification problems. You'll use the scikit-learn library to fit classification models to real data.
'''



# scikit-learn refresher
'''
Video
'''



# KNN classification
'''
In this exercise you'll explore a subset of the Large Movie Review Dataset. The variables X_train, X_test, y_train, and y_test are already loaded into the environment. The X variables contain features based on the words in the movie reviews, and the y variables contain labels for whether the review sentiment is positive (+1) or negative (-1).
This course touches on a lot of concepts you may have forgotten, so if you ever need a quick refresher, download the Scikit-Learn Cheat Sheet and keep it handy!

Instructions
-Create a KNN model with default hyperparameters.
-Fit the model.
-Print out the prediction for the test example 0.
'''
from sklearn.neighbors import KNeighborsClassifier

# Create and fit the model
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

# Predict on the test features, print the results
pred = knn.predict(X_test[0])
print("Prediction for test example 0:", pred)



# Comparing models
'''
Compare k nearest neighbors classifiers with k=1 and k=5 on the handwritten digits data set, which is already loaded into the variables X_train, y_train, X_test, and y_test. You can set k with the n_neighbors parameter when creating the KNeighborsClassifier object, which is also already imported into the environment.
Which model has a higher test accuracy?

Possible Answers
-k=1
-k=5

# k=5
'''



# Overfitting
'''
Which of the following situations looks like an example of overfitting?

Possible Answers
-Training accuracy 50%, testing accuracy 50%.
-Training accuracy 95%, testing accuracy 95%.
-Training accuracy 95%, testing accuracy 50%.
-Training accuracy 50%, testing accuracy 95%.

# Training accuracy 95%, testing accuracy 50%.
'''



# Applying logistic regression and SVM
'''
Video
'''



# Running LogisticRegression and SVC
'''
In this exercise, you'll apply logistic regression and a support vector machine to classify images of handwritten digits.

Instructions
-Apply logistic regression and SVM (using SVC()) to the handwritten digits data set using the provided train/validation split.
-For each classifier, print out the training and validation accuracy.
'''
from sklearn import datasets
digits = datasets.load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target)

# Apply logistic regression and print scores
lr = LogisticRegression()
lr.fit(X_train, y_train)
print(lr.score(X_train, y_train))
print(lr.score(X_test, y_test))

# Apply SVM and print scores
svm = SVC()
svm.fit(X_train, y_train)
print(svm.score(X_train, y_train))
print(svm.score(X_test, y_test))



# Sentiment analysis for movie reviews
'''
In this exercise you'll explore the probabilities outputted by logistic regression on a subset of the Large Movie Review Dataset.
The variables X and y are already loaded into the environment. X contains features based on the number of times words appear in the movie reviews, and y contains labels for whether the review sentiment is positive (+1) or negative (-1).

Instructions
-Train a logistic regression model on the movie review data.
-Predict the probabilities of negative vs. positive for the two given reviews.
-Feel free to write your own reviews and get probabilities for those too!
'''
# Instantiate logistic regression and train
lr = LogisticRegression()
lr.fit(X, y)

# Predict sentiment for a glowing review
review1 = "LOVED IT! This movie was amazing. Top 10 this year."
review1_features = get_features(review1)
print("Review:", review1)
print("Probability of positive review:", lr.predict_proba(review1_features)[0,1])

# Predict sentiment for a poor review
review2 = "Total junk! I'll never watch a film by that director again, no matter how good the reviews."
review2_features = get_features(review2)
print("Review:", review2)
print("Probability of positive review:", lr.predict_proba(review2_features)[0,1])



# Linear classifiers
'''
Video
'''



#