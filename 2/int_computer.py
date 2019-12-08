
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
    for noun in range(100):
        for verb in range(100):
            test_sequence = sequence.copy()
            test_sequence[1], test_sequence[2] = noun, verb
            transform(test_sequence)

            if test_sequence[0] == 19690720:
                print(100 * noun + verb)
                exit(0)
