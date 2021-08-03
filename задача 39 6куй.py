# https://www.codewars.com/kata/60b7d7c82358010006c0cda5/train/python

test = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


def corner_fill(square):
    sq = square.copy()
    result = []
    while True:
        try:
            result.extend(sq.pop(0))
            for row in sq:
                result.append(row.pop(-1))
            result.extend([row.pop(-1) for row in sq][::-1])
            result.extend(sq.pop(0)[::-1])
        except IndexError:
            break
    return result

print(corner_fill(test))

