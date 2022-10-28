# Use a List of numbers in your program.
# Write a program that replaces every 0 in the list with the largest odd number
# you can find on the right side of that 0. If there is no odd number to be found then the 0 just remains.

my_list = [0,42,18,17,0,2,19,10,5,14]
print(my_list)

for index in range(len(my_list)-1):
    if my_list[index] == 0:
        largest_odd = 0
        for i in range(index+1,len(my_list)):
            if my_list[i]%2 != 0 and my_list[i]>largest_odd:
                largest_odd=my_list[i]
        my_list[index] = largest_odd
print(my_list)
