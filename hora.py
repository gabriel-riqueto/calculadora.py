horas= int(input('Digite as horas: '))
min= int(input('Digite os minutos: '))
if horas >= 0 and horas <= 23 and min >=0 and min <=59:
    print(f'As horas são {horas}:{min}')
else:
    print('Horas invalidas')

