# 12:59;Ace Of Base;THE SIGN
# 12:55;NENA & KIM WILDE;ANYPLACE ANYWHERE ANYTIME
# 12:51;NATHANIEL RATELIFF;I NEED NEVER GET OLD

# to
#
# 12:33      MILK INC (storm)
# 12:36      NIALL HORAN (this town)
# 12:40      Calvin Harris (blame)

with open('playlist.txt') as file:
    all_lines = file.readlines()
    all_lines.sort()
    for line in all_lines:
        if line != '\n':
            result = line.split(';')
            print(result[0].ljust(10),result[1],'({}) '.format(result[2].lower().rstrip()))
