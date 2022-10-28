# https://dodona.ugent.be/nl/courses/807/series/9104/activities/1050914274
k1 = int(input('k1: '))
r1 = int(input('r1: '))
k2 = int(input('k2: '))
r2 = int(input('r2: '))

if k1 % 2 == r1 % 2 and k2 % 2 == r2 % 2 or k1 % 2 != r1 % 2 and k2 % 2 != r2 % 2:
    print('DEZELFDE KLEUR')
else:
    print('VERSCHILLENDE KLEUR')