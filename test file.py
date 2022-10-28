# count = 1
# while count <= 6:
#     print(count, end='  ')
#     count+=1

getal = 0
som = 0
while getal >=0:
    som += getal
    getal = int(input('Geef een geheel getal in: ' ))

print('\nDe som van de ingegevens getallen ( uitgezonderd de waarde -1) bedraagt: ' +str(som+getal)+ "!")