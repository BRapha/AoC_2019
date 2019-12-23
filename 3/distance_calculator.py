from shared.parser import Parser

left_map = set()
closest_intersection = float('inf')


def GoRight(num_steps):
    pass


def GoLeft(num_steps):
    pass


def GoUp(num_steps):
    pass


def GoDown(num_steps):
    pass


def StepThroughPath(s):
    x, y = 0, 0
    for turn in s.split(','):
        direction, steps = turn[0], int(turn[1])
        if direction == 'R':
            for _ in range(steps):
                x += 1
                yield x, y
        elif direction == 'L':
            for _ in range(steps):
                x -= 1
                yield x, y
        elif direction == 'U':
            for _ in range(steps):
                y += 1
                yield x, y
        else:
            for _ in range(steps):
                y -= 1
                yield x, y



def FindClosestIntersection(s):
    global closest_intersection
    for x, y in StepThroughPath(s):
        if (x, y) in left_map:
            manhattan_distance = x+y
            closest_intersection = manhattan_distance if manhattan_distance < closest_intersection else closest_intersection

    return closest_intersection



def CreateMap(s):
    for x, y in StepThroughPath(s):
        left_map.add((x, y))


if __name__ == '__main__':
    for line in Parser.ReadLines('test.txt'):  #('input.txt'):
        if not left_map:
            CreateMap(line)
        else:
            print(FindClosestIntersection(line))
