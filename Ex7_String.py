# Write a program that reads a string and prints how big the largest block of characters is.
# A block is a series of characters that lie next to each other and are the same.
# You may assume the string isn't empty.

text = input('Enter a text: ')
block_size = 1
largest = 1

for i in range(len(text)-1):
    if text[i]==text[i+1]:
        block_size+=1
    else:
        block_size=1
    if block_size>largest:
        largest=block_size

print('The length of the largest block in this text is', largest)

