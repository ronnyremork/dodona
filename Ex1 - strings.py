# Write a program to read a colour. Then print out the following information:
# -	The first and third letter of the colour
# -	How many letters the colour name consists of
# -	All the letters of the colour one by one with the ASCII code of each letter next to it (use a for)
# -	All the letters of the colour underneath each other (use a while).
# o	for the 1st, 3rd, 5th ... letter add # at the front and at the back
# o	for the 2nd, 4th, ... letter add ** at the front and at the back

colour = input('colour: ')
print(colour[0:3:2])
print(len(colour))
for i in colour:
    print(i,'=',ord(i),)

i = 0
while i < len(colour):
    if i%2 == 0:
        print('#'+colour[i]+'#')
    else:
        print('**'+colour[i]+'**')
    i+=1



# fruit = "aaldbei"
# fruit = fruit[:2] + "r" + fruit[3:]
# print( fruit )

# fruit = "banaan"
# print( fruit[::-1] )
# for i in range( 5, -1, -1 ):
#     print( fruit[i] )


# fruit = "banaan"
# print( fruit [::2] )
# print( fruit [1::2] )
# print( fruit[::-1] )
# print( fruit[::-2] )

# fruit = "aalbes"
# print( fruit[:] )
# print( fruit[0:] )
# print( fruit[:6] )
# print( fruit [:100] )
# print( fruit[:len( fruit )] )
# print( fruit[1:-1] )
# print( fruit[2], fruit [1:6] )