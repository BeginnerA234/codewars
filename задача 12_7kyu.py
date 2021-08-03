# https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/python
def solve(s):
    s_lowercase=[]
    s_uppercase=[]
    for i in s:
        if i.islower(): # ПРОВЕРЯЕТ i в нижнем регистре или нет
            s_lowercase.append(i)
        elif i.isupper():
            s_uppercase.append(i)
    if len(s_lowercase)>=len(s_uppercase):
        return s.lower()
    else:
        return s.upper()
print(solve('QWEsad'))