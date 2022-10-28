# Write a program to read an odd-length string. Print the middle three characters of this string.
# You may assume that the string contains at least 3 characters.

word = input('Enter a word: ')
number = len(word)//2
print(word[number-1:number+2])
