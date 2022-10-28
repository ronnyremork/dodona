# https://dodona.ugent.be/nl/courses/807/series/9108/activities/1710627294

lijst_1 =[]
invoer = input('Geef getallen gescheiden door een spatie: ')
lijst_1 = invoer.split(' ')
index=0
while index < len(lijst_1):
    if int(index)%2==0:
        print(lijst_1[index]+' ',end='')
    index+=1