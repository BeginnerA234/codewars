
# чужое решение
# from itertools import count, filterfalse
#
# def next_id(arr):
#     return next(filterfalse(set(arr).__contains__, count()))

# def next_id(arr):
#     t = 0
#     while t in arr:
#         t +=1
#     return t


# def next_id(arr):
#     '''Возвращает первое пропущенное число'''
#     arr.sort()
#     if not arr or arr[0] != 0:   # Если поле отсутствует или 1 по индексу элемент не равен 0
#         return 0
#     for i in range(len(arr) - 1):
#         if arr[i] - arr[i+1] < -1:
#             return arr[i] + 1
#     return arr[-1] + 1

arr = [1,2,3,4,5,6,7,8,8]
print(range(len(arr) - 1))
#
#
#
# print(next_id([4,0,1,2,3,4,4,4,2,90]))
# print(next_id([0,1,2,3,4,5,6,7,8]))
# print(next_id([]))




