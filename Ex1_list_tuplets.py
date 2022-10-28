# Write a program to change the first and last element in a given (hard coded)
# list of strings. Print the List before and after the switch.

list = ['a','b','c','d','e','f']
dummy=list[0]
list[0]= list[len(list)-1]
list[len(list)-1]=dummy
print(list)
