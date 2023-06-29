from functools import reduce
import itertools

def choose_best_sum(max_distance, towns, ls):
    perms = list(itertools.combinations(ls, towns))
    total_distance_perms = list()
    for tuple in perms:
        total_distance_perms.append(reduce(lambda prev, curr: prev + curr, tuple))
    total_distance_perms = list(filter(lambda i: i <= max_distance, total_distance_perms))
    return max(total_distance_perms) if len(total_distance_perms) > 0 else None

xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print(choose_best_sum(230, 4, xs))