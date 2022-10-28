# Exercise 1
# For this exercise you use the file first_names.txt.
# a)	Write a program that prints all first names without using a List.
# b)	Complete your program so that you print at the end: there are 353  first names in the file.
#
# c)	Customize your program so that you only print the first names that contain a letter z.

#demo1 :

# file = open('first_names.txt')
# print(file.read())
# file.close()

# demo2

# with open('first_names.txt') as file:
#     line = file.readline()
#     i=0
#     while line:
#         i+=i
#         print(line.rsplit())
#         line= file.readline()
#
#         deze optie is met een lijst. split maakt lijst.

with open('first_names.txt') as file:
    line = file.readline()
    count=0
    aantal_z = 0
    while line:
        if 'z' in line.lower():
            aantal_z+=1
            print(line,end='')
        line = file.readline()
        count+=1
    print('There are ',count,'first names in the file,',aantal_z,' wich contain a letter z')

