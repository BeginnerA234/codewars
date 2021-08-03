# https://www.codewars.com/kata/550498447451fbbd7600041c/train/python

def comp(array1, array2):
    if array1==None or array2 == None:
        return False
    elif array1 == []:
        if array1==array2:
            return True
        return False
    for i in array1:
        if i*i in array2:
            array2.remove(i*i)
        else:
            return False
    return True
