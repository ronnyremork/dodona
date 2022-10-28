# Write a program to play Wheel of Fortune.
# In this word game you have to guess a proverb/sentence
# by entering a letter each time until you think you
# recognize the proverb/sentence.
# You may put the proverb hard coded in your program.
# Also the string that indicates how many words and
# letters the proverb consists of may be hard coded.

quote = 'keep looking up'
hidden = quote.replace('keep looking up','#### ####### ##')
letter = input('Guess a letter: ')
x = quote.index(letter,0,len(quote))


print(hidden)

