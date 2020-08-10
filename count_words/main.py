from collections import Counter
import string
def count_words(sentence):
	# words = sentence.split()
	# words = map(lambda x: x.lower(), words)
	
	# for word in words:
	# 	dict_count[word.lower()] += 1
	return {
			word.strip(string.punctuation) : +1	
			for word in map(lambda x: x.lower(), sentence.split())

	}


if __name__ == '__main__':
	x = count_words("Oh what a day what a lovely day!")
	print(x)