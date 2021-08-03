# def multiply(a, b):
#     return a*b
# print(multiply(3,4))

# Ваша цель в этом ката-реализовать функцию разности,
# которая вычитает один список из другого и возвращает результат.
# Он должен удалить все значения из списка а, которые присутствуют в списке В.
# Если значение присутствует в b, то все его вхождения должны быть удалены из другого значения.:


def array_diff(a, b):
    set_b = set(b)
    return [i for i in a if i not in set_b]  # сделали еще короче

    # c = [i for i in a if i not in set_b] # записали 1 строчкой
    # return c

    # for i in a:
    #     if i not in b:
    #         c.append(i)
    # return c

# print(array_diff([1, 2],[1]))
# print(array_diff([1, 2, 2],[1]))
# array_diff([1, 2, 2],[2])
# array_diff([1, 2, 2],[])
# array_diff([],[1, 2])

# a = [1,2,3,4,5,6,7]
# b = [3,5,6]
# c = [i for i in a if i not in b]
# print(c)
