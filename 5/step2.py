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
        if value >= 3:
            lines[index] = value - 1
        else:
            lines[index] = value + 1
        index += value
        count += 1
