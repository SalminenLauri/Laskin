import re


def perusoperaatio(string): #Määrittelee operaatiot.
    operaattorieka = ("*", "/") #Ensimmäisessä järjestyksessä olevat operaatiot
    operaattoritoka = ("+", "-") #Toisena järjestyksessä olevat operaatiot

    string = re.split('(\W)', string)  # luvut ja operaattorit listaksi

    if string[0] == "":  # jos lauseke alkaa minuuksella re.split luo tyhjän elementin listan alkuun, poistetaan se
        del string[0]

    for i, char in enumerate(string):  # re.split hajoittaa desimaalit kahdeksi osaksi, joten yhdistetään ne takaisin
        if char == ".":
            string[i - 1:i + 2] = ["".join(string[i - 1:i + 2])]

    def to_int(symboli):
        try:
            symboli = int(symboli)
        except ValueError:
            pass
        return symboli

    string = list(map(to_int, string))  # muutetaan numerot tekstistä

    if type(string[0]) is not int:  # yhdistetään mahdollinen ensimmäistä lukua edeltävä miinus siihen
        if string[0] == "-":
            string[1] = - string[1]
        del string[0]

    while True:  # tehdään kerto ja jakolaskut
        for i, char in enumerate(string):
            if char in operaattorieka:
                if char == "*":
                    string[i - 1:i + 2] = [string[i - 1] * string[i + 1]]
                else:
                    string[i - 1:i + 2] = [string[i - 1] / string[i + 1]]
                break
        else:
            break

    while True:  # tehdään plus ja miinuslaskut
        for i, char in enumerate(string):
            if char in operaattoritoka:
                if char == "+":
                    string[i - 1:i + 2] = [string[i - 1] + string[i + 1]]
                else:
                    string[i - 1:i + 2] = [string[i - 1] - string[i + 1]]
                break
        else:
            break

    return str(string[0])



def laske(string): #Tämä funtkio laskee lausekkeen.
    operators = ("+", "-", "*", "/", "^")
    string = string.replace(" ", "")  # käyttäjä voi jättää halutessaan välejä lausekkeeseen

    for i in range(1, len(string)):  # mahdollistaa kertomerkin poisjätön sulkujen yhteydessä
        if string[i] == ")" and string[i + 1] not in operators and string[i + 1] != ")":
            string = string[:i + 1] + "*" + string[i + 1:]
        elif string[i] == "(" and string[i - 1] not in operators and string[i - 1] != "(":
            string = string[:i] + "*" + string[i:]
    print(string)

    def kasittele_negatiiviset(string):  # vyöryttää kerto tai jakolaskua seuraavan miinuksen laskun eteen
        while True:
            string = string.replace("*+", "*").replace("/+", "+")
            jii = max(string.find("*-"), string.find("/-"))
            if jii == -1:
                break

            edeltavaOperaattori = None
            for i, char in enumerate(string):
                if char in ("+", "-"):
                    edeltavaOperaattori = char
                    edeltavaOperaattori_index = i

                if i >= jii:
                    if edeltavaOperaattori is not None:
                        if edeltavaOperaattori == "+":
                            string = string[:edeltavaOperaattori_index] + "-" + string[edeltavaOperaattori_index + 1:]
                        else:
                            string = string[:edeltavaOperaattori_index] + "+" + string[edeltavaOperaattori_index + 1:]
                        string = string[:jii + 1] + string[jii + 2:]
                    else:
                        string = "-" + string
                        string = string[:jii + 2] + string[jii + 3:]

                    break
        return string

    #SULUT: Eivät toimi vielä kunnolla, joten eivät mukana lopullisessa laskimessa.

    while True:  # poistetaan sulut yksi kerrallaan laskemalla sulkujen sisältö
        string = kasittele_negatiiviset(string)

        for i, char in enumerate(string):

            if char == "(":
                viimeinenOperaatioIndeksi = i

            if char == ")":
                string = string.replace(string[viimeinenOperaatioIndeksi: i + 1],
                                       perusoperaatio(string[viimeinenOperaatioIndeksi + 1: i]))
                break
        else:
            string = perusoperaatio(string)
            break

    return string #Palauttaa Stringinä tuloksen
