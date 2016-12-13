# A histogram structured as a list of tuples
import random

class DictionaryHistogram(dict):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new list; update with given items"""
        super(DictionaryHistogram, self).__init__()
        
        self.types = 0
        self.tokens = 0

        if iterable:
            self.update(iterable)

    def __repr__(self):
        items_string = " ".join(map(str, self.items()))
        return items_string

    def insert(self, item):
        """Insert a single item to this histogram"""
        if item in self.keys():
            self[item] += 1
        else:
            self[item] = 1
            self.types += 1
        self.tokens += 1

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            self.insert(item)

    def delete(self, item):
        """Delete the item from this histogram"""
        del self[item]

    def count(self, key):
        """Return the count of the word"""
        return self[key]

    def get_random_word(self):
        """Return a 'random' word weighted based on occurance"""
        temp_value = 0
        tuple_list = []
        for key, value in self.items():
            new_tuple = (key, temp_value, temp_value + value - 1)
            tuple_list.append(new_tuple)
            temp_value += value

        random_int = random.randint(0, self.tokens-1)
        for i in tuple_list:
            if random_int >= i[1] and random_int <= i[2]:
                return i[0]


if __name__ == '__main__':

    # Create word string and list
    word_string = "one fish two fish red fish blue fish"
    word_list = word_string.split(' ')

    print("List to add...")
    print(word_string)

    print("\n")

    # Add to DictionaryHistogram
    hist = DictionaryHistogram(word_list)

    print("types...")
    print(hist.types)

    print("\n")

    print("tokens...")
    print(hist.tokens)

    print("\n")

    print("histogram...")
    print(hist)






