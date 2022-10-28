# https://dodona.ugent.be/nl/courses/807/series/9105/activities/22171673
n = int(input('Geef een getal: '))
x = 0
y = 0
while y <= n:
    x += 1
    y = x**2
    if y<=n:
        print(y,end=' ')

# print het kwadraat van elk natuurlijk getal  zolang het kwadraat kleiner is dan N