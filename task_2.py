word_count = 0
line_number = 0
line_list = list()

word_inp = str(input("Enter a word: "))

with open("resources/text.txt", 'r') as file:
    text = file.read()
text.lower()
text.replace('.', '')
text.replace(',', '')
text.replace('!', '')
text.replace('?', '')
text.replace(';', '')
text.replace(':', '')
lines = text.split('\n')
words = text.split()

for line in lines:
    line_number += 1
    if line.find(word_inp) == -1:
        continue
    line_list.append(line_number)

for word in words:
    if word == word_inp:
        word_count += 1

if word_count > 0:
    Found = True
else:
    Found = False

with open("resources/search_results.txt", 'w') as file:
    if Found:
        file.write(f"Word found that many times {word_count}, in lines {line_list}")
    else:
        file.write("Word not found")