import clean_up_text
import tokenize_text
from dictionary_histogram import DictionaryHistogram

def create_model(iterable, num):

    # Create empty model
    model = {}

    # Create first key -> start # WORKING
    first_key = []
    for i in range(0, num - 1):
        first_key.append(None)
    first_key.append("*START*")
    first_key = tuple(first_key)

    # Append first key
    model[first_key] = DictionaryHistogram()

    for sentence in iterable:

        previous_words = []
        for i in range(0, num - 1):
            previous_words.append(None)
        previous_words.append("*START*")

        for index, word in enumerate(sentence):

            current_key = tuple(previous_words)

            if model.get(current_key) is not None:
                model[current_key].insert(word)
            else:
                model[current_key] = DictionaryHistogram()
                model[current_key].insert(word)

            previous_words.pop(0)
            previous_words.append(word)

        current_key = tuple(previous_words)
        if model.get(current_key) is None:
            model[current_key] = DictionaryHistogram()
        model[current_key].insert("*STOP*")

    return model

def walk_markov_chain(model, num):

    words = []

    # Create first key -> start # WORKING
    previous_words = []
    for i in range(0, num - 1):
        previous_words.append(None)
    previous_words.append("*START*")

    current_key = tuple(previous_words)

    while True:
        word = model[current_key].get_random_word()
        if word == "*STOP*":
            break
        words.append(word)

        previous_words.pop(0)
        previous_words.append(word)
        current_key = tuple(previous_words)

    return words


if __name__ == '__main__':
    sentences = clean_up_text.return_sentences()
    tokens = tokenize_text.tokenize(sentences)
    model = create_model(tokens, 3)
    words = walk_markov_chain(model, 3)
    print(' '.join(words))



