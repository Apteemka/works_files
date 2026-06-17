lines_count = 0

with open("resources/input.txt", "r") as file:
    for line in file:
        lines_count += 1
with open("resources/input.txt", "r") as file:
    text = file.read()
words = text.split()

with open("resources/statistics.txt", "a") as file:
    file.write(f"{str(lines_count)}\n{str(len(words))}\n")