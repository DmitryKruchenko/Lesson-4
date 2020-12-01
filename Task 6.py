from itertools import count, cycle

my_list = []

for el in count(20):
    if el > 50:
        break
    else:
        my_list.append(el)
print(my_list)

my_list_new = ('red', 'yellow', 'green')
с = 0
for el in cycle(my_list_new):
    if с > 25:
        break
    print(el)
    с += 1
