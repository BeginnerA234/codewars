# https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python
from itertools import combinations

xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]


def choose_best_sum(t: int, k: int, ls: list):
    res = []
    for item in combinations(ls, k):
        if sum(item) > t:
            continue
        res.append(sum(item))
    if res:
        return max(res)
    return None


print(choose_best_sum(430, 8, xs))
