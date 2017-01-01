# A Histogram structured as a Hash Table

from histogram import Histogram


class MarkovModel(dict):

    def __init__(self, iterable=None, order=2):
        """Initialize this histogram as a new list; update with given items"""
        super(MarkovModel, self).__init__()

        self.order = order

        if iterable:
            self.update(iterable)

    def __repr__(self):
        """Return a string representation of this histogram"""
        items = []
        for item in self.items():
            items.append(item)
        items_str = " ".join(map(str, items))
        return items_str

    def _generate_empty_previous_words(self):
        """Generate a start key based on the markov model's order"""
        previous_words = []
        for i in range(0, self.order - 1):
            previous_words.append(None)
        previous_words.append("*START*")
        return previous_words

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
        for sentence in iterable:

            # First word in sentence (start)
            previous_words = self._generate_empty_previous_words()

            # Run through the sentence
            for index, word in enumerate(sentence):

                current_key = tuple(previous_words)

                if self.get(current_key) is not None:
                    self[current_key].insert(word)
                else:
                    self[current_key] = Histogram()
                    self[current_key].insert(word)

                previous_words.pop(0)
                previous_words.append(word)

            # End of sentence
            current_key = tuple(previous_words)
            if self.get(current_key) is None:
                self[current_key] = Histogram()
            self[current_key].insert("*STOP*")

    def walk(self):
        """Walk through the markov model"""
        words = []

        # Create first key
        previous_words = self._generate_empty_previous_words()
        current_key = tuple(previous_words)

        while True:
            word = self[current_key].get_random()
            if word == "*STOP*":
                break
            words.append(word)

            previous_words.pop(0)
            previous_words.append(word)
            current_key = tuple(previous_words)

        return words


def test_markov_model():
    sentence1 = "one fish two fish red fish blue fish".split(' ')
    sentence2 = "once upon a time there was a man named John".split(' ')
    sentence3 = "one in every two people is named Bill".split(' ')
    sentences = [sentence1, sentence2, sentence3]

    mm = MarkovModel(sentences, 1)
    words = mm.walk()
    print ' '.join(words)


if __name__ == '__main__':
    test_markov_model()

    