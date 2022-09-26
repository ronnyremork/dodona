x= int(input('Geef een getal kleiner dan 1000: '))
h = x//100
t1 = x%100
t2 = t1//10
e = t1%10

som = h+t2+e
print(som)
