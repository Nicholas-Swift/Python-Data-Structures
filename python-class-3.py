# Create random sentences

import sys
import random
import time

def get_source_file():
	text_file = open('sourcetext.txt', 'r')
	text = text_file.read().strip()
	text_file.close()

	print(text)

	return(text)

def text_to_list(source_text):
	# Remove new lines
	source_text = source_text.replace('\n', ' ')

	# Remove grammar
	source_text = source_text.replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace('--', ' ').replace('-', ' ').replace("'", '').replace('"', '')

	# Strip of white space on ends
	source_text = source_text.strip()

	# Turn to lower case
	source_text = source_text.lower()

	# Turn to list
	source_list = source_text.split(' ')

	return source_list

# Good -> Dict structure makes the most sense
#		> Only need word and count {word: count}
#		> Fast to get a word you know
#		> Helps prevent accidently duplicating words
#		> Easy to update

# Bad  -> If you need to sort, need to put it in an array
#		> Hard to search by value
#		> Not as space effecient

def histogram(source_text):

	source_list = text_to_list(source_text)

	# Dictionary
	word_count = {}
	for word in source_list:
		if word in word_count.keys():
			word_count[word] += 1
		else:
			word_count[word] = 1
	return(word_count)

def unique_words(histogram):
	return len(histogram)

def frequency(word, histogram):
	if word in histogram.keys():
		return histogram[word]
	else:
		return 0

# Challenge 2
def list_histogram(source_text):
	source_list = text_to_list(source_text)

	# List
	word_count = []
	for word in source_list:
		print(word)
		new_word = True
		for i in range(0, len(word_count)-1):
			if word == word_count[i][0]:
				word_count[i][1] += 1
				new_word = False
				break
		if new_word:
			word_count.append([word, 1])
	return(word_count)

def tuple_histogram(source_text):
	dict_histogram = histogram(text)
	tuple_histogram = dict_histogram.items()
	return tuple_histogram

# Challenge 3
def histogram_to_file(histogram, new_file_name):
	histogram_file = open(new_file_name, 'w')
	for key, value in histogram.items():
		print(key)
		histogram_file.write(key + ' ' + str(value) + '\n')
	histogram_file.close()

if __name__ == '__main__':
	t0 = time.time()

	# Code here
	text = get_source_file()

	histogram = histogram(text)
	print('histogram:')
	print(histogram)
	print('\n\n')

	print('unique word count:')
	print(unique_words(histogram))
	print('\n\n')

	print('\n\n\n\n\n\n\n\n\n')

	histogram_to_file(histogram, 'histogram.txt')

	# print('frequency of "mystery"')
	# print(frequency('mystery', histogram))
	# print('\n\n')

	t1 = time.time()
	print(t1 - t0)
