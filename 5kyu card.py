from collections import defaultdict
CARD = 'A23456789TJQK'
SYMBOL = 'cdhs'

array_test = []

for i in SYMBOL:
    for j in CARD:
        array_test.append(f'{j}{i}')

def encode(cards):
    return sorted([array_test.index(i) for i in cards])

def decode(cards):
    return [array_test[i] for i in sorted(cards)]