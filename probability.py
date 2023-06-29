import random, collections

array_of_numbers = []
count = {}

for i in range(10000000000000000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    array_of_numbers.append(abs(dice1 - dice2))

array_of_numbers.sort()
count = collections.Counter(array_of_numbers)

print(count)