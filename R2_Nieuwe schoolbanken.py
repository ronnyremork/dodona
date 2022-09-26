a = int(input('Aantal lln klas A: '))
b = int(input('Aantal lln klas B: '))
c = int(input('Aantal lln klas C: '))
banken = a // 2 + a % 2 + b // 2 + b % 2 + c // 2 + c % 2
print(banken)