# Create random sentences

import sys
import random #from random import randint
import time

# Create Sentence
def get_word_list(file_name):
	words_file = open(file_name, 'r') #open(file_name) will also work -> only read
	words_list = words_file.read().strip().split('\n')
	#words_file.close() # -> will reduce performance
	return(words_list)

def get_word_list_2(file_name):
	words_file = open(file_name, 'r')
	words_list = words_file.readlines()
	#words_file.close() # -> will reduce performance
	return(words_list)

def get_word_list_3(file_name):
	words_file = open(file_name, 'r')
	words_list = words_file.read().splitlines()
	return(words_list)

def create_sentence(num_of_words):
	word_list = get_word_list_2('words.txt')
	word_length = len(word_list)-1
	my_sentence = []
	for i in range(0, num_of_words):
		random_int = random.randint(0, word_length)
		random_word = word_list[random_int]
		my_sentence.append(random_word.rstrip())
	my_sentence = ' '.join(my_sentence) + '.'
	return(my_sentence)

# Autocomplete Challenge
def autocomplete(first_characters):
	for i in get_word_list():

		# # Second try - much more effecient, around 0.056
		# if i[:len(first_characters)] == first_characters:
		# 	print(i)

		if i[:1] == first_characters[:1]:
			if i[:len(first_characters)] == first_characters:
				print(i)

def anagram(my_word):
	my_word = my_word.lower()

	# Set up a character dictionary
	characters_list = [char for char in my_word]
	character_dict = {}
	for character in characters_list:
		if character in character_dict.keys():
			character_dict[character] = character_dict[character] + 1
		else:
			character_dict[character] = 1

	return_list = []

	# Loop through all words
	for word in get_word_list():
		word = word.lower()

		# Continue if same word
		if word == my_word:
			continue

		# Make sure lengths are the same
		if len(word) == len(my_word):
			if all(char in word for char in character_dict.keys()):
				new_word_dict = {}
				for character in word:
					if character in new_word_dict.keys():
						new_word_dict[character] = new_word_dict[character] + 1
					else:
						new_word_dict[character] = 1

				if character_dict == new_word_dict:
					return_list.append(word)

	return(return_list)

def all_anagrams():

	anagram_dict = {}

	for word in get_word_list():
		print(word)
		anagrams_list = anagram(word)
		if anagrams_list:
			anagram_dict[word] = anagrams_list

	return(anagram_dict)

if __name__ == '__main__':
	t0 = time.time()

	num_of_words = int(sys.argv[1])
	sentence = create_sentence(num_of_words)
	print(sentence)

	t1 = time.time()
	print(t1 - t0)
