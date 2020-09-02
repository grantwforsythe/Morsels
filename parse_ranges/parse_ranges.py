import re


def parse_ranges(arg):
	pairs = re.findall(r'\b(\d+)-(\d+)\b', arg)
	print(pairs)
	for val in arg.split(','):
		start, found, end = val.partition('-')
		if found:
			for x in range(int(start), int(end)+1):
				yield x
		else:
			yield int(start)



print(list(parse_ranges('1-2,4-4,8-10')))


# regex = r'\d[->]*\d*'

# # list(parse_ranges('0, 4-8, 20->exit, 43-45'))

# # test = re.findall(regex, '0, 4-8, 20->exit, 43-45')
# test = re.finditer(regex, '0, 4-8, 20->exit, 43-45'.replace(' ', ''))

# for m in test:
# 	print(m.group())