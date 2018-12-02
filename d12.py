x = 0
freqz = {0}
reachedtwice = None

while reachedtwice is None:
    with open("input_1.txt", "r") as f:
        for line in f.readlines():
            x += int(line)
            if x not in freqz:
                freqz.add(x)
            else:
                print(f"Frist one that's repeated: {x}")
                reachedtwice = x
                break
