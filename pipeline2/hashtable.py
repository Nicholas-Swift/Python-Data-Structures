# A Hash Table

from doublylinkedlist import DoublyLinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [DoublyLinkedList() for i in range(init_size)]
        self.entries = 0
        self.load = self.entries / len(self.buckets)
        self.max_load = 0.75

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(self.length())

    def __contains__(self, key):
        """Does it contain the item"""
        bucket = self._bucket(key)

        for item_key, item_value in bucket:
            if key == item_key:
                return True
        return False

    def __iter__(self):
        """Iterate through the hash table"""
        for bucket in self.buckets:
            if bucket:
                for item in bucket:
                    yield item

    def _update_entries(self, number_added):
        """Update the number of entries and update the load, resize if needed"""
        self.entries += number_added
        self.load = self.entries / float(len(self.buckets))

        if self.load > self.max_load:
            self._resize_up()

    def _resize_up(self):
        """The load factor is greater than 0.75! Resize and Rehash! Resize and Rehash it all!"""
        new_length = len(self.buckets)*2

        # Create new buckets list, recalculate load with new_length
        new_buckets = [DoublyLinkedList() for i in range(new_length)]
        self.load = self.entries / new_length

        # Iterate through current items and add to new buckets
        for item_key, item_value in self.__iter__():
            index = hash(item_key) % new_length
            new_buckets[index].append((item_key, item_value))

        self.buckets = new_buckets
        return

    def _resize_down(self):
        """Resize down! There are too many buckets and too little entries. Resize and Rehash!"""
        new_length = self.entries * 2

        # Create new buckets list, recalculate load with new_length
        new_buckets = [DoublyLinkedList() for i in range(new_length)]
        self.load = self.entries / new_length

        # Iterate through current items and add to new buckets
        for item_key, item_value in self.__iter__():
            index = hash(item_key) % new_length
            new_buckets[index].append((item_key, item_value))

        self.buckets = new_buckets
        return

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def _bucket(self, key):
        """Return the bucket where the given key would be stored"""
        index = self._bucket_index(key)
        return self.buckets[index]

    def length(self):
        """Return the length of this hash table"""
        return self.entries

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        bucket = self._bucket(key)

        for item_key, item_value in bucket:
            if key == item_key:
                return True

        return False

    def get(self, key):
        """Return the value associated with the given key, or return None"""
        bucket = self._bucket(key)

        for item_key, item_value in bucket:
            if key == item_key:
                return item_value

        return None

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
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
        """Return a list of all items (key, value) in this hash table"""
        items = []
        for item in self.__iter__():
            items.append(item)
        return items

    def shrink():
        """Let user shrink the hash table to fit"""
        self._resize_down()
        return

    def clear(self):
        for i, bucket in enumerate(self.buckets):
            if bucket:
                self.buckets[i] = DoublyLinkedList()


def test_hash_table():
    ht = HashTable()
    ht.set('1', 1)
    ht.set('2', 1)
    ht.set('3', 1)

    for i in ht.buckets:
        print(i)


if __name__ == '__main__':
    test_hash_table()

