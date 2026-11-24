def dodawanie (a,b):
    return a+b
def odejmowanie (a,b):
    return a-b
def mnozenie (a,b):
    return a*b
def dzielenie (a,b):
    if b==0:
        raise ValueError("Nie mozna dzielic przez zero")
    else:
        return a/b
def potegowanie(a, b):
    if a == 0 and b < 0:
        raise ValueError("Zero nie moze miec ujemnej potegi.")
    if a < 0 and b == int(b):
        raise ValueError("Wynik nie jest liczba rzeczywistą.")
    return a ** b
 
def pierwiastkowanie(a):
    if a < 0:
        raise ValueError("Nie mozna obliczyc pierwiastka z liczby ujemnej.")
    return a**0.5
def dzielenie_modulo (a,b):
    if b == 0:
        raise ValueError("Nie można dzielić modulo przez zero.")
    return a % b
def dzielenie_calkowite (a,b):
      if b == 0:
        raise ValueError("Nie można dzielić przez zero.")
      return a // b
     
def wczytaj_liczbe(tekst):
    liczba = input(tekst)
    liczba = liczba.replace(",", ".")
    try:
        return float(liczba)
    except ValueError:
        raise ValueError("To nie jest liczba.")

     
def pokaz_wynik(wynik):
     if wynik == int(wynik):
      print("wynik to:", wynik)

while True:
     print("==========Kalkulator==========")
     print ("1. Dodawanie")
     print ("2. Odejmowanie")
     print ("3. Mnozenie")
     print ("4. Dzielenie")
     print ("5. Potegowanie")
     print ("6. Pierwistkoeanie")
     print ("7. Dzielenie Modulo")
     print ("8. Dzielenie Calkowite")
     print ("0. Wyjscie")
     wybor = input("Wybierz dzialanie: ")

     if wybor == "0":
        print("Do widzenia!")
        break

     try:
            if wybor == "6":
                a = wczytaj_liczbe("Podaj liczbę: ")
                pokaz_wynik(pierwiastkowanie(a))
            elif wybor in ["1", "2", "3", "4", "5", "7", "8"]:
                a = wczytaj_liczbe("Podaj pierwszą liczbę: ")
                b = wczytaj_liczbe("Podaj drugą liczbę: ")
            if wybor == "1":
                    pokaz_wynik(dodawanie(a, b))
            elif wybor == "2":
                    pokaz_wynik(odejmowanie(a, b))
            elif wybor == "3":
                    pokaz_wynik(mnozenie(a, b))
            elif wybor == "4":
                    pokaz_wynik(dzielenie(a, b))
            elif wybor == "5":
                    pokaz_wynik(potegowanie(a, b))
            elif wybor == "7":
                    pokaz_wynik(dzielenie_modulo(a, b))
            elif wybor == "8":
                    pokaz_wynik(dzielenie_calkowite(a, b))
            else:
                print("Blad: wybierz numer z menu (0-8).")
     except ValueError as blad:
            print("Blad:", blad)  