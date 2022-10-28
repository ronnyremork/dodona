# https://dodona.ugent.be/nl/courses/807/series/9108/activities/1496650896
# -146 734 -169 217 -606 -596 49 -456 -521 -217 76
invoer = input('reeks met spatie: ')
lijst_1 = invoer.split(' ')
groter = 0
index = 1
while index < len(lijst_1)-1:
    if int(lijst_1[index]) > int(lijst_1[index-1]) and int(lijst_1[index]) > int(lijst_1[index+1]):
        groter+=1
    index+=1
print(groter)