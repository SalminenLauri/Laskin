from tkinter import *

from Laskija import *

#Tämä tiedosto sisältää laskimen graafiset oliot, joista painikkeet joko syöttävät näyttöön merkkejä tai kutsuvat näytön funktioita.

#Painikkeiden parametrit esiteltynä:
#Kehys: se kehys tai suoritus, jossa grafiikka pyörii.
#Nimi: Painikkeen nimi, joka näkyy myös graafisesti. Normaaleissa painikkeissa nimi on se mitä syötetään näyttöön. Muissa painikkeissa nimellä ei ole merkitystä funktioiden kannalta.
#Column ja Row: kolumni ja rivi, jossa oliot sijaitsevat gridissä.
#Naytto: Se näyttö, jonka kanssa painike on yhteydessä.

class Painike: #Normaali numeropainike, joka lisää näyttöön merkin.
    lauseke =""
    def __init__(self, kehys, nimi, column, row, naytto):
        self.naytto = naytto
        self.kehys = kehys
        self.nimi = nimi
        self.column = column
        self.row = row

        painike = Button(self.kehys, text=self.nimi, font="Arial", width=4, height=0, pady=2, command = lambda: naytto.lisaa(self.nimi))
        painike.grid(column=self.column, row=self.row)


class YhteensaPainike(Painike): #Painike, joka käynnistää näytöstä laske()-funktion, joka palauttaa tuloksen näyttöön.
    lauseke = ""

    def __init__(self, kehys, nimi, column, row, naytto):
        self.naytto = naytto
        self.kehys = kehys
        self.nimi = nimi
        self.column = column
        self.row = row
        painike = Button(self.kehys, text=self.nimi, font="Arial", width=9, height=3, pady=2,
                         command=lambda: naytto.yhteensa())
        painike.grid(column=self.column, row=self.row, columnspan=2,rowspan=2)

class NegPosPainike(Painike): #Lisaa näytön lausekkeen alkuun miinuksen, jos lause on positiivinen tai poistaa sen, jos sellainen jo on. Jos alussa on jokin muu merkki ei tee mitään.
    # Toimii kutsumalla näytön negpos() funktiota.
    def __init__(self, kehys, nimi, column, row, naytto):
        self.naytto = naytto
        self.kehys = kehys
        self.nimi = nimi
        self.column = column
        self.row = row

        painike = Button(self.kehys, text=self.nimi, font="Arial", width=4, height=0, pady=2, command = lambda: naytto.negpos())
        painike.grid(column=self.column, row=self.row)


class PyyhintaPainike(Painike): #Pyyhkii näytön kutsumalla näytön pyyhi()-funktiota.
    lauseke = ""

    def __init__(self, kehys, nimi, column, row, naytto):
        self.naytto = naytto
        self.kehys = kehys
        self.nimi = nimi
        self.column = column
        self.row = row
        painike = Button(self.kehys, text=self.nimi, font="Arial", width=4, height=0, pady=2,
                         command=lambda: naytto.pyyhi())
        painike.grid(column=self.column, row=self.row)

class PyyhiYksi(Painike): #Pyyhkii yhden merkin lopusta kutsumalla näytön pyyhiYksi()-funktiota.
    lauseke = ""

    def __init__(self, kehys, nimi, column, row, naytto):
        self.naytto = naytto
        self.kehys = kehys
        self.nimi = nimi
        self.column = column
        self.row = row
        painike = Button(self.kehys, text=self.nimi, font="Arial", width=4, height=0, pady=2,
                         command=lambda: naytto.pyyhiYksi())
        painike.grid(column=self.column, row=self.row)

class Naytto: #Näyttö näyttää tämänhetkisen lausekkeen ja olion hoitaa myös sen sisällä tapahtuvan laskemisen kutsumalla laske() funtkiota.

    def __init__(self, ikkuna): #Näyttö luodaan määrittämällä se ikkuna, kehys tai suorite, missä se pyörii.
        self.lauseke = StringVar(ikkuna,"") #Tämä muuttuja sisältää näytön lausekkeen.
        self.ikkuna=ikkuna
        self.naytto = Entry(self.ikkuna,width=15, textvariable = self.lauseke, font="Helvetica", borderwidth=2)
        self.naytto.grid(row=0, column=0, sticky='w',columnspan=100,pady=10)

    def lisaa(self,nimi): #Lisää merkin näyttöön.
        yhdessa = self.lauseke.get()+nimi
        self.lauseke.set(yhdessa)

    def yhteensa(self): #Laskee näytön lausekkeen kutsumalla laske()-funktiota. Palauttaa tekstin "ERROR", jos tässä tapahtuu virhe. Alunperin käytettiin Python eval() funtkiota, mutta
        #päätimme toteuttaa oman funtkion sekä harjoituksen vuoksi että koska eval() on turvallisuuden takia ongelmallinen.
        try:
            yhteensa = laske(self.lauseke.get())
            yhteensa = re.sub("\\.0$","", yhteensa) ##Poistaa lopusta ".0", koska se on turha tämä helpompaa kuin pelata tyyppimuunnosten kanssa."
            self.lauseke.set(yhteensa)
        except:
            testi=self.lauseke.get()
            if len(testi)!=0:
                self.lauseke.set("ERROR")
            else:
                self.lauseke.set("")


    def pyyhi(self): #Pyyhkii näytön.
        self.lauseke.set("")

    def pyyhiYksi(self): #Pyyhkii yhden merkin näytöstä.
        uusi=self.lauseke.get()
        uusi= uusi[0:len(uusi)-1]
        self.lauseke.set(uusi)

    def negpos(self): #Lisaa näytön lausekkeen alkuun miinuksen, jos lause on positiivinen tai poistaa sen, jos sellainen jo on. Jos alussa on jokin muu merkki ei tee mitään.
        uusi = self.lauseke.get()
        if len(uusi)==0:
            return
        if uusi[0]=='-':
            uusi=uusi[1:len(uusi)]
        else:
            if(uusi[0].isdigit() and uusi[0]!='0'):
                uusi='-'+uusi
        self.lauseke.set(uusi)


