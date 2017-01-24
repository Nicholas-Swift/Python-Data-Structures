# A Histogram structured as a Hash Table

import os
from flask import Flask, request
from markovmodel import MarkovModel
import cleanuptext

# Open file
file = open('text.txt')

# Create models
text = file.read()
tokens = cleanuptext.tokenizetext(text)
model = MarkovModel(tokens, 3)

app = Flask(__name__)

@app.route('/')
def main():
    words = model.walk()
    words_string = ' '.join(words)
    words_string = words_string[0].upper() + words_string[1:] + '.'
    return words_string

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
