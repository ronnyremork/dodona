# Write a function to convert an amount in Euro into Dollar.
# The function has 2 parameters: the amount in Euro and the exchange rate of the day.
# The function returns the amount in Dollar.
# Then use this function in the program below.

def euro_usd_conv(eur,rate=1.2327):
    usd = eur*rate
    return usd
# main

eur = int(input('Euro\'s: '))
usd = euro_usd_conv(eur,)
print('Dollars:',usd)