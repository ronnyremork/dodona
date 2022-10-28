# Write a program that allows the user to print a series of numbers on the screen,
# each time separated by 2 dots.
# The user first fills in a positive start number,
# then all numbers from that number up to and including 0 are printed on the screen.

g = int(input('Enter a number: '))
end = 0
for i in range (g,0,-1):
    print(str(i), end='..' )

    # Nog een 0 op einde

