# https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111/train/python
from collections import Counter

def triangle(row):
	if len(row) == 1:
		return row
	my_dict = {
		'RB': 'G', 'BG': 'R', 'RG': 'B',
		'BR': 'G', 'GB': 'R', 'GR': 'B',
		'GG': 'G', 'RR': 'R', 'BB': 'B',
	}
	string = ''.join(row)
	res_string = ''
	while len(res_string) != 1:
		res_string = ''
		for id, s in enumerate(string):
			if id != (len(string)-1):
				conc = string[id]+string[id+1]
				res_string += res_string.join(my_dict[conc])
			else:
				pass

		string = ''.join(res_string)

	return res_string
	# """GENIUS IDEA MY IDEA"""
	# my_dict_first = {
	# 	'RB': 'G', 'BG': 'R', 'RG': 'B',
	# 	'BR': 'G', 'GB': 'R', 'GR': 'B',
	# }
	# my_dict = Counter()
	# key = ''
	# for i in set(row):
	# 	my_dict[i] = row.count(i)
	# if len(my_dict) == 1:
	# 	for k, v in my_dict.most_common(1):
	# 		return k
	# elif len(my_dict) == 2:
	# 	for k, v in my_dict.most_common(2):
	# 		key += key.join(k)
	# 	return my_dict_first[key]
	# else:
	# 	if my_dict.most_common()[0][1] != my_dict.most_common()[1][1]:
	# 		for k, v in my_dict.most_common(1):
	# 			return row[v]
	# 	else:
	# 		for k, v in my_dict.most_common(2):
	# 			key += key.join(k)
	# 		return my_dict_first[key]
			
			# return row[value]
	
		
		
	
	
print(triangle('GRGRR'))
