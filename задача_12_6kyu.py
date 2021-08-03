def persistence(n):
    answer = 0
    str_n = str(n)
    while len(str_n) > 1:
        answer +=1
        result = 1
        for i in str_n:
            result *= int(i)
        str_n = str(result)
    return answer

print(persistence(39))
