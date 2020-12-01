from functools import reduce

def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el

my_list = []
for i in  range(100, 1002, 2):
    my_list.append(i)

print(my_list)
print(reduce(my_func, my_list))
