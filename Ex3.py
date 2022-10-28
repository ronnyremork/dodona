# Write a program that reads in your age and that of your father.
# # Then calculate when your father is exactly twice as old as you.

my_age = int(input('My age: '))
father_age = int(input('My fathers age: '))
count = 0
if father_age < my_age * 2:
    print('The situation is no longer possible for your ages')
else:
    while father_age - my_age != my_age:
        my_age +=1
        count += 1
    print('Within '+str(count)+' years your father will have twice your age\nYour father will be '+str(father_age)+' and you will be '+str(my_age))


