import clean_up_text
import tokenize_text
from dictionary_histogram import DictionaryHistogram

def create_model(iterable):

    model = {}
    model[(None, "*START*")] = DictionaryHistogram()

    for sentence in iterable:

        previousWord = None
        for index, word in enumerate(sentence):

            print(word)

            # Check if word is in model, if not, create new dictogram
            if word not in model:
                model[(previousWord, word)] = DictionaryHistogram()

            # Check if word is end or start
            if (index == len(sentence)-1):
                model[(previousWord, word)].insert("*STOP*")
                break
            elif(index == 0):
                model[(previousWord, "*START*")].insert(word)

            # Add the next thing to it!
            model[(previousWord, word)].insert(sentence[index + 1])
            previousWord = word

    return model

def walk_markov_chain(model):
    words = []

    for key, value in model.items():
        print("Key: ", key)
        print("Value: ", value)
        print("\n\n")

    previousWord = None
    word = (None, "*START*")
    while True:
        word = model[word].get_random_word()
        if word == "*STOP*":
            break
        words.append(word)
        word2 = (previousWord, word)
        previousWord = word
        word = word2

    return words


if __name__ == '__main__':
    sentences = clean_up_text.return_sentences()
    tokens = tokenize_text.tokenize(sentences)
    model = create_model(tokens)

    words = walk_markov_chain(model)
    print(' '.join(words))



