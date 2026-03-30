print("Wybierz wersję kalkulatora:")
print("1 – wersja podstawowa")
print("2 – wersja rozszerzona")

mode = input("Wybór: ")

if mode == "1":
    from calculator_basic import calculate
    a = float(input("Podaj składnik 1: "))
    b = float(input("Podaj składnik 2: "))

    print("1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie")
    operation = int(input("Wybór działania: "))

    result = calculate(operation, a, b)
    print(f"Wynik to {result:.2f}")

elif mode == "2":
    from calculator_extended import calculate

    print("1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie")
    operation = int(input("Wybór działania: "))

    result = calculate(operation)
    print(f"Wynik to {result:.2f}")

else:
    print("Niepoprawny wybór.")