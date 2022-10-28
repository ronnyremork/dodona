# Exercise 3
# For this exercise you first write the function press_square(). This function has 2 parameters: a number and a character.
# •	The number stands for the number of characters per line and the number of lines to be printed.
# •	The character determines the character to print.
#
# For example: number= 5, character =  '*': the function prints 5 lines with 5 asterisks per line.
# Write a program in which the character to be used and the desired number are entered first.
# Then use the function to press the square.
#
# After the square has been printed, ask again which character you want to form lines
# with and the number of characters per line.
# The program will keep running as long as the user does not press enter at the question
# 'Give the character with which the lines are formed (enter = stop):'.
# When the user presses enter, the question about the number of characters will of course no longer be asked.

def press_square(c,n):
    for i in range(n):
        x=c*n
        print(x)
# main
char = input('Char: ')
while char:
    num = int(input('Number: '))
    press_square(char,num)
    char = input('Char: ')
