# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
def move_zeros(array):
    result = []
    for i in array:
        if i != 0 or i is False:
            result.append(i)
    for i in array:
        if i == 0 and i is not False:
            result.append(0)
    return result

print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))


# def move_zeros(array):
#     for i in array:
#         if i == 0 and i is not False:
#             array.remove(i)
#             array.append(0)
#     return array
#
# print(move_zeros([1,1,2,1,False,0,2,1]))





