# https://dodona.ugent.be/nl/courses/807/series/9108/activities/515676861

invoer = input('reeks gehele getallen, spatie gescheiden: ')
lijst_1 = invoer.split(' ')
lijst_1.sort()
lijst_2= []
count=0
for getal in lijst_1:
    if getal:
        if getal not in lijst_2:
            lijst_2.append(getal)
            count+=1
print(count)