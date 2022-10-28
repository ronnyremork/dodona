# https://dodona.ugent.be/nl/courses/807/series/9104/activities/708567172
k1 = int(input(' Geef kolom1: '))
r1 = int(input('Geef rij1: '))
k2 = int(input('Geef kolom2: '))
r2 = int(input('Geef rij2: '))

if k2 != k1 and r1==r2:
    print('GELDIGE TORENZET')
elif r2!=r1 and k2==k1:
    print('GELDIGE TORENZET')
else:
    print('ONGELDIGE TORENZET')
