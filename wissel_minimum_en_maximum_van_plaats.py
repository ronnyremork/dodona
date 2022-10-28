# https://dodona.ugent.be/nl/courses/807/series/9108/activities/594682185

invoer = input('reeks met spatie : ')
lijst_1 = invoer.split(' ')
for i in range(0,len(lijst_1)):
    lijst_1[i] = int(lijst_1[i])
min = max = lijst_1[0]
pos_min = pos_max = 0
dummy = 0
for i in range(0,len(lijst_1)):
    if lijst_1[i] < min:
        min = lijst_1[i]
        pos_min = i
    elif lijst_1[i] > max:
        max = lijst_1[i]
        pos_max = i
dummy = lijst_1[pos_min]
lijst_1[pos_min] = lijst_1[pos_max]
lijst_1[pos_max] = dummy
print(*lijst_1)


# print(min)
# print('index min = ',pos_min)
# print(max)
# print('index max = ',pos_max)
