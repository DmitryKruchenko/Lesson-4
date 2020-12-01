def fact(arg):
    res = 1
    i = 1
    while i <= arg:
        res = res * i
        i = i + 1
    return res

def generator(arg):
    for el in arg:
        yield el

my_list =[]
i = 1
while i <= 5:
    print(fact(i))
    my_list.append(fact(i))
    i = i + 1
print(my_list)

g = generator(my_list)

for i in g:
    print(i)









