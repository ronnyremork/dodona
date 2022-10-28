# Write a program to read a series of numbers  (stop the input by entering 0).
# Print the largest number and the smallest number entered as well as the difference between those numbers

g = int(input('Enter a number: '))
g_groot  = 1
g_klein = 0

if g == 0:
    print('No numbers entered')
while g!=0:
    if g > g_groot:
        g_groot = g
    else:
        g_klein = g
    g = int(input('Enter a number: '))

print('The difference between the largets number {} and the smallest {} = {}' .format(g_groot,g_klein,g_groot-g_klein))