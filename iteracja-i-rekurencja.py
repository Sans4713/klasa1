# n = int(input("Podaj liczbe: "))
# silnia = 1
# for i in range(1, n + 1):
#     silnia=silnia * i
# print("Silnia wynosi:", silnia )


# for i in range (1,101):
#     if i%15==0:
#         print("FizzBuzz")
#     elif i%5==0:
#         print("Buzz")
#     elif i%3==0:
#         print("Fizz")
#     else:
#         print(i)


# lista = [50,13,2,5,46]
# najmniejsza = lista[0]
# for i in  lista:
#     if najmniejsza > i:
#         najmniejsza = i
# print(najmniejsza)

# slowo = ["o","w","c","a"]
# slowo.reverse()
# print(*slowo, sep="")

# owca = "owca"
# print(owca [::-1])

# wysokosc = int(input("podaj wysokosc: "))
# for i in range (wysokosc, 0, -1):
#     print("*" * i)

# def wypisz_rosnanco(n):
#     if n == 0:
#         return
#     wypisz_rosnanco(n-1)
#     print(n)
# wypisz_rosnanco(10)

# def silnia(n):
#     if n == 1 or n == 0:
#         return 1
#     else: 
#         return n * silnia(n-1)
# print (silnia(5))

# ile = int(input("ile wyrazow w ciagu"))
# a, b = 0, 1
# for i in range (ile):
#     print (a, end = " ")
#     a, b = b, a + b 

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(100))

    