# Write a program to play 'Higher Lower’. ' \
# The computer takes a number for the player to guess. The game continues with
# tips like ‘Higher’ or ‘Lower’ until the player has guessed the number. ' \
# At that point the program prints out how many tips the player needed to get to the result.

number = 11
count = 0
g = int(input('Enter a positive numer: '))
while g != number:
    if g > number:
        print('Lower')
    else:
        print('Higher')
    count+=1
    g = int(input('Enter a positive numer: '))
print('You have guessed the number {} in {} turns' .format(number,count+1))