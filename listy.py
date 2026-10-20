lista = [1,6,4,53,3,5,65,7,8,76,4,678,789]
print(type(lista))
print(lista)
print (lista[0])
print(*lista)
print (*lista, sep =",")

for i in (lista):
    print(i)

lista.sort()
print (lista)
lista.reverse()
print(lista)

print (lista.count(4))   #liczy ile jest 4 

lista.remove(3)    #usuwa 3 ale tylko jedna 
print (lista)

lista.append(3)   #dodaje 3
print(lista)

print (len(lista))  #liczy ile jest liczb
       

kontakty={           #slownik
    "ewa": 85364583,
    "leon": 2934274289,
    "edward":4987593456,
}

print (kontakty["ewa"])  #wypisze ten kontakt
kontakty ["iza"]= 123131321       #dodaje kontakt

for imie,numer in kontakty.items():
    print ("%s na numer telefonu %d" %(imie, numer))


kontakty.pop ("iza")    #usuwa ize 
print (kontakty.keys())    #wypisuje imiona
print(kontakty.values())   #wypisuje numery

zbior1 = {1,2,3}
zbior2 = {3,4,5,6}


suma_zbiorow = zbior1.union(zbior2)
print(suma_zbiorow)

roznica_zbiorow = zbior1.difference(zbior2)
print(roznica_zbiorow)


czesc_wspolna = zbior1.intersection(zbior2)
print(czesc_wspolna)

krotka=(1,2,3)  #nie zmienia sie
print(krotka)

krotka = 1,2,3
print(len(krotka))
print (krotka.count(1))

print (krotka[1])

a,b,c = krotka #pisze po kolei jak wpisalismy
print (a)

lista2 =[10,20,30,40,50,60]
print (lista2[1:4]) #od 1 do 4 
print (lista2 [:3]) #do 3
print (lista2 [3:]) # po 3
print (lista2 [::2]) #co drugie
print (lista2 [-1])  #od konca zaczynamy od 1 a nie od 0
print (lista2 [::-1]) # po kolei od konca 