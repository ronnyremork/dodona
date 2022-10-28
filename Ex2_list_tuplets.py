# Use a List of numbers in your program. Write a program that generates a new List that contains the same numbers
# but all even numbers are in the first part of the List and the odd numbers at the end.

list1 = [41,5,8,96,41,22,88]
list2= []

for i in list1:
    if i%2==0:
        list2.insert(0,i)
    else:
        list2.append(i)

print(list2)
