import random
print ("hello world") #komentarz
zmienna = 10 
print(type(zmienna))
rzeczywista = 10.5 
print(type(rzeczywista))
teks = "hello world" 
print(type(teks)) 
# suma = 1+2 
# roznica = 5-4 
# iloczyn = 3*2
# iloraz = 4/2 
# reszta = 5%2
# potega = 5**2
# dzielenie_calkowite = 5//2 
# print (suma,roznica,iloczyn,iloraz,reszta,potega,dzielenie_calkowite)
# print ("wartosc sumy to:", suma, "a wartosc roznicy to:", roznica)
# print (f"wartisc sumy to:{suma}, a wartosc roznicy to{roznica}")
# print ("wartosc sumy to %.10f" %suma)
# imie = input("jak masz na ime?")
# print = ("czesc",imie)
# wiek = int(input("ile masz lat"))
# print = (type(wiek)) 
# los = random.randint(1, 100)
# # print (los) 
# liczba = -5
# if liczba>0:
#     print ("liczba jest wieksz od 0")
# elif liczba == 0:
#     print("liczba jest rowna 0")
# else:
#     print("liczba jest mniejsza od 0")
#     if "tekst" in "bardzo prosty tekst":
#         print ("prawda")
#     else : 
#         print ("falsz")


#     for i in range (5):
#         print (i)

#     for i in range (1,100):
#         if i%2==0:
#             print (i)

#             for i in range (1,100, 2):
#                 print (i)

#                 for i in range (100,0, -1):
#                     print (i)

# for litera in "slowo":
#     if litera =="o":
#         break
#     print ("litera")


# for litera in "slowo":
#     if litera =="o":
#         continue
#     print ("litera")


#     liczba = int (input("podaj liczbe calkowita:"))
#     while liczba <=0:
#         liczba = int (input("podaj liczbe calkowita:"))
#         print ("podales liczbe dodatnia")


def powitanie():
            print ("czesc")

powitanie()

def powitanie_imienne(name):
     print ("czesc", name)
powitanie_imienne("Jacek")

def dzielenie (dzielna,dzielnik):
        if dzielnik==0: 
                return "nie mozna dzielic przez 0"
        else :
                return dzielna/dzielnik
print (dzielenie(10,2)) 
iloraz = dzielenie (15,3)
print (iloraz) 
        