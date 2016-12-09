import re

myfile = open('catcher_in_the_rye.txt', 'r')
text = myfile.read()

text = text.replace(',', ' ').replace('-', ' ').replace('"', ' ').replace('*', ' ').replace('@', ' ').replace('#', ' ').replace('%', ' ').replace('^', ' ').replace('&', ' and ').replace('*', ' ').replace('(', ' ').replace(')', ' ')
text = text.replace('Mr.', 'Mr ').replace('Mrs.', 'Ms ').replace('Ms.', 'Ms ').replace('D.B.', 'DB ')
text = ' '.join(text.split())

print(text)

sentenceRegex = re.compile("[^.](.*?)[!.;]")
matches = sentenceRegex.findall(text)

new_text = []
for match in matches:
    new_text.append(match)

new_file = open('sanitzied_file.txt', 'w')
new_file.write('\n'.join(new_text))