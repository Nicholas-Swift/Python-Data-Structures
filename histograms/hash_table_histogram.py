# A histogram structured as a hashtable

from hash_table import HashTable
import random
import timeit

class HashTableHistogram(HashTable):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new list; update with given items"""
        super(HashTableHistogram, self).__init__()
        
        self.types = 0
        self.tokens = 0

        if iterable:
            self.update(iterable)

    def __repr__(self):

        items = []
        for item in self:
            items.append(item)
        items_str = " ".join(map(str, items))
        return items_str

    def insert(self, item):
        """Insert a single item to this histogram"""

        old_item = self.get(item)
        if old_item is not None:
            self.set(item, old_item + 1)
        else:
            self.set(item, 1)
            self.types += 1
        self.tokens += 1

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            self.insert(item)

    def remove(self, item):
        """Delete the item from this histogram"""
        self.delete(item)

    def count(self, item):
        old_item = self.get(item)
        return ((item, old_item))


if __name__ == '__main__':

    # Create word string and list
    word_string = "one fish two fish red fish blue fish"
    word_list = word_string.split(' ')

    print("List to add...")
    print(word_string)

    print("\n")

    # Add to DictionaryHistogram
    hist = HashTableHistogram(word_list)

    print("types...")
    print(hist.types)

    print("\n")

    print("tokens...")
    print(hist.tokens)

    print("\n")

    print("histogram...")
    print(hist)

    