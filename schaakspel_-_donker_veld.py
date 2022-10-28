# https://dodona.ugent.be/nl/courses/807/series/9104/activities/72628368
k = int(input('geef kolom : '))
r = int(input('geef rij: '))
if k % 2 == r % 2 :
    print('DONKER VELD')
else:
    print('LICHT VELD')