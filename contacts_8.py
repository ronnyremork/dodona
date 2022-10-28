
# input
# Anthoni;Erwin;erwinanthoni@itfactory.com;M
# Bastiaens;Nigel;bastiaens.nigel@itfactory.com;M
# Cardinaels;Seppe;seppe.cardinaels@itfactory.com;M

with open('contacts.csv') as file:
    line = file.readline()
    list_mannen = []
    list_vrouwen = []
    while line:
        line = line.rstrip()
        record = line.split(';')
        if record[3] == 'M':
            list_mannen.append(record[1]+' '+record[0])
        else:
            list_vrouwen.append(record[1]+' '+record[0])
        line = file.readline()
list_vrouwen.sort()
list_mannen.sort()

print(len(list_vrouwen),' Girls')
for name in list_vrouwen:
    print('\t',name)

print()

print(len(list_mannen),' Guys')
for name in list_mannen:
    print('\t',name)