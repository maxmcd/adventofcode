

directions = {
    "E": (1, 0),
    "N": (0, 1),
    "W": (-1, 0),
    "S": (0, -1),
}


filled_squares = {(0,0): 1}


def squares_around(coorindate):
    x, y = coorindate
    return [
        (x+1, y),
        (x+1, y+1),
        (x, y+1),
        (x-1, y+1),
        (x-1, y),
        (x-1, y-1),
        (x, y-1),
        (x+1, y-1),
    ]


def apply_direction(last_coordinates, d_index):
    delta = directions[list(directions.keys())[d_index % 4]]
    dx, dy = delta
    x, y = last_coordinates
    coordinates = (x+dx, y+dy)
    value = sum([filled_squares.get(x, 0) for x in squares_around(coordinates)])
    return (value), coordinates


def get_coordinates(number):
    d_index = 0
    coordinates = (0, 0)
    distance = 1
    while True:
        for _ in range(2):
            for _ in range(distance):
                value, coordinates = apply_direction(coordinates, d_index)
                filled_squares[coordinates] = value
                if value > number:
                    return value
            d_index += 1
        distance += 1



get_coordinates(361527)
print(filled_squares)
