u1 = int(input('Geef het uur van het eerste tijdstip: '))
m1 = int(input('Geef de minuten uur van het eerste tijdstip: '))
s1 = int(input('Geef de seconden van het eerste tijdstip: '))
u2 = int(input('Geef het uur van het tweede tijdstip: '))
m2 = int(input('Geef de minuten van het tweede tijdstip: '))
s2 = int(input('Geef de seconden van het tweede tijdstip: '))

tijdverschil = ((u2*3600)+(m2*60)+s2)-((u1*3600)+(m1*60)+s1)
print(tijdverschil)