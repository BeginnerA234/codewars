# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

def duplicate_count(text):
    res = 0
    text = text.lower()
    for i in text:
        if text.count(i)>1:
            res+=1
            text = text.replace(i,'')
    return res
print(duplicate_count("abcdabcd"))

