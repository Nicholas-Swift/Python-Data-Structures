# Python Modues

# Python modules are a common pattern in python that allow files to be run independently (as a script) and also imported by other files (as a module).

# The program below will return a random quote

# import random

# quotes = ("It's just a flesh wound.",
#           "He's not the Messiah. He's a very naughty boy!",
#           "THIS IS AN EX-PARROT!!")

# rand_index = random.randint(0, len(quotes) - 1)
# print quotes[rand_index]

# Importing the script above will always print out a quote. Instead, we can do what we do below and use quotes without it automatically printing.

import random

quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")


def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

if __name__ == '__main__':
    quote = random_python_quote()
    print quote