import time

# def pobierz_pierwszy(lista):
#     start = time.time()
#     element = lista[0]
#     end = time.time()
#     return element, end-start
# dane  = list(range(1000000))
# print (pobierz_pierwszy(dane))

def suma_elementow(lista):
    start = time.time
    suma = 0
    for x in lista:
        suma += x #suma + x 
        end = time.time
        return suma, end-start
    dane = list(range(1000))
    print (suma_elementow(dane))

n = int(input("podaj liczbe calkowita:"))    #zlozonosc kwadratowa
start =time.time()
for i in range(n):
    for j in range(n):
        print ("#")
    print()
    end= time.time()
print(end-start)

