x = int(input('Wat is het gehele deel van de prijs van een koekje: '))
z = int(input('Wat is het decimale deel van de koekjesprijs: '))
y = int(input('Hoeveel koekjes: '))
print(int((x*y) + ((z/100)*y))//1,(z*y)%100)