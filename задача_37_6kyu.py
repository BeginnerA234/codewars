# https://www.codewars.com/kata/59aa6567485a4d03ff0000ca/train/python
from math import floor, sqrt
from datetime import datetime


def timeit(func):
    def psd(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        print(datetime.now() - start)
        return res

    return psd


def _counter(prime_list):
	result = 0
	for i in prime_list:
		test_list = []
		n, k = i, 0
		while n != 1:
			if n in test_list:
				result -= 1
				break
			for num in str(n):
				k += int(num) ** 2
			
			test_list.append(n)
			n, k = k, 0
		result += 1
	return result


@timeit
def prime_number(a, b):
	sieve = set(range(2, b))
	for i in range(2, floor(sqrt(b)) + 1):
		if i in sieve:
			sieve -= set(range(2 * i, b, i))
	sieve -= set(range(2, a))
	return _counter(sieve)


print(prime_number(1, 25))
