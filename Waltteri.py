import re


def do_basic_operations(string):
    operatorsfirst = ("*", "/")
    operatorslast = ("+", "-")

    string = re.split('(\W)', string)

    for i, char in enumerate(string):
        if char == ".":
            string[i - 1:i + 2] = ["".join(string[i - 1:i + 2])]

    def to_int(symbol):
        try:
            symbol = int(symbol)
        except ValueError:
            pass
        return symbol

    string = list(map(to_int, string))

    while True:
        for i, char in enumerate(string):
            if char in operatorsfirst:
                if char == "*":
                    string[i - 1:i + 2] = [string[i - 1] * string[i + 1]]
                else:
                    string[i - 1:i + 2] = [string[i - 1] / string[i + 1]]
                break
        else:
            break

    while True:
        for i, char in enumerate(string):
            if char in operatorslast:
                if char == "+":
                    string[i - 1:i + 2] = [string[i - 1] + string[i + 1]]
                else:
                    string[i - 1:i + 2] = [string[i - 1] - string[i + 1]]
                break
        else:
            break

    return str(string[0])


def calculate(string):
    while True:
        for i, char in enumerate(string):

            if char == "(":
                last_opening_bracket_index = i

            if char == ")":
                string = string.replace(string[last_opening_bracket_index: i + 1],
                                        do_basic_operations(string[last_opening_bracket_index + 1: i]))
                break
        else:
            string = do_basic_operations(string)
            break
        print(string)

    return string
