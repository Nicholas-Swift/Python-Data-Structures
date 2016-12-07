# A histogram structured as a list of tuples

class TupleHistogram(list):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new list; update with given items"""
        super(TupleHistogram, self).__init__()
        
        self.types = 0
        self.tokens = 0

        if iterable:
            self.update(iterable)

    def __repr__(self):
        items_string = " ".join(map(str, self))
        return items_string

    def insert(self, item):
        """Insert a single item to this histogram"""
        for i, old_item in enumerate(self):
            if item == old_item[0]:
                new_tuple = (item, old_item[1] + 1)
                self[i] = new_tuple
                self.tokens += 1
                return
        new_tuple = (item, 1)
        self.append(new_tuple)
        self.types += 1
        self.tokens += 1

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            self.insert(item)

    def delete(self, item):
        """Delete the item from this histogram"""
        for i in self:
            if item == i[0]:
                self.remove(i)
                return

    def count(self, key):
        """Return the count of the word"""
        for item in self:
            if key == item[0]:
                return item


if __name__ == '__main__':

    # Create word string and list
    word_string = "one fish two fish red fish blue fish"
    word_list = word_string.split(' ')

    print("List to add...")
    print(word_string)

    print("\n")

    # Add to DictionaryHistogram
    hist = TupleHistogram(word_list)

    print("types...")
    print(hist.types)

    print("\n")

    print("tokens...")
    print(hist.tokens)

    print("\n")

    print("histogram...")
    print(hist)

