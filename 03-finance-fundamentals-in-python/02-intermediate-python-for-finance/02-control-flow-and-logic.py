# 02 Control Flow and Logic
'''
Through hands-on activities, you’ll discover how to use Boolean logic to determine truth and use comparison and equality operators to control execution in if-statements and loops.
'''



# Comparison operators
'''
Video
'''



# Equality across types
'''
The equality operator == can be used to test if two variables have the same value. What is the result of using the equality operator to compare a variable closing_price, which holds the floating point value for a stocks closing price, to the variable closing_time, which holds a datetime object with the time of closing as a value.

Possible Answers
-True
-False
-A TypeError complaining about comparing different types
-A warning message complaining about comparing different types

# False
'''



# Assignment and equality
'''
When looking at someone's wealth, a distinction between cash and non-cash securities is important. Savings and checking accounts are cash securities. Stock positions are non-cash. Imagine that as part of balancing a client's wealth portfolio, you are asked to compare their cash and non-cash securities. The variable non_cash is provided with the value of the non-cash securities.

Instructions
-Assign a value of 19.11 to the variable cash.
-Check if cash and non_cash have the same value.
-Assign to cash the value of non_cash.
-Confirm that cash and non_cash are equal.
'''
# Assign a value to cash.
cash = 19.11

# Check if cash is equal to non-cash
print(cash == non_cash)

# Assign the value of cash to be equal non-cash
cash = non_cash

# Check if cash is equal to non-cash
print(cash == non_cash)



# Comparing dividends
'''
Dividends are payments made to stockholders, usually from profits that are not re-invested in a company. It is important to identify which stocks are paying higher dividends when analyzing how to balance stocks in a portfolio. Let's say that in your role analyzing a client's portfolio, you are tasked with comparing dividends from different holdings. The values of these dividends are provided in the variables d1 and d2.

Instructions 1/2
-Find out if dividend d2 is greater than zero.
-See if dividend d1 is greater than d2.
Instructions 2/2
-Check that dividend 1 is at least 100 units.
-Check that dividend 1 is not more than dividend 2.
'''
# Check dividend is greater than zero
print(d2 > 0)

# Is dividend 1 is greater than dividend 2?
print(d1 > d2)

# Check dividend 1 is at least 100
print(d1 >= 100)

# Check dividend 2 is at least as much dividend 1
print(d1 <= d2)



# Boolean operators
'''
Video
'''



# Decisions with Boolean operations
'''
Boolean operations are used in Python to make decisions. Imagine that you work as an analyst identifying accounts that might potentially participate in stock trades. You might use this information to advise qualifying clients on market moves. The variable is_investment_account is supplied. It is set to True if the given account includes stock positions as part of it's holdings. The supplied variable balance_positive is set to True if the account has a positive cash balance, which could be used to purchase securities.

Instructions
-Print the value of the variable balance_positive.
-Set the variable potential_trade to True if the account is an investment account with a positive balance.
-Print the True if this is a potential trade.
'''
# Print the given variables
print(is_investment_account)
print(balance_positive)

# Decide if this account is cantidate for trading advice
potential_trade = is_investment_account and balance_positive

# Print if this represents a potential trade
print(potential_trade)



# Assigning variables with Boolean operators
'''
You can use the fact that and and or are short-circuit operators to assign objects to variables in intelligent ways. Pretend that you are deciding what actions you should take with a client's account based on what they entered in a web-form. Unfortunately, they could submit the form with this field empty, so you need to set a default action just in case. The supplied variable input_action has the contents submitted by the client. The supplied variable is_trading_day is True if today is a day that trades are possible.

Instructions
-If your client entered an action, assign it to the variable action. If they entered nothing, use the default action "Hold".
-Assign the action to the variable do_action if trades can be done today, otherwise assign it as False.
-Print the action that should be done.
'''
# Assign a default action if no input
action = input_action or "Hold"

# Print the action
print(action)

# Assign action only if trades can be made
do_action = is_trading_day and action

# Print the action to do
print(do_action)



# Negating with Boolean operators
'''
It is often the case that you need to combine Boolean operations to solve more complicated problems. Let's say that you need to know if you need to download the closing stock prices for today. You only want to do the operation if the markets have already closed. The closing prices are a list held in the provided variable closing_prices. The supplied variable market_closed is set to True once the markets close. Use Boolean operations and what you know about how objects evaluate in them to determine if you should download the data.

Instructions
-Set the variable not_prices to True if you do not have closing prices for today.
-Set the variable get_prices to True if the market is closed and you don't have closing prices yet.
'''
