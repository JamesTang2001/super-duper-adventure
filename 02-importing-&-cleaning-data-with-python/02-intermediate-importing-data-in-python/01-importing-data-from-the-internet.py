# 01 Importing data from the Internet
'''
The web is a rich source of data from which you can extract various types of insights and findings. In this chapter, you will learn how to get data from the web, whether it is stored in files or in HTML. You'll also learn the basics of scraping and parsing web data.
'''



# Importing flat files from the web
'''
Video
'''



# Importing flat files from the web: your turn!
'''
You are about to import your first file from the web! The flat file you will import will be 'winequality-red.csv' from the University of California, Irvine's Machine Learning repository. The flat file contains tabular data of physiochemical properties of red wine, such as pH, alcohol content and citric acid content, along with wine quality rating.
The URL of the file is 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
After you import it, you'll check your working directory to confirm that it is there and then you'll load it into a pandas DataFrame.

Instructions
-Import the function urlretrieve from the subpackage urllib.request.
-Assign the URL of the file to the variable url.
-Use the function urlretrieve() to save the file locally as 'winequality-red.csv'.
-Execute the remaining code to load 'winequality-red.csv' in a pandas DataFrame and to print its head to the shell.
'''
# Import package
from urllib.request import urlretrieve

# Import pandas
import pandas as pd

# Assign url of file: url
url = "https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv"

# Save file locally
urlretrieve(url, "winequality-red.csv")

# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())



# Opening and reading flat files from the web
'''
You have just imported a file from the web, saved it locally and loaded it into a DataFrame. If you just wanted to load a file from the web into a DataFrame without first saving it locally, you can do that easily using pandas. In particular, you can use the function pd.read_csv() with the URL as the first argument and the separator sep as the second argument.
The URL of the file, once again, is 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

Instructions
-Assign the URL of the file to the variable url.
-Read file into a DataFrame df using pd.read_csv(), recalling that the separator in the file is ';'.
-Print the head of the DataFrame df.
-Execute the rest of the code to plot histogram of the first feature in the DataFrame df.
'''
# Import packages
import matplotlib.pyplot as plt
import pandas as pd



# Assign url of file: url
url = "https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv"

# Read file into a DataFrame: df
df = pd.read_csv(url, delimiter = ";")

# Print the head of the DataFrame
print(df.head())

# Plot first column of df
pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()



# Importing non-flat files from the web
'''
Congrats! You've just loaded a flat file from the web into a DataFrame without first saving it locally using the pandas function pd.read_csv(). This function is super cool because it has close relatives that allow you to load all types of files, not only flat ones. In this interactive exercise, you'll use pd.read_excel() to import an Excel spreadsheet.
The URL of the spreadsheet is 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'
Your job is to use pd.read_excel() to read in all of its sheets, print the sheet names and then print the head of the first sheet using its name, not its index.
Note that the output of pd.read_excel() is a Python dictionary with sheet names as keys and corresponding DataFrames as corresponding values.

Instructions
-Assign the URL of the file to the variable url.
-Read the file in url into a dictionary xls using pd.read_excel() recalling that, in order to import all sheets you need to pass None to the argument sheet_name.
-Print the names of the sheets in the Excel spreadsheet; these will be the keys of the dictionary xls.
-Print the head of the first sheet using the sheet name, not the index of the sheet! The sheet name is '1700'
'''
# Import package
import pandas as pd

# Assign url of file: url
url = "http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls"

# Read in all sheets of Excel file: xls
xls = pd.read_excel(url, sheetname = None)

# Print the sheetnames to the shell
print(xls.keys())

# Print the head of the first sheet (using its name, NOT its index)
print(xls["1700"].head())



# HTTP requests to import files from the web
'''
Video
'''



# Performing HTTP requests in Python using urllib
'''
Now that you know the basics behind HTTP GET requests, it's time to perform some of your own. In this interactive exercise, you will ping our very own DataCamp servers to perform a GET request to extract information from the first coding exercise of this course, "https://campus.datacamp.com/courses/1606/4135?ex=2".
In the next exercise, you'll extract the HTML itself. Right now, however, you are going to package and send the request and then catch the response.

Instructions
-Import the functions urlopen and Request from the subpackage urllib.request.
-Package the request to the url "https://campus.datacamp.com/courses/1606/4135?ex=2" using the function Request() and assign it to request.
-Send the request and catch the response in the variable response with the function urlopen().
-Run the rest of the code to see the datatype of response and to close the connection!
'''
# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# This packages the request: request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Print the datatype of response
print(type(response))

# Be polite and close the response!
response.close()



# Printing HTTP request results in Python using urllib
'''
You have just packaged and sent a GET request to "https://campus.datacamp.com/courses/1606/4135?ex=2" and then caught the response. You saw that such a response is a http.client.HTTPResponse object. The question remains: what can you do with this response?
Well, as it came from an HTML page, you could read it to extract the HTML and, in fact, such a http.client.HTTPResponse object has an associated read() method. In this exercise, you'll build on your previous great work to extract the response and print the HTML.

Instructions
-Send the request and catch the response in the variable response with the function urlopen(), as in the previous exercise.
-Extract the response using the read() method and store the result in the variable html.
-Print the string html.
-Hit submit to perform all of the above and to close the response: be tidy!
'''
# Just started. Haven't complete the question.