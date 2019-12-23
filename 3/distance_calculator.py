from shared.parser import Parser


if __name__ == '__main__':
    for line in Parser.ReadLines('input.txt'):
        print(line)