# https://dodona.ugent.be/nl/courses/807/series/9108/activities/515676861
# Opdracht
# Schrijf een programma dat volgende stappen doorloopt:
#
# De gebruiker voert, op 1 regel, een vrij te kiezen aantal gehele getallen in, oplopend gesorteerd en gescheiden door een spatie.
# Zorg dat de elementen uit de stringwaarde gehaald worden en in een lijst terecht komen.
# Tel het aantal verschillende waarden in de lijst.
# Invoer
# Eén stringwaarde die een vrij te kiezen aantal gehele getallen bevat, oplopend gesorteerd en gescheiden door een spatie.
#
# Uitvoer
# Eén natuurlijk getal –> het aantal verschillende waarden in de lijst.
#
# Voorbeeld 1
# Invoer
#
# -4 -3 -3 -3 0 0 0 1 1 1 2 2 3
# Uitvoer
6

# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

begin = input('Geef x aantal getallen, oplopend en geschieden door spatie: ')
lijst_1 = begin.split(' ')
# unique_list = list(set(lijst_1))
# counter = len(unique_list)
# print(counter)
unique_list=[]
i = 0
while i < len(lijst_1):
    if lijst_1[i] not in unique_list:
        unique_list.append(lijst_1[i])
    i+=1
print(len(unique_list))