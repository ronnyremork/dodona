# https://dodona.ugent.be/nl/courses/807/series/9108/activities/1930940053
getallen = input('')
lijst = getallen.split()
lijst = list(map(int,lijst))
even_lijst=[]

for index in lijst:
    if index%2==0:
        even_lijst.append(index)
print(*even_lijst)