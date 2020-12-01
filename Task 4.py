from random import randint


my_list = []
my_list_new = []
for i in range(20):
    my_list.append(randint(0, 100))

print(my_list)
for i in my_list:
    if i not in my_list_new:
        my_list_new.append(i)
print(my_list_new)
