x = 0

with open("input_1.txt", "r") as f:
    for line in f.readlines():
        x += int(line)

print(x)
