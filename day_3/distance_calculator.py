from shared.parser import Parser


def YieldPoints(s):
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
    closest_dist = None
    for x, y in YieldPoints(s):
        if (x, y) in trail_map:
            distance = abs(x)+abs(y)
            if closest_dist is None or closest_dist > distance:
                closest_dist = distance

    return closest_dist


def GetClosestIntersection(s1, s2):
    trail = set(point for point in YieldPoints(s1))
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
