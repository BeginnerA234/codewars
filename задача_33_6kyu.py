# https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python

BRACES = {"(":")", "{":"}","[":"]"}

def validBraces(string="()()()()()(((()){}{}[][[[]{}[]{}[(]{))"):
  waiting = []
  for l in string:
    if l in BRACES.keys():
      waiting.append(BRACES[l])
    elif not waiting or waiting.pop() != l:
      return False
  return not waiting

print(validBraces())