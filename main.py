

class Pracownicy:

    def __init__(self, imie, wynagrodzenie):
        self._imie = imie
        self._wynagrodzenie = wynagrodzenie
        self._wynNetto = self.oblicz(wynagrodzenie)

    def oblicz(self, wynagr):
        skladki = round((round(wynagr * 0.0976,2)) + (round(wynagr * 0.015,2) )+( round(wynagr * 0.0245,2)),2)
        podstawaNaskladki_na_ubezpieczenieZdrow = wynagr - skladki
        skladka_ubezZdrow = round(podstawaNaskladki_na_ubezpieczenieZdrow * 0.09,2)
        podstawa_przychod = podstawaNaskladki_na_ubezpieczenieZdrow - 111.25
        podatek18 = round(podstawa_przychod * 0.18,2)
        zaliczkaPodatek = podatek18 - 46.33
        ubezZdrowNowe = round(podstawaNaskladki_na_ubezpieczenieZdrow * 0.0775,2)
        podatekNowa = round((zaliczkaPodatek - ubezZdrowNowe),0)

        netto = round((wynagr - skladki - skladka_ubezZdrow - podatekNowa),2)
        return netto
    def getNetto(self):
        return self._wynNetto
    def skladkiPracodawcy(self):
        return round((self._wynagrodzenie * 0.0976 + self._wynagrodzenie*0.065 + self._wynagrodzenie*0.0193 + self._wynagrodzenie*0.0245 + self._wynagrodzenie*0.001),2)

    def lacznyKoszt(self):
        return round((self._wynagrodzenie + (self._wynagrodzenie* 0.0976 + self._wynagrodzenie*0.065 + self._wynagrodzenie*0.0193 + self._wynagrodzenie*0.0245 + self._wynagrodzenie*0.001)),2)
    def getName(self):
        return  self._imie
liczbaPrac = int(input())

listaPrac = list()
for i in range(liczbaPrac):
    linia = input().split()
    pracownik = Pracownicy(linia[0], int(linia[1]))
    listaPrac.append(pracownik)
listakoszt = list()
for i in listaPrac:
    print( '{}'.format(i.getName() ), "%.2f"%float(round(i.getNetto() ,2)), "%.2f"%round(float(i.skladkiPracodawcy()), 2),"%.2f"%round(float(i.lacznyKoszt()), 2))
    listakoszt.append(i.lacznyKoszt())
print (sum(listakoszt))









