with open("./in.txt") as f:
    content = [line.rstrip('\n') for line in f]

def main():
    grid = [[0 for x in range(1000)] for y in range(1000)] 
    for x in content:
        num, _, coords, size = x.split(" ")
        num = num[1:]
        coords = [int(f) for f in coords[:-1].split(',')]
        size = [int(f) for f in size.split('x')]
        x,y = coords
        for xo in range(size[0]):
            for yo in range(size[1]):
                if grid[x+xo][y+yo] != 0:
                    grid[x+xo][y+yo] = "x"
                else:
                    grid[x+xo][y+yo] = num

    for x in content:
        num, _, coords, size = x.split(" ")
        num = num[1:]
        coords = [int(f) for f in coords[:-1].split(',')]
        size = [int(f) for f in size.split('x')]
        x,y = coords
        expected = size[0] * size[1]
        count = 0
        for xo in range(size[0]):
            for yo in range(size[1]):
                if grid[x+xo][y+yo] == num:
                    count += 1
        if expected == count:
            print(num)
main()
