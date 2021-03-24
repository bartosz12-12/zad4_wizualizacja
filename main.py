
# Zad1

# list = [x for x in range(31)]
# print(list)
# listx2 = [str(x*2) for x in list]
# plik = open("liczbyx2.txt", "w")
# plik.writelines(listx2)
#
#
#
# #zadanie2
# plik = open('liczbyx2.txt', 'r')
# odzczyt = plik.readlines()
# print(odzczyt)


#zadanie3
# with open('tekst.txt', 'w') as plik4:
#     for newLine in range(10):
#         plik4.write('abcde\n')
# with open('tekst.txt', 'r') as plik4:
#     for line in plik4:
#         print(line, end='')



##Zadanie4

# class NaZakupy:
#     nazwa_produktu = ""
#     ilosc = 0
#     jednostka_miary = ""
#     cena_jed = 0
#
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc=ilosc
#         self.jednostka_miary=jednostka_miary
#         self.cena_jed=cena_jed
#     def wyswietl_Produkt(self):
#         print(self.ilosc, self.nazwa_produktu, self.jednostka_miary, self.cena_jed)
#     def ile_produktu(self):
#         print(str(self.ilosc) +""+self.jednostka_miary)
#     def ile_kosztuje(self):
#         kwota = self.cena_jed*self.ilosc
#         return kwota



#Zadanie5
# class CiagiArytm:
#     a1 = 0
#     rozn = 0
#     ile = 0
#     wyrazyCiagu = [a1]
#
#     def wyswietlElementy(self):
#         print(self.wyrazyCiagu)
#     def pobierzElem(self, *n):
#         pobraneElementy = []
#         for x in n:
#             pobraneElementy.append(self.wyrazyCiagu[x-1])
#         print(pobraneElementy)
#     def pobierzParametry(self, a1, rozn, ile):
#         self.a1 = a1
#         self.rozn=rozn
#         self.ile = ile
#     def sumaEl(self):
#
#         suma=0
#         for x in self.wyrazyCiagu:
#             suma +=x
#         print(suma)
#     def policzEl(self):
#         if self.rozn != 0:
#             a1 = self.a1
#             for x in range(self.ile):
#                 an = a1 + self.rozn
#                 self.wyrazyCiagu.append(an)
#                 a1 = an

##zadanie6
# class Robaczek:
#     xaxis = 0
#     yaxis = 0
#     krok = 0
#
#     def __init__(self, x=0, y=0, step=1):
#         self.xaxis=x
#         self.yaxis=y
#         self.krok=step
#
#     def goUp(self, ile):
#         self.yaxis+=(ile*self.krok)
#     def goDown(self, ile):
#         self.yaxis-=(ile*self.krok)
#     def goRight(self, ile):
#         self.xaxis +=(ile*self.krok)
#     def goLeft(self, ile):
#         self.xaxis -=(ile*self.krok)
#     def whereAmI(self):
#         print("Wspolrzedna x: " + str(self.xaxis) + " Wspolrzedna y: " + str(self.yaxis))