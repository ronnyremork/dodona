# https://dodona.ugent.be/nl/courses/807/series/9108/activities/442563744

invoer = input('Reeks getallen gescheiden door spatie: ')
lijst_1 = invoer.split(' ')
index = 1
while index < len(lijst_1):
    if int(lijst_1[index]) > int(lijst_1[index-1]):
        print(lijst_1[index]+' ',end='')
    index+=1
