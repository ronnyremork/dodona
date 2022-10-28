# Exercise 3
# Use the file first_names.txt again.
# Read the complete file and put all the first names
# in a List. Print the names 10 by 10.

with open('first_names.txt') as file:
    lines = file.readlines()
    i=0
    while i < len(lines):
        print(lines[i].rstrip().ljust(13),end='')
        i+=1
        if i%10 == 0:
            print()


