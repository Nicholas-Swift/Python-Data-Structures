# A module to clean up and tokenize text

import re


SUBREDDIT_REGEX = "\/?r\/[\A-z0-9-]+" # Get /r/subreddit and r/subreddit
USERNAME_REGEX = "\/?u\/[\A-z0-9-]+" # Get /u/username and u/username
MULTIPLE_ENDS_REGEX = "[.!?;]{2,}" # Get ...., !!, ?????, etc.
MULTIPLE_SPACES_REGEX = '[\s]{2,}' # Get 2 or more spaces

SMILEYS = [':-)', ':-]', ':-3', ':->', '8-)', ':-}',
            ':)', ':]', ':3', ':>', '8)', ':}',
            ':-D', '8-D', 'xD', ':X']

" ".replace("Edit:", " ") # Remove edits
" ".replace("\n", " ") # Remove new lines
CHARS_TO_DELETE = [':)("#*&-><@^,~[]']

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

    # Turn links into "LINK"
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url)
    for url in urls:
        text = text.replace(url, "LINK_HERE")

    # Delete and replace
    #chars_to_delete = ',-"*@#%^()'

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

    