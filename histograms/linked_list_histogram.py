# A histogram structured as a linked list of tuples

from linked_list import LinkedList

class LinkedListHistogram(LinkedList):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new LinkedList; update with given items"""
        super(LinkedListHistogram, self).__init__()

        self.types = 0
        self.tokens = 0

        if iterable:
            self.update(iterable)

    def __repr__(self):
        #tuple_list = self.as_list()
        items_str = " ".join(map(str, self.as_list()))
        return items_str

    def insert(self, item):
        """Insert a single item to this histogram"""
        old_item = self.find(lambda x: x[0] == item)
        if old_item is not None:
            new_item = (item, old_item[1] + 1)
            self.delete(old_item)
            self.append(new_item)
        else:
            new_item = (item, 1)
            self.append(new_item)
            self.types += 1
        self.tokens += 1

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            self.insert(item)

    def remove(self, item):
        """Delete the item from this histogram"""
        old_item = self.find(lambda x: x[0] == item)
        self.delete(old_item)

    def count(self, key):
        item = self.find(lambda x: x[0] == item)
        return item[1]


if __name__ == '__main__':

    # Create word string and list
    word_string = "one fish two fish red fish blue fish"
    word_list = word_string.split(' ')

    print("List to add...")
    print(word_string)

    print("\n")

    # Add to DictionaryHistogram
    hist = LinkedListHistogram(word_list)

    print("types...")
    print(hist.types)

    print("\n")

    print("tokens...")
    print(hist.tokens)

    print("\n")

    print("histogram...")
    print(hist)

