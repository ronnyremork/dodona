# Use a Tuple of at least 6 numbers in your program. Write the code to create a new Tuple containing all the numbers
# that appear after the last digit 4. Print the original Tuple and the new Tuple.
numbers = (4, 2, 3, 9, 1, 4)
print(numbers)
found = False
index = len(numbers)

while not found and index > 0:
    index-=1
    if numbers[index]==4
        found = True
if not found
    print('The number 4 does not appear in the Tuple')
else:
    partnumbers = numbers[index+1:len(numbers)]
    print()



