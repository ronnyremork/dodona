x = int(input('Geef een natuurlijk getal: '))
x2 = x//100
t1 = x%100
t2 = t1//10
e = t1%10
e_nieuw = e*10
t_nieuw = t2
x_nieuw = x2*100 + e_nieuw+t_nieuw
print(x_nieuw)