def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
    counter = dict()
    for line in handle:
        line = line.rstrip()
        if not line.startswith('From '): continue
        words = line.split()
        days = words[1]
        if days not in counter:
            counter[days] = 1
        else:
            counter[days] += 1
    bigkey = max(counter, key=counter.get)
    valsort = list(counter.values())
    bigval = max(valsort)
    print(bigkey, bigval)

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
