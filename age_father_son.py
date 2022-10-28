with open('age_father_son.txt') as file:
    count=1
    lines = file.readlines()
    for line in lines:
        file = open('age_father_son_2.txt', 'a', encoding='UTF-8')
        if line != '\n':
            file.write(str(count)+'\t'+str(line))
        else:
            file.write(str(count)+'\t'+'\n')
        count+=1
        file.close()
