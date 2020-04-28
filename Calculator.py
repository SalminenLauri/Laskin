import re


def do_basic_operations(string):
    operatorsfirst = ("*", "/")
    operatorslast = ("+", "-")

    string = re.split('(\W)', string)  # luvut ja operaattorit listaksi

    if string[0] == "":  # jos lauseke alkaa minuuksella re.split luo tyhjän elementin listan alkuun, poistetaan se
        del string[0]

    for i, char in enumerate(string):  # re.split hajoittaa desimaalit kahdeksi osaksi, joten yhdistetään ne takaisin
        if char == ".":
            string[i - 1:i + 2] = ["".join(string[i - 1:i + 2])]

    def to_int(symbol):
        try:
            symbol = float(symbol)
        except ValueError:
            pass
        return symbol

    string = list(map(to_int, string))  # muutetaan numerot tekstistä floateiksi

    if type(string[0]) is not float:  # yhdistetään mahdollinen ensimmäistä lukua edeltävä miinus siihen
        if string[0] == "-":
            string[1] = - string[1]
        del string[0]

    while True:  # tehdään kerto ja jakolaskut
        for i, char in enumerate(string):
            if char in operatorsfirst:
                if char == "*":
                    string[i - 1:i + 2] = [string[i - 1] * string[i + 1]]
                else:
                    string[i - 1:i + 2] = [string[i - 1] / string[i + 1]]
                break
        else:
            break

    while True:  # tehdään plus ja miinuslaskut
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
    operators = ("+", "-", "*", "/", "^")
    string = string.replace(" ", "")  # käyttäjä voi jättää halutessaan välejä lausekkeeseen

    for i in range(1, len(string)):  # mahdollistaa kertomerkin poisjätön sulkujen yhteydessä
        if string[i] == ")" and string[i + 1] not in operators and string[i + 1] != ")":
            string = string[:i + 1] + "*" + string[i + 1:]
        elif string[i] == "(" and string[i - 1] not in operators and string[i - 1] != "(":
            string = string[:i] + "*" + string[i:]

    def handle_negatives(string):  # vyöryttää kerto tai jakolaskua seuraavan miinuksen laskun eteen
        while True:
            string = string.replace("*+", "*").replace("/+", "+")
            string = string.replace("+-", "-").replace("-+", "-").replace("--", "+").replace("++", "+")
            jii = max(string.find("*-"), string.find("/-"))
            if jii == -1:
                break

            previous_operator = None
            for i, char in enumerate(string):
                if char in ("+", "-"):
                    previous_operator = char
                    previous_operator_index = i

                if i >= jii:
                    if previous_operator is not None:
                        if previous_operator == "+":
                            string = string[:previous_operator_index] + "-" + string[previous_operator_index + 1:]
                        else:
                            string = string[:previous_operator_index] + "+" + string[previous_operator_index + 1:]
                        string = string[:jii + 1] + string[jii + 2:]
                    else:
                        string = "-" + string
                        string = string[:jii + 2] + string[jii + 3:]

                    break
        return string

    while True:  # poistetaan sulut yksi kerrallaan laskemalla sulkujen sisältö
        string = handle_negatives(string)
        print(string)

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

    return string
