# https://dodona.ugent.be/nl/courses/807/series/9108/activities/360836693
getallen = input('')
lijst = getallen.split()
lijst = list(map(int,lijst))
no_result = 0
i = 0
result=[]
x = True
for i in range(len(lijst)-1):
    if x == True:
        if (lijst[i] > 0 and lijst[i+1] > 0) or (lijst[i] < 0 and lijst[i+1] < 0) == True:
            result.append(lijst[i])
            result.append(lijst[i+1])
            x = False
            print(*result)
    else:
         i+=1
if x == True:
    print(no_result)









