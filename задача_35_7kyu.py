# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

def accum(string):
    res = ''
    for i, s in enumerate(string):
        if i == 0:
            res = res + s.capitalize()
        else:
            res = res + '-' + (s * i).capitalize()
    return res


print(accum('ZpglnRxqenU'))
