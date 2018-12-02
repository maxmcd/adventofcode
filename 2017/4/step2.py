 
with open('input.txt') as f:
    lines = f.read().splitlines()
    split_lines = [line.split(' ') for line in lines]
    count = 0
    for sl in split_lines:
        sl = [''.join(sorted(w)) for w in sl]
        if len(sl) == len(list(set(sl))):
            count += 1
    print(count)