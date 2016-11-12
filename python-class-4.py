# Create random sentences

import sys
import random
import time

args = sys.argv[1:]

def create_histogram(my_list):
	histogram = {}
	for word in my_list:
		if word in histogram.keys():
			histogram[word] += 1
		else:
			histogram[word] = 1
	return histogram

def weight_words_lazy(histogram):
	weighted_words_list = []
	for key, value in histogram.items():
		for i in range(0, value):
			weighted_words_list.append(key)

	random_int = random.randint(0, len(weighted_words_list)-1)
	random_word = weighted_words_list[random_int]
	return random_word

def weight_words_not_as_lazy(histogram):
	tokens = 0
	for value in histogram.values():
		tokens += value

	tempNum = 0
	weighted_words = {}
	for key in histogram.keys():
		tempNum2 = tempNum
		weighted_words[key] = []
		for i in range(tempNum, tempNum2 + histogram[key]):
			weighted_words[key].append(i)
			tempNum += 1

	print(weighted_words)

	randomNumber = random.randint(0, tokens-1)
	for key, value in weighted_words.items():
		if randomNumber in value:
			return key

def weight_words_brian(histogram):
	tokens = 0
	for value in histogram.values():
		tokens += value

	temp_value = 0
	tuple_list = []
	for key, value in histogram.items():
		new_tuple = (key, temp_value, temp_value + value - 1)
		tuple_list.append(new_tuple)
		temp_value += value
	print(tuple_list)

	random_int = random.randint(0, tokens-1)
	for i in tuple_list:
		if random_int >= i[1] and random_int <= i[2]:
			return i[0]


if __name__ == '__main__':
	t0 = time.time()

	test_list = []

	# Code here
	histogram = create_histogram(args)
	random_word = weight_words_brian(histogram)
	print(random_word)

	t1 = time.time()
	print(t1 - t0)
