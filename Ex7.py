# a)	Write a program that calculates the sum of all numbers between 25 and 32 (including the boundaries).
count = 25
for i in range (26,33):
    print(i,end='-->')
    print(i+count)
    count+=i