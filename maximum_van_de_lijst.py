# # https://dodona.ugent.be/nl/courses/807/series/9108/activities/1227349963

getallen = input('Lijst gehele getallen met spatie: ')
getallen = getallen.split(' ')
lijst = list(map(int,getallen))
max = 0
index = 0
i=0
while i <= len(lijst)-1:
    if lijst[i] > max:
        max = lijst[i]
        index = lijst.index(lijst[i])
    elif len(lijst) == 1:
        max = lijst[i]
    i+=1
print(max,index)
