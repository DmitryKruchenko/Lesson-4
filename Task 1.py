from sys import argv

print('Введите отработанные часы: ')
print('Введите часовую ставку: ')
print('Введите размер премии: ')

salary = (float(argv[1]) * float(argv[2])) + float(argv[3])
print('Размер заработной платы: ', salary)