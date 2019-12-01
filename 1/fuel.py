def get_int_value_from_line(line):
    try:
        return int(line)
    except ValueError:
        return 0


def get_module_weights_from_file(filename):
    with open(filename, 'r') as infile:
        for line in infile:
            yield get_int_value_from_line(line)


def calculate_fuel_for_weight(weight):
    fuel = weight // 3 - 2
    if fuel <= 0:
        return 0

    return fuel + calculate_fuel_for_weight(fuel)


if __name__ == '__main__':
    total_fuel = 0
    for module_weight in get_module_weights_from_file('input.txt'):
        total_fuel += calculate_fuel_for_weight(module_weight)

    print(total_fuel)
