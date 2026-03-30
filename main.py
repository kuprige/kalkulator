from calculator import calculate

print("Podaj działanie, posługując się odpowiednią liczbą:")
print("1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie")

operation = int(input("Wybór: "))
a = float(input("Podaj składnik 1: "))
b = float(input("Podaj składnik 2: "))

result = calculate(operation, a, b)

print(f"Wynik to {result:.2f}")