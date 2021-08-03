# https://www.codewars.com/kata/5bb904724c47249b10000131/train/python
def points(*games):
    result = 0
    for i in games:
        x,y = i.split(':')
        if x > y:
            result += 3
        elif x == y:
            result += 1
        else:
            pass
    return result

points('1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3')

