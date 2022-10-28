# Write a program that asks for a digit followed by the input of 10 numbers.
# As a result you get the number of numbers that ends on this digit.
# Make sure that the output text changes appropriately when only 1 number ends on the final digit.

g = int(input('What final digit do you want to check the numbers on: '))
count = 0
for i in range (0,10):
    g1 = int(input('Enter a number: '))
    if g1%10 == g:
        count +=1
print('{} out of 10 numbers end on {}'.format(count,g))