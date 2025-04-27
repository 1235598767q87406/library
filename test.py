# with open("yello.txt", "a") as file:
#     file.write("привет")
with open("yello.txt", "r") as file:
    for line in file:
        print(line)
