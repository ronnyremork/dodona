# https://dodona.ugent.be/nl/courses/807/series/9104/activities/247466074
g = int(input('Geef een cijfer bestaande uit 3 verschillende getallen: '))
if g//100 >= ((g%100)//10) or ((g%100)//10) >= g%10:
    print('NIET (!) STIJGEND')
else:
    print('STIJGEND')

