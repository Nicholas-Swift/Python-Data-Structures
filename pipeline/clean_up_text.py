import re

def read_file():
    old_file = open('text.txt', 'r')
    text = old_file.read()

    return text

def sanitize_text(text):
    chars_to_delete = ',-"*@#%^()'

    new_text = text
    for char in chars_to_delete:
        new_text = new_text.replace(char, ' ')

    new_text = new_text.replace('Mr.', 'Mr ').replace('Mrs.', 'Ms ').replace('Ms.', 'Ms ').replace('D.B.', 'DB ').replace('Dr.', 'Dr ')

    new_text = ' '.join(new_text.split())

    return new_text

def get_sentences(text):
    sentenceRegex = re.compile("[^.](.*?)[!.;?]")
    matches = sentenceRegex.findall(text)

    sentences = []
    for match in matches:
        sentences.append(match)

    return sentences

def write_file(sentences):
    new_file = open('sanitized_text.txt', 'w')
    new_file.write('\n'.join(new_text))

def return_sentences():
    old_text = read_file()
    sanitized_text = sanitize_text(old_text)
    sentences = get_sentences(sanitized_text)
    return sentences

if __name__ == '__main__':
    sentences = return_sentences()
    write_file(sentences)

    