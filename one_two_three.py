from random import randint
import collections

def one_two():
    return randint(1, 2)

def one_two_three():
    a,b = one_two(),one_two() - 1
    return one_two_three() if a == b else a + b

list_1 = list()
new_list = list()
for i in range(1000):
    list_1.append(one_two_three())

for i in range(1000):
    new_list.append(randint(1, 3))

print(dict(collections.Counter(list_1)))
print(dict(collections.Counter(new_list)))