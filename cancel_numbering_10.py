input = open('age_father_son_2.txt')
output = open('cancelnumbering.txt','w' , encoding='UTF-8')

lines = input.readlines()
for line in lines:
    if line !='\n':
        output.write(line[2:])
input.close()
output.close()

