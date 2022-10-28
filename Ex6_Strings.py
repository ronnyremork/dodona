# Write a program to read a string and form a new string.
# The characters are changed into groups of 3.
# If there was abc in the original string, it will be bca in the new string.
# This process is repeated for all subsequent groups of 3. The last remaining (1 or 2) letters are simply added.

text = input('Enter a string: ')
new_text = ''
i=0

while i < len(text)-2:
    new_text += text[i+1]
    new_text += text[i+2]
    new_text+= text[i]
    i+=3

new_text += text[i:]
print(new_text)
