#


def expanded_form(num):
    num_str = str(num)
    length = len(num_str)
    b = length
    q = 0
    res = []
    while q != length:
        if b == 0:
            res.append(str(num_str[-1]))
        else:
            result = int(num_str[q:]) // 10**(b-1)
            if result == 0:
                pass
            else:
                res.append(str(result*10**(b-1)))
        q += 1
        b -= 1
    return ' + '.join(res)

print(expanded_form(70304))