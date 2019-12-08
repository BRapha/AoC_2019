from os import path


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

    def parse_sequence(self, sequence):
        return [int(s) for s in sequence.split(',')]

    def evaluate(self, sequence):
        pass


if __name__ == "__main__":
    IntComputer('input.txt')
