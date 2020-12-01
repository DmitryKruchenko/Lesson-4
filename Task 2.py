from random import randint

my_list = []
my_list_new = []
for i in range(20):
    my_list.append(randint(0, 100))
j = 0
for k in my_list:
    if (k > j):
        my_list_new.append(k)
    j = k
print(my_list)
print(my_list_new)
