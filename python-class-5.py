# Create random sentences

import sys
import random
import time
from flask import Flask

"""===========================================================================
Setting up functions to create words
==========================================================================="""

class CreateSentence:

	def __init__(self):
		self.histogram = self.create_histogram()
		self.weighted_words_list = self.weight_words()


	# Open file
	def get_source_file(self):
		text_file = open('sourcetext.txt', 'r')
		text = text_file.read().strip()
		text_file.close()
		return(text)

	# Turn file to list
	def text_to_list(self):

		source_text = self.get_source_file()

		source_text = source_text.replace('\n', ' ')
		source_text = source_text.replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace('--', ' ').replace('-', ' ').replace("'", '').replace('"', '')
		source_text = source_text.strip()
		source_text = source_text.lower()
		source_list = source_text.split(' ')

		return source_list

	# Returns dictionary{string: int}
	def create_histogram(self):

		my_list = self.text_to_list()

		histogram = {}
		for word in my_list:
			if word in histogram.keys():
				histogram[word] += 1
			else:
				histogram[word] = 1
		print(histogram)
		return histogram

	# Brian's implementation of weight words
	# Returns tokens, list[(string, int, int)]
	def weight_words(self):
		temp_value = 0
		tuple_list = []
		for key, value in self.histogram.items():
			new_tuple = (key, temp_value, temp_value + value - 1)
			tuple_list.append(new_tuple)
			temp_value += value
		return tuple_list

	# Returns word
	def get_random_word(self):
		tokens = self.weighted_words_list[len(self.weighted_words_list)-1][2]

		random_int = random.randint(0, tokens)
		for weighted_tuple in self.weighted_words_list:
			if random_int >= weighted_tuple[1] and random_int <= weighted_tuple[2]:
				return weighted_tuple[0]

	def create_sentence(self, num_of_words):
		sentence_list = []
		for i in range(0, num_of_words):
			sentence_list.append(self.get_random_word())
		my_sentence = ' '.join(sentence_list) + '.'
		return my_sentence

"""===========================================================================
Setting up Flask
==========================================================================="""

app = Flask(__name__)

wow = CreateSentence()

@app.route('/')
def main():
	return "Hello"

@app.route('/<words>')
def return_sentence(words):
	words = int(words)
	return wow.create_sentence(words)


if __name__ == '__main__':

	app.run()


