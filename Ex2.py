# Write a program to count how many zeros and sixes you can find in a number.
# Test with real numbers which do not start with the number 0.
# If you do enter a number starting with the digit 0, it will be omitted e.g. 0125 is stored as 125.
zero = six = 0
g = int(input('Geef een getal'))

while g > 0:
    rest = g %10
    if rest == 0:
        zero +=1
    elif rest==6:
            six += 1
    g = g//10

print('Aantal zessen',six,'Aantal zero\'s',zero)