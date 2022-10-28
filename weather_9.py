# Exercise 9
# For this exercise you use the file weather_2018 08.csv.
# Write a program that prints the highest temperature reached during that period.
# print: The highest temperature in this period = 35.92 °C

with open('weather_2018 08.csv') as file:
    heading = file.readline()
    high_temp = 0
    line = file.readline()
    line.rstrip()
    while line:
        if line != '\n':
            record = line.split(';')
            if float(record[1])>high_temp:
                high_temp = float(record[1])
            line=file.readline()
    print('The highest temperature in this periode = {} °C'.format(high_temp))



