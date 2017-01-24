#

from hashtable import HashTable
from linkedlist import LinkedList
import random
import timeit

def list_of_words(num):
    word_file = open("words.txt")
    word_list = word_file.read().strip().split('\n')
    word_length = len(word_list)-1

    return_list = []
    for i in range(0, num):
        random_int = random.randint(0, word_length)
        random_word = word_list[random_int]
        return_list.append(random_word.rstrip())

    return return_list


# Set up word lists
hundred_words = list_of_words(100)
ten_thousand_words = list_of_words(10000)

# Set up models
hundred_ll = LinkedList(hundred_words)
ten_thousand_ll = LinkedList(ten_thousand_words)

# Search through hundred
hundred_search = hundred_words[-1]
stmt = "hundred_ll.find_item('{}')".format(hundred_search)
setup = "from __main__ import hundred_ll"
timer = timeit.Timer(stmt, setup=setup)

iterations = 10000
result = timer.timeit(number=iterations)
print("count time for 100-word linked list: " + str(result))

# Search through thousand
ten_thousand_search = ten_thousand_words[-1]
stmt = "ten_thousand_ll.find_item('{}')".format(ten_thousand_search)
setup = "from __main__ import ten_thousand_ll"
timer = timeit.Timer(stmt, setup=setup)

iterations = 10000
result = timer.timeit(number=iterations)
print("count time for 10000-word linked list: " + str(result))

# Set up models
hundred_ht = HashTable()
for word in hundred_words:
    hundred_ht.set(word, 1)
ten_thousand_ht = HashTable()
for word in ten_thousand_words:
    ten_thousand_ht.set(word, 1)

# Search through hundred
hundred_search = hundred_words[-1]
stmt = "hundred_ht.get('{}')".format(hundred_search)
setup = "from __main__ import hundred_ht"
timer = timeit.Timer(stmt, setup=setup)

iterations = 10000
result = timer.timeit(number=iterations)
print("count time for 100-word hash table: " + str(result))

# Search through thousand
ten_thousand_search = ten_thousand_words[-1]
stmt = "ten_thousand_ht.get('{}')".format(ten_thousand_search)
setup = "from __main__ import ten_thousand_ht"
timer = timeit.Timer(stmt, setup=setup)

iterations = 10000
result = timer.timeit(number=iterations)
print("count time for 10000-word hash table: " + str(result))

