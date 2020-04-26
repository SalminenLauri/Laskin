from tkinter import *
from Grafiikka import *

ikkuna = Tk()



ikkuna.title("Laskin")


naytto = Naytto(ikkuna)

painikePyyhi = PyyhintaPainike(ikkuna,"C",2,6, naytto)

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
painikeSulkuAlku = Painike(ikkuna,'(',0,6, naytto)
painikeSulkuLoppu = Painike(ikkuna,')',1,6, naytto)
painikePiste = Painike (ikkuna, '.',2,5,naytto)
painikeAlkuunMiinus = NegPosPainike(ikkuna, '+/-',0,5,naytto)

painikePlus = Painike(ikkuna,'+',3,5, naytto)
painikeMiinus = Painike(ikkuna,'-',3,4, naytto)
PainikeKerto = Painike(ikkuna,'*',3,3, naytto)
PainikeJako = Painike(ikkuna,'/',3,2, naytto)
PainikeYhteensa = YhteensaPainike(ikkuna,'=',3,6, naytto)


ikkuna.mainloop()
