# https://dodona.ugent.be/nl/courses/807/series/9106/activities/1058737268
n = int(input(': '))
totaal = n + 1
print('<--- er zijn',n,'kaarten aanwezig ( van de',totaal,')')
count = 0
y = n
while count <= n-1:
    x = int(input(':'))
    print('<--- kaart nummer',x,'is er')
    count+=1

print(y)




# print('<--- er zijn',n-1,'kaarten aanwezig ( van de',n,')')


