from Grafiikka import *


#Luodaan ikkuna, jossa ohjelma pyörii.
ikkuna = Tk()

#Ohjelman otsikko.
ikkuna.title("Laskin")

#Luodaan näyttö naytto-oliona.
naytto = Naytto(ikkuna)

#Luodaan pyyhkimispainike.
painikePyyhi = PyyhintaPainike(ikkuna,"C",1,6, naytto)

#Luodaan yhden merkin kerrallaan pyyhkivä painike.
pyyhiYksi = PyyhiYksi(ikkuna,"CE", 0,6,naytto)

#Luodaan normaalit painikkeet.
painike7 = Painike(ikkuna,'7',0,2, naytto)
painike8 = Painike(ikkuna,'8',1,2, naytto)
painike9 = Painike(ikkuna,'9',2,2, naytto)
painike4 = Painike(ikkuna,'4',0,3, naytto)
painike5 = Painike(ikkuna,'5',1,3, naytto)
painike6 = Painike(ikkuna,'6',2,3, naytto)
painike1 = Painike(ikkuna,'1',0,4, naytto)
painike2 = Painike(ikkuna,'2',1,4, naytto)
painike3 = Painike(ikkuna,'3',2,4, naytto)
painike0 = Painike(ikkuna,'0',1,5, naytto)
painikePiste = Painike (ikkuna, '.',2,5,naytto)
painikePlus = Painike(ikkuna,'+',3,5, naytto)
painikeMiinus = Painike(ikkuna,'-',3,4, naytto)
PainikeKerto = Painike(ikkuna,'*',3,3, naytto)
PainikeJako = Painike(ikkuna,'/',3,2, naytto)
PainikeAlkuSulku = Painike(ikkuna, '(',0,7,naytto)
painikeLoppuSulku = Painike(ikkuna,')',1,7, naytto)

#Luodaan painike, joka muuttaa lausekkeen negatiivisesta positiiviseksi ja toisin päin.
painikeAlkuunMiinus = NegPosPainike(ikkuna, '+/-',0,5,naytto)

#Luodaan lausekkeen laskeva painike.
PainikeYhteensa = YhteensaPainike(ikkuna,'=',2,6, naytto)

#Pidetään ikkuna päällä
ikkuna.mainloop()
