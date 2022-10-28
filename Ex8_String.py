# Write a program that reads a word and checks if the word in appears in the string
# in the first or second place.
# Use a String method for this.

text = input('Enter a word: ')
if text.find('in') in (0,1):
    print('ok')
elif text.find('in' ) == -1:
    print('no')
else:
    print('ok but not in 1 or 2 ')