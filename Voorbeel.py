total = count = 0
#read the first numer before the whiole
number = int(input('Enter a numer, stop by entering -1: '))

while number != -1:
        count += 1
        total += number
        #read the next number
        number =int(input('Enter a numer, stop by entering -1: '))

print('Sum of the', count, 'numbers =', total)