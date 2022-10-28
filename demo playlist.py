with open('playlist.txt') as file:
    lines = file.readlines()
    lines.sort()
    for line in lines:
        velden =   line.split(';')
        print(velden[0]+'\t'+velden[1]+'\t'+velden[2].rstrip().lower(),end='\n')