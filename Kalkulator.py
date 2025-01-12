def dodaj(x, y):
    return x + y

def odejmij(x, y):
    return x - y

def pomnoz(x, y):
    return x * y

def podziel(x, y):
    if y != 0:
        return x / y
    else:
        return "Nie można dzielić przez zero!"

print("Wybierz operację:")
print("1. Dodaj")
print("2. Odejmij")
print("3. Pomnóż")
print("4. Podziel")

wybor = input("Wpisz numer operacji (1/2/3/4): ")

num1 = float(input("Wpisz pierwszą liczbę: "))
num2 = float(input("Wpisz drugą liczbę: "))

if wybor == '1':
    print(f"{num1} + {num2} = {dodaj(num1, num2)}")
elif wybor == '2':
    print(f"{num1} - {num2} = {odejmij(num1, num2)}")
elif wybor == '3':
    print(f"{num1} * {num2} = {pomnoz(num1, num2)}")
elif wybor == '4':
    print(f"{num1} / {num2} = {podziel(num1, num2)}")
else:
    print("Nieprawidłowy wybór.")
