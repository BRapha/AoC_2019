
class Parser:

    @staticmethod
    def ReadLines(filename):
        with open(filename, 'r') as infile:
            for line in infile:
                yield line
