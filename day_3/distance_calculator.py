from shared.parser import Parser


def YieldSteps(s):
    x = y = 0
    for segment in s.split(','):
        direction, steps = segment[0], int(segment[1:])
        for _ in range(steps):
            if direction == 'L':
                x -= 1
            elif direction == 'R':
                x += 1
            elif direction == 'U':
                y += 1
            else:
                y -= 1

            yield (x, y)


def FindClosestIntersection(trail_map, s):
    path_length = 0
    closest_dist = None
    for x, y in YieldSteps(s):
        path_length += 1
        if (x, y) in trail_map:
            total_dist = path_length + trail_map[(x, y)]
            if closest_dist is None or closest_dist > total_dist:
                closest_dist = total_dist

    return closest_dist


def GetClosestIntersection(s1, s2):
    path_length = 0
    trail = dict()
    for point in YieldSteps(s1):
        path_length += 1
        trail.setdefault(point, path_length)

    return FindClosestIntersection(trail, s2)


if __name__ == '__main__':
    first = None
    second = None
    for line in Parser.ReadLines('input.txt'):
        if first is None:
            first = line
        else:
            second = line

    print(GetClosestIntersection(first, second))
