from os import path


def parse_sequence(string_sequence):
    return [int(s) for s in string_sequence.split(',')]


def transform(int_sequence):
    i, flag = 0, int_sequence[0]

    while flag != 99 and len(int_sequence) > i:
        left, right, res = int_sequence[i+1], int_sequence[i+2], int_sequence[i+3]
        if flag == 1:
            int_sequence[res] = int_sequence[left] + int_sequence[right]
        else:
            int_sequence[res] = int_sequence[left] * int_sequence[right]

        i += 4
        flag = int_sequence[i]

class IntComputer:
    def __init__(self, file_name):
        self.sequence = self._read_nums_from(file_name)

        print("Computer initiated.")

    def _read_nums_from(self, file_name):
        sequence = []
        if path.isfile(file_name):
            with open(file_name, 'r') as infile:
                for line in infile:
                    sequence.extend(self.parse_sequence(line))

        return sequence


if __name__ == "__main__":
    IntComputer('input.txt')
