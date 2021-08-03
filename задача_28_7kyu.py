def word_pattern(word='Hippopotomotrosesquippedaliophobia'):
    d = {}
    res = []
    n=0
    for i in word.lower():
        if i in d:
            res.append(str(d[i]))
            continue
        else:
            d[i] = n
            n+=1
            res.append(str(d[i]))
    return '.'.join(res)


word_pattern('Hippopotomotrosesquippedaliophobia')