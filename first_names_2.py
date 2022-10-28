with open('first_names.txt') as file:
    lines = file.readlines()
    names = []
    for line in lines:
        # line = line.rstrip()
        names.append(line)
    print(*names)
    print(*names[-1::-1])