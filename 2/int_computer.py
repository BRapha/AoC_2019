
def parse_sequence(line):
    return [int(s) for s in line.split(',')]


def transform(sequence):
    i, flag = 0, sequence[0]

    while flag != 99 and len(sequence) > i:
        left, right, res = sequence[i+1], sequence[i+2], sequence[i+3]
        if flag == 1:
            sequence[res] = sequence[left] + sequence[right]
        else:
            sequence[res] = sequence[left] * sequence[right]

        i += 4
        flag = sequence[i]


if __name__ == "__main__":
    sequence = []
    with open('input.txt', 'r') as infile:
        for line in infile:
            sequence.extend(parse_sequence(line))

    # apply task magic
    sequence[1], sequence[2] = 12, 2

    transform(sequence)
    print(sequence[0])