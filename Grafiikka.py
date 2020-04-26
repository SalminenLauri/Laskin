from tkinter import *

from Laskija import calculate


class Painike:
    lauseke =""
    def __init__(self, kehys, nimi, column, row, naytto):
        self.naytto = naytto
        self.kehys = kehys
        self.nimi = nimi
        self.column = column
        self.row = row

        painike = Button(self.kehys, text=self.nimi, font="Arial", width=4, height=0, pady=2, command = lambda: naytto.lisaa(self.nimi))
        painike.grid(column=self.column, row=self.row)


class YhteensaPainike(Painike):
    lauseke = ""

    def __init__(self, kehys, nimi, column, row, naytto):
        self.naytto = naytto
        self.kehys = kehys
        self.nimi = nimi
        self.column = column
        self.row = row
        painike = Button(self.kehys, text=self.nimi, font="Arial", width=4, height=0, pady=2,
                         command=lambda: naytto.yhteensa())
        painike.grid(column=self.column, row=self.row)

class NegPosPainike(Painike):
    def __init__(self, kehys, nimi, column, row, naytto):
        self.naytto = naytto
        self.kehys = kehys
        self.nimi = nimi
        self.column = column
        self.row = row

        painike = Button(self.kehys, text=self.nimi, font="Arial", width=4, height=0, pady=2, command = lambda: naytto.negpos())
        painike.grid(column=self.column, row=self.row)


class PyyhintaPainike(Painike):
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

class Naytto:

    def __init__(self, ikkuna):
        self.lauseke = StringVar(ikkuna,"")
        self.ikkuna=ikkuna
        self.naytto = Entry(self.ikkuna,width=15, textvariable = self.lauseke, font="Helvetica", borderwidth=2)
        self.naytto.grid(row=0, column=0, sticky='w',columnspan=100,pady=10)

    def lisaa(self,nimi):
        yhdessa = self.lauseke.get()+nimi
        self.lauseke.set(yhdessa)

    def yhteensa(self):
        try:
            yhteensa = calculate(self.lauseke.get())
            self.lauseke.set(yhteensa)
        except:
            self.lauseke.set("ERROR")

    def pyyhi(self):
        self.lauseke.set("")

    def negpos(self):
        uusi = self.lauseke.get()
        if len(uusi)==0:
            return
        if uusi[0]=='-':
            uusi=uusi[1:len(uusi)]
        else:
            if(uusi[0].isdigit() and uusi[0]!='0'):
                uusi='-'+uusi
        self.lauseke.set(uusi)


