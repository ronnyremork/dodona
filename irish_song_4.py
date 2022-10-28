with open('irish_song.txt') as file:
    line = file.readline()
    shortest = line
    print(shortest)
    line = file.readline()
    while line:
        if len(line.rstrip()) < len(shortest):
            shortest = line.rstrip()
            print(shortest)
        line = file.readline()
print(len(shortest))
print(shortest)