# https://www.codewars.com/kata/550f22f4d758534c1100025a
def dirReduc(arr):
    print(arr)
    new_dict = {'NORTH': 'SOUTH',
                'SOUTH': 'NORTH',
                'EAST': 'WEST',
                'WEST': 'EAST'}
    res = []
    for i in arr:
        if res and res[-1] == new_dict[i]:
            res.pop()
        else:
            res.append(i)
    return res

print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))