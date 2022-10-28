# Exercise 4
# a)	Write a function generate_list that fills a list with a number of random integers between lower and upper limit.
# The number of generated numbers is given as a parameter as well as the lower and upper limit between which
# the generated numbers must fall. The generated list will be returned.
# For example:
# •	generate_list (5,1,3) returns a list of 5 numbers between 1 to 3 (inclusive)
# •	generate_list (10,5,7) returns a list of 10 numbers from 5 to 7 (inclusive)

from random import randint

def remove_duplicates(x):
    return list(dict.fromkeys(x))


def generate_list(a,b,c):
    d=0
    list=[]
    for i in range(a):
        if b < c:
            d = randint(b,c)
            list.append(d)
        else:
            print('Low needs to be smaller then High try again: ')
            a = int(input('Aantal nummers: '))
            b = int(input('Low: '))
            c = int(input('High: '))
    return list


a= int(input('Aantal nummers: '))
b= int(input('Low: '))
c= int(input('High: '))
my_list = generate_list(a,b,c)
print(my_list)
my_list = remove_duplicates(my_list)
print(my_list)


