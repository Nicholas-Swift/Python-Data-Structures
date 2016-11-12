# Randomly swap around words

import sys
import random

# Get command line arguments (without 1st arg - script name)
argument_list = sys.argv[1:]

def shuffle_list(my_list):

	# # Random.shuffle
	# random.shuffle(my_list)
	# return(my_list)

	# # First Attempt
	# new_list = []
	# while len(new_list) < len(my_list):
	# 	random_number = random.randint(0, len(my_list)-1)
	# 	if random_number not in new_list:
	# 		new_list.append(random_number)
	# for i in range(0, len(new_list)):
	# 	new_list[i] = my_list[new_list[i]]
	# return(new_list)

	# Best Attempt
	copy_list = my_list[:]
	shuffled_list = []
	while copy_list:
		random_number = random.randint(0, len(copy_list)-1)
		shuffled_list.append(copy_list.pop(random_number))
	return(shuffled_list)

# Reverse Word Challenge
def reverse_word(my_word):
	#reversed_word = ''.join(reversed(my_word)) # Easy to read
	reversed_word = my_word[::-1] # This is extended slice syntax. It works by doing [begin:end:step] - by leaving begin and end off and specifying a step of -1, it reverses a string.

	return(reversed_word)

# Reverse Sentence Challenge
def reverse_sentence(my_sentence):
	words = my_sentence.split(' ')
	reversed_sentence = ' '.join(reversed(words))
	return reversed_sentence

# Mad Libs Challenge
def mad_libs():
	print('Enter a noun: ')
	noun = input()
	print('Enter a verb: ')
	verb = input()
	print('Enter a noun: ')
	noun2 = input()

	print('The', verb, noun, 'ran away from the', noun2, '.')

# Anagram Challenges
def anagram_generator(my_word):
	characters_list = [char for char in my_word]
	new_word = ''.join(shuffle_list(characters_list))
	return new_word

if __name__ == '__main__':
	print(shuffle_list(argument_list))
	#print(reverse_word("Ready"))
	#print(reverse_sentence("This is Nick Swift"))
	#mad_libs()
	#print(anagram_generator('hello'))
