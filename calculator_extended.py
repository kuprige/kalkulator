import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s: %(message)s")


def get_number(message):
    """Pobiera liczbę od użytkownika, dopóki nie poda poprawnej."""
    while True:
        value = input(message)
        try:
            return float(value)
        except ValueError:
            print("To nie jest liczba. Spróbuj ponownie.")


def get_many_numbers():
    """Pobiera wiele liczb oddzielonych spacją."""
    while True:
        values = input("Podaj liczby oddzielone spacją: ").split()
        try:
            return [float(v) for v in values]
        except ValueError:
            print("Wszystkie wartości muszą być liczbami. Spróbuj ponownie.")


def calculate(operation):
    """
    Wykonuje działanie matematyczne zgodnie z wyborem użytkownika.
    """
    if operation in (1, 3):  # dodawanie lub mnożenie
        numbers = get_many_numbers()
        logging.info(f"Argumenty: {numbers}")

        if operation == 1:
            logging.info("Wykonuję dodawanie")
            return sum(numbers)

        if operation == 3:
            logging.info("Wykonuję mnożenie")
            result = 1
            for n in numbers:
                result *= n
            return result

    else:
        a = get_number("Podaj składnik 1: ")
        b = get_number("Podaj składnik 2: ")

        if operation == 2:
            logging.info(f"Odejmuję {a} i {b}")
            return a - b

        if operation == 4:
            logging.info(f"Dzielę {a} przez {b}")
            return a / b

    raise ValueError("Niepoprawny numer działania.")