# file = open('schedule.txt')
# print(file.read())
# file.close()

# with open ('schedule.txt') as file:
#         print(file.read())

# with open('schedule.txt') as file:
#     # READ LINE BY LINE
#     line = file.readline()
#     while line:
#             # not empty
#             if line != '\n' :
#                 print(line.rstrip())
#             line = file.readline()

# 1: open file
with open('schedule.txt') as file:
# 2: read line by line
    line = file.readline()
    while line:
        if line != '\n':
            record = line.split(';')
            print(record[1],*record[2].rsplit())
        line = file.readline()

# with open('schedule.txt') as file:
# # read all lines and place them in a list of strings
#     lines = file.readlines()
#     for line in lines:
#         if line != '\n':
#             print(line, end='')

