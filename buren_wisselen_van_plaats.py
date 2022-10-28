# https://dodona.ugent.be/nl/courses/807/series/9108/activities/228235149

invoer = input('Geef lijst gehele getallen, gescheiden door spatie: ')
lijst_1 = invoer.split(' ')
lijst_2 = []
index = 0
while index <= len(lijst_1)-1:
    # print(len(lijst_1))
    if len(lijst_1)%2 != 0 and index == len(lijst_1)-1:
        lijst_2.append(lijst_1[index])
        index+=2


    else:
        lijst_2.append(lijst_1[index+1]+' '+lijst_1[index])


    index+=2
print(*lijst_2)
