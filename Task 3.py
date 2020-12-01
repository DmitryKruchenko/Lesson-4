from itertools import count

my_list = []
my_list_new = []
for el in count(20):
    if el > 241:
        break
    else:
        my_list.append(el)
print(my_list)
for i in my_list:
    if (i % 20 == 0 or i % 21 == 0):
        my_list_new.append(i)
    else:
        continue
print(my_list_new)