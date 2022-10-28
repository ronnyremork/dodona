# a) With this program you can calculate
# the product of a number of numbers. The program
# continues to ask the user for whole numbers until
# they enter a 0 (zero).

# When the user enters 0, the product is printed.

# b) Extend your exercise and print also how many
# numbers were entered.
total = product = 1
count = 0

g = int(input('Enter a number, stop bij entering a zero: '))

while g!=0:
    product*=g
    # total*=product
    # product = 1
    count+=1
    g = int(input('Enter a number, stop bij entering a zero: '))
print('The product is '+str(product))
print('The total used numbers is '+str(count))
