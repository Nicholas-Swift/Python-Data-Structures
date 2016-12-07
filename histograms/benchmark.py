# A histogram structured as a hashtable

from hash_table_histogram import HashTableHistogram
from tuple_histogram import TupleHistogram
from dictionary_histogram import DictionaryHistogram
from linked_list_histogram import LinkedListHistogram
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

# Set up histograms
hundred_hgram = DictionaryHistogram(hundred_words)
ten_thousand_hgram = DictionaryHistogram(ten_thousand_words)

hundred_or_ten_thousand = False

if hundred_or_ten_thousand == True:
    # Words to search for
    hundred_search = hundred_words[-1]

    stmt = "hundred_hgram.count('{}')".format(hundred_search)
    setup = "from __main__ import hundred_hgram"
    timer = timeit.Timer(stmt, setup=setup)

    iterations = 10000
    result = timer.timeit(number=iterations)
    print("count time for 100-word histogram: " + str(result))
else:
    # Words to search for
    ten_thousand_search = ten_thousand_words[-1]

    stmt = "ten_thousand_hgram.count('{}')".format(ten_thousand_search)
    setup = "from __main__ import ten_thousand_hgram"
    timer = timeit.Timer(stmt, setup=setup)

    iterations = 10000
    result = timer.timeit(number=iterations)
    print("count time for 10,000-word histogram: " + str(result))

