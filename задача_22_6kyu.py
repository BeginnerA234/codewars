# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

def solution(number):
#     res = []
#     for i in range(0,number):
#         if i%3 == 0 or i%5==0:
#             res.append(i)
#     return sum(res)
    return sum([i for i in range (0,number) if i%3==0 or i%5==0])