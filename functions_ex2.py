# Exercise 2
# Write a function to convert an amount in Euro into Dollar. The function has 2 parameters:
# the amount in Euro and the exchange rate of the day. The function returns the amount in Dollar.
# Then use this function in the program below.

def euro_to_dollar(euro,rate=1.2327):
    dollar = euro*rate
    return dollar

# main

euro = int(input("Euro: "))
dollar = euro_to_dollar(euro)
print(dollar)



