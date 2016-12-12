import re
import clean_up_text

def tokenize(iterable):
    tokens = []

    for sentence in iterable:
        words = []
        for word in sentence.split():
            words.append(word)
        tokens.append(words)

    return tokens

if __name__ == '__main__':
    sentences = clean_up_text.return_sentences()
    tokens = tokenize(sentences)
    print(tokens)
