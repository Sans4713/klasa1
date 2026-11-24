# try:
#     liczba = int(input("podaj liczbe:"))
#     wynik = 10/liczba
# except ValueError:
#     print ("to nie jest liczba")
# except ZeroDivisionError:
#     print("nie mazna dzielic sie przez 0")
# else:
#     print(wynik)

# try: 
#     plik = open("dane.txt")
# except FileNotFoundError:
#     print("brak pliku")
# else:
#     print("plik poprawnie wczytany")
#     plik.close

# def ustaw_wiek(wiek):
#     if wiek < 0 or wiek > 125:
#         raise ValueError (" niepoprawna wartosc wieku")
#     return wiek

#print(ustaw_wiek(-10))     

while True:
    try:
        liczba = int(input("podaj liczbe calkowita:"))
    except ValueError:
        print("to nie jest licba, sproboj ponownie")
    else:
        print(f"dodales: {liczba}")
        break 
