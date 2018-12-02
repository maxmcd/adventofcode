with open('input.txt') as f:
    lines = f.read().splitlines()
    lines = [int(line) for line in lines]
    count = 0
    index = 0
    while True:
        try:
            value = lines[index]
        except IndexError:
            print(count)
            break
        lines[index] = value + 1
        index += value
        count += 1
