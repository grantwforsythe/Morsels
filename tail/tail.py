def tail(sequence, index=0):
	if index <= 0:
		return []

	result = [
			x
			for x in sequence
		] 

	if index >= len(result):
		return result
	else:
		return result[len(result)-index:]

if __name__ == '__main__':
	print(tail([1,2,3,4,5], 3))
	print(tail('hello', 2))
	print(tail('hello', 0))

	squares = (n**2 for n in range(10))
	print(tail(squares, 3))


	print(tail([1,2,3,4], 5))