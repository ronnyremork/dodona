text = input('Enter a text: ')
list_1 =[]
text = text.replace(' ','')
for i in text:
    if i not in list_1:
        list_1.append(i)
    list_1.sort()



print(list_1)
print(*list_1)
print(*list_1,sep='  ')

# a)	Write a program to read a piece of text and save the characters
#     (except spaces) in a List. Then print the List in three different ways.
# b)	Extend your program so that you only put a letter of the text in the List
# if that letter is not already there. Also sort your List before you print it.