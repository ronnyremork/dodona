# https://dodona.ugent.be/nl/courses/807/series/9105/activities/1774310070
d = 1
x = int(input('Distance first day of training: '))
y = int(input(' Give race distance: '))


while x < y:
    x=x+x/10
    d+=1
    if x>=y:
        print(d)