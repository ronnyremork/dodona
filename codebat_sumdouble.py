#
# Given two int values, return their sum. Unless the two values are the same, then return double their sum.
#
#
# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

def sum_double(a,b):
    sum = a + b
    if a == b:
        sum = sum*2
    return sum

# main
assert(sum_double(2,2)) == 8
assert(sum_double(5,2)) == 7

# a = int(input('a: '))
# b = int(input('b: '))
# totaal = sum_double(a,b)
# print(totaal)