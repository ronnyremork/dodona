# Exercise 1
# Write a function that returns the number of degrees Fahrenheit (Tf) when the temperature in degrees
# Celsius (Tc) is given as a parameter.  Use this conversion formula between Tc and Tf : Tf = Tc * 9/5 +32
#
# Then use this function in the program below.

def temp_convert(c):
        f = c*9/5 +32
        return f
# main

celcius = int(input('Celcius: '))
fahrenheit = temp_convert(celcius)
print(celcius,'degrees Celsius =',fahrenheit,'degrees Fahrenheit')





