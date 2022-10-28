# https://dodona.ugent.be/nl/courses/807/series/9104/activities/361731995
g = int(input('Getal van 4 cijfers: '))
if g//1000 == g%10 and (g%1000)//100 == (g%100)//10:
    print('EEN CIJFERPALINDROOM')
else:
    print('GEEN CIJFERPALINDROOM')