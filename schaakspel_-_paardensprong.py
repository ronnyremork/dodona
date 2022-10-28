# https://dodona.ugent.be/nl/courses/807/series/9104/activities/851950642
k1 = int(input('Kolom 1: '))
r1 = int(input('rij 1: '))
k2 = int(input('Kolom 2: '))
r2 = int(input('rij 2: '))

if k2 == k1 + 2 or k2 == k1 -2 and r2 == r1 + 1:
    print('GELDIGE ZET')
elif k2 == k1 -2 or k2 == k1 + 2 and r2 == r1 - 1:
    print('GELDIGE ZET')
elif r2 == r1 + 2 or r2 == r1 - 2 and k2 == k1 - 1:
    print('GELDIGE ZET')
elif r2 == r1 + 2 or r2 == r1 - 2 and k2 == k1 + 1:
    print('GELDIGE ZET')
else:
    print('ONGELDIGE ZET')