# A triple in a text is a character that occurs 3 times in a row.
# rite a program to count the number of triples in a text. The triples may overlap, as in the second example!
# Make sure that the answer you print is grammatically correct! (There is 1 triple – There are 4 triples)

text = input('Enter a text: ')
number_triplets = 0
i = 0

while i < len(text)-2:
    if  text[i] == text[i+1] and text[i]==text[i+2]:
        number_triplets+=1
    i+=1
if  number_triplets==0:
    print('There is no triple in this text')
elif number_triplets ==1:
    print('There is 1 triple in this text')
else:
    print('There are',number_triplets,' triples in this text')


