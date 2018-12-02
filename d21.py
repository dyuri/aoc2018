doubles = 0
triples = 0


def check(line):
    chars = {}
    for c in line:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return 2 in chars.values(), 3 in chars.values()


with open("input_2.txt", "r") as f:
    for line in f.readlines():
        d, t = check(line)
        doubles += 1 if d else 0
        triples += 1 if t else 0

print(doubles * triples)
