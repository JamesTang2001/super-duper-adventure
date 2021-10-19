# 01 Welcome to Python
'''
This chapter is an introduction to basics in Python, including how to name variables and various data types in Python.
'''



# Welcome to Python for Finance!
'''
Video
'''



# Why might you use Python in finance?
'''
Python is routinely used in financial quantitative analyses. What applications might you use Python for in finance?

Possible Answers
-To compile monthly sales reports
-To optimize an investment strategies performance
-Visualizing stock data trends
-All of the above

# All of the above
'''



# Run code vs. submit answer
'''
On the right, you'll see the area where you can write and execute Python scripts and the IPython console. In this exercise, you will practice submitting code. The output of this code will be shown in the IPython Shell. The IPython Shell can also be used interactively to type and execute commands. The code entered directly in IPython shell is not checked for correctness, so it is a great place to experiment.
You can submit your script to check for correctness by hitting Submit Answer. Note that you can also use Take Hint or Show Answer if you're stuck.

Instructions
-Hit the Run Code button and observe that the code in your script is executed in the IPython Shell.
-Next, hit the Submit Answer to execute the code and check it against the solution.
'''
# Example 1, do not modify!
print(8 / 2)

# Example 2, do not modify!
print(2**2)



# Comments and variables
'''
Video
'''



# Printing output
'''
The print() function in a Python script explicitly prints the output. It is time to write your first line of Python code with and without the print() function to observe how it impacts the output of a script.

Instructions 1/2
-Write a command that adds 10 and 2.
Instructions 2/2
-Write a command that multiplies 10 and 2.
-Print this output explicitly.
'''
# Addition, no print output
10 + 2

# Multiplication, with print output
print(10 * 2)



# Finding the average revenue
'''
Variables can be used to store information and efficiently recover and manipulate stored values.
The revenue of three companies have been stored in three variables: revenue_1, revenue_2, and revenue_3.
Let's calculate the total revenue and the average revenue of these companies.

Instructions 1/2
-Create a new variable, total that represents the sum of revenue_1, revenue_2 and revenue_3.

Instructions 2/2
-Find the average of total.
'''
# Print the total revenue
total = revenue_1 + revenue_2 + revenue_3
print(total)

# Print the average revenue
average = total / 3
print(average)



# Data types
'''
Videos
'''



# Creating variables
'''
Variables in Python hold a value that may consist of varying data types. Variable names can contain letters, underscores, and numbers.
Let's create three types of Python variables that might be useful in finance.

Instructions 1/3
-Assign the string 'Apple' to the variable company_1.
Instructions 2/3
-Assign the integer 2017 to the variable year_1.
Instructions 3/3
-Assign the float 229.23 to the variable revenue_1.
'''
# Create company_1
company_1 = "Apple"
print(company_1)

# Create year_1
year_1 = 2017
print(year_1)

# Create revenue_1
revenue_1 = 229.23
print(revenue_1)



# Determining types
'''
Python has a built-in command type() that can determine the type of a variable or literal value. Let's determine the data types of the variables you created in the last exercise.

Instructions
-Print the data types associated with the variables company_1, year_1 and revenue_1.
'''
# Type of company_1
print(type(company_1))

# Type of year_1
print(type(year_1))

# Type of revenue_1
print(type(revenue_1))



# Booleans in Python
'''
Booleans are used to represent True or False statements in Python. Boolean comparisons include:

operators   descriptions
>	greater than
>=  greater than or equal
<	less than
<=	less than or equal
==	equal
!=	does not equal

Let's use boolean comparison operations to assess the revenues of three companies.

Instructions 1/2
-The name of company 1 is provided as company_1. Determine if the variable test_company is equivalent to company_1.
Instructions 2/2
-The revenue of company 1 and company 2 are provided as revenue_1 and revenue_2, respectively. Using a comparison operator, determine if revenue_1 is greater than revenue_2.
'''
# Test equality
test_company = 'apple'
print(company_1 == test_company)

# Compare revenue_1 and revenue_2
print(revenue_1 > revenue_2)



# Combining data types
'''
Different types of data types have different properties. For example, strings and floats cannot be mathematically combined. To convert a variable x to an integer, you can use the command int(x). Similarly, to convert a variable y to a string, you can use the command str(y).
It's time for you to change some data types to complete and print a statement.
The variables company_1, year_1, and revenue_1 are available in your workspace.

Instructions
-Convert the data type of variables year_1, and revenue_1 to string.
-Use these new variables to create and print the following sentence: "The revenue of Apple in 2017 was $229.23 billion."
'''
# Update data types
year_1_str = str(year_1)
revenue_1_str = str(revenue_1)

# Create a complete sentence combining only the string data types
sentence = 'The revenue of ' + company_1 + ' in ' + year_1_str + ' was $' + revenue_1_str + ' billion.'

# Print sentence
print(sentence)
