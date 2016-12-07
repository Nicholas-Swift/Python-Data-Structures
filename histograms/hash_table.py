# A hashtable

from linked_list import LinkedList

class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        # Best: Omega(1)
        # Worst: O(n) (init size)

        self.buckets = [LinkedList() for i in range(init_size)]
        self.entries = 0
        self.load = self.entries / len(self.buckets)
        self.max_load = 0.75

    def __iter__(self):
        for bucket in self.buckets:
            if bucket:
                for item in bucket:
                    yield item

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        # Best: Omega(1)
        # Worst: O(1)

        return hash(key) % len(self.buckets)

    def _bucket(self, key):
        """Return the bucket where the given key would be stored"""
        # Best: Omega(1)
        # Worst: O(1)

        index = self._bucket_index(key)
        return self.buckets[index]

    def _update_entries(self, number_added):
        """Update the number of entries and update the load, resize if needed"""
        # Best: Omega(1)
        # Worst: O(1)

        self.entries += number_added
        self.load = self.entries / float(len(self.buckets))

        if self.load > self.max_load:
            self._resize_up()

    def _resize_up(self):
        """The load factor is greater than 0.75! Resize and Rehash! Resize and Rehash it all!"""
        # Best: Omega(n)
        # Worst: O(n)

        new_length = len(self.buckets)*2

        # Create new buckets list, recalculate load with new_length
        new_buckets = [LinkedList() for i in range(new_length)]
        self.load = self.entries / new_length

        # Iterate through current items and add to new buckets
        for item_key, item_value in self.__iter__():
            index = hash(item_key) % new_length
            new_buckets[index].append((item_key, item_value))

        self.buckets = new_buckets
        return

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        bucket = self._bucket(key)
        for item_key, item_value in bucket:
            if key == item_key:
                return True

        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""

        # Find bucket
        bucket = self._bucket(key)

        # Check if key is already in bucket
        for item_key, item_value in bucket:
            if key == item_key:
                return item_value

    def set(self, key, value):
        """Insert or update the given key with its associated value"""

        # Find bucket
        bucket = self._bucket(key)

        item = bucket.find(lambda x: x[0] == key)
        new_tuple = (key, value)

        if item is not None:
            bucket.delete(item)
            bucket.append(new_tuple)
        else:
            bucket.append(new_tuple)
            self._update_entries(1)

        return

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        bucket = self._bucket(key)

        item = bucket.find(lambda x: x[0] == key)
        if item is not None:
            bucket.delete(item)
            self._update_entries(-1)
            return
        else:
            raise KeyError('Key is not in HashTable')

    def keys(self):
        """Return a list of all keys in this hash table"""
        keys = []
        for item_key, item_value in self.__iter__():
            keys.append(item_key)
        return keys

    def values(self):
        """Return a list of all values in this hash table"""
        values = []
        for item_key, item_value in self.__iter__():
            values.append(item_value)
        return values

    def items(self):
        items = []
        for item in self.__iter__():
            items.append(item)
        return items

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

