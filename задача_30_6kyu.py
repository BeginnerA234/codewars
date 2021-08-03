# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python
def is_valid_walk(walk):
    print(walk)
    res = 0
    random_name = ''
    for i in walk:
        if i in random_name or len(random_name) == 0:
            random_name += i
            res += 1
        else:
            res -= 1

    if len(walk) == 10 and res == 0:
        return True
    else:
        return False

print(is_valid_walk(['s', 'e', 's', 's', 'n', 's', 'e', 'n', 'n', 's']))
