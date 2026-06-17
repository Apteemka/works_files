def stick_together(sort_list):
    temp_str = ''
    for word in sort_list:
        temp_str = temp_str + word + ' '
    return temp_str


with open("resources/words.txt", 'r') as file:
    text = file.read()
words = text.split('\n')
alp_sorted = sorted(words)
len_sorted = sorted(words, key=len)
alp_reverse = sorted(words, reverse = True)
with open("resources/sorted_alphabetically.txt", 'w') as file:
    file.write(stick_together(alp_sorted))
with open("resources/sorted_by_length.txt", 'w') as file:
    file.write(stick_together(len_sorted))
with open("resources/sorted_reverse.txt", 'w') as file:
    file.write(stick_together(alp_reverse))