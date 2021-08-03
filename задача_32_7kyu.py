# https://www.codewars.com/kata/5a61a846cadebf9738000076/train/python

def accum(string):
	res = ''
	for i, s in enumerate(string):
		if i == 0:
			res = res + s.capitalize()
		else:
			res = res + '-' + (s * i).capitalize()
	return res

