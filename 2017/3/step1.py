

directions = {
    "E": (1, 0),
    "N": (0, 1),
    "W": (-1, 0),
    "S": (0, -1),
}


def apply_direction(number, last_coordinates, d_index):
    delta = directions[list(directions.keys())[d_index % 4]]
    dx, dy = delta
    x, y = last_coordinates
    return (number + 1), (x+dx, y+dy)


def get_coordinates(number):
    count = 1
    d_index = 0
    coorindates = (0, 0)
    distance = 1
    while True:
        for _ in range(2):
            for _ in range(distance):
                count, coorindates = apply_direction(
                    count, coorindates, d_index)
                if count == number:
                    return coorindates
            d_index += 1
        distance += 1


def distance(first, second):
    mx, my = first
    px, py = second
    return abs(px-mx) + abs(py-my)

assert distance((0, 0), (2, 1)) == 3


def get_distance_of_number(number):
    out = distance((0, 0), get_coordinates(number))
    print(number, out)
    return out

assert get_distance_of_number(12) == 3
assert get_distance_of_number(23) == 2
assert get_distance_of_number(1024) == 31


get_distance_of_number(361527)
