# A module to clean up and tokenize text

import re


def _read_file(filename):
    """Return the text from a given file"""
    text_file = open(filename, 'r')
    text = text_file.read()
    return text

def _get_sentences(text):
    """Returns a list of sentences from the given text"""
    sentenceRegex = re.compile("[^.](.*?)[!.;?]")
    matches = sentenceRegex.findall(text)

    sentences = []
    for match in matches:
        sentences.append(match)

    return sentences

def _sanitize_text(text):
    """Return a sanitized version of the given text"""
    chars_to_delete = ',-"*@#%^()'

    new_text = text
    for char in chars_to_delete:
        new_text = new_text.replace(char, ' ')

    new_text = new_text.replace('Mr.', 'Mr ').replace('Mrs.', 'Ms ').replace('Ms.', 'Ms ').replace('D.B.', 'DB ').replace('Dr.', 'Dr ')

    new_text = ' '.join(new_text.split())

    return new_text

def cleanuptext(text):
    """Returns a sanitized version of the given text"""
    sanitized_text = _sanitize_text(text)
    return sanitized_text

def cleanupfile(filename):
    """Returns a sanitized string version of the given file"""
    text = _read_file(filename)
    return cleanuptext(text)

def tokenizetext(text):
    """Returns a tokenized version of the given text"""
    sentences = _get_sentences(text)
    tokenized_sentences = []

    for sentence in sentences:
        words = []
        for word in sentence.split(' '):
            words.append(word)
        tokenized_sentences.append(words)

    return tokenized_sentences

def tokenizefile(filename):
    """Returns a tokenized string version of the given file"""
    text = cleanupfile(filename)
    return tokenizetext(text)


if __name__ == '__main__':
    print("WOW")

    