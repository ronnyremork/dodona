# Exercise 1
# Write a function that returns the number of degrees Fahrenheit (Tf) when the temperature in degrees
# Celsius (Tc) is given as a parameter.  Use this conversion formula between Tc and Tf :
#
# Then use this function in the program below.
# tf = tc*9/5+32

def temp_convert(c):
    f=c*9/5+32
    return f
# main

celcius = int(input('Graden Celcius: '))
f = temp_convert(celcius)
print(f)
