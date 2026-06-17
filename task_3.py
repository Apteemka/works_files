with open("resources/file1.txt", "r") as file:
    combine = f"=== Содержимое {file.name} ===\n" + file.read() + "\n\n"
with open("resources/file2.txt", "r") as file:
    combine = combine + f"=== Содержимое {file.name} ===\n" + file.read() + "\n\n"
with open("resources/file3.txt", "r") as file:
    combine = combine + f"=== Содержимое {file.name} ===\n" + file.read()
with open("resources/combined.txt", "w") as file:
    file.write(combine)