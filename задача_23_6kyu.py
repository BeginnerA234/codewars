# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

def find_outlier(number):
    even = []
    odd = []
    for i in number:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    if len(even)>len(odd):
        return odd[0]
    else:
        return even[0]

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
