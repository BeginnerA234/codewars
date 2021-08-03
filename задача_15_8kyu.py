# https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
def square_sum(numbers):
    # res = 0
    # for num in numbers:
    #     res += num*num
    # return res
    return sum(num*num for num in numbers)
print(square_sum([0, 3, 4, 5]))