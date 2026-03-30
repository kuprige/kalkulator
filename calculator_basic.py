import logging

# konfiguracja logowania
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s: %(message)s")

def calculate(operation, a, b):
    """
    Wykonuje działanie matematyczne na dwóch liczbach.

    Argumenty:
        operation (int): numer działania (1 dodawanie, 2 odejmowanie, 3 mnożenie, 4 dzielenie)
        a (float): pierwsza liczba
        b (float): druga liczba

    Zwraca:
        float: wynik działania
    """
    if operation == 1:
        logging.info(f"Dodaję {a:.2f} i {b:.2f}")
        return a + b
    elif operation == 2:
        logging.info(f"Odejmuję {a:.2f} i {b:.2f}")
        return a - b
    elif operation == 3:
        logging.info(f"Mnożę {a:.2f} i {b:.2f}")
        return a * b
    elif operation == 4:
        logging.info(f"Dzielę {a:.2f} przez {b:.2f}")
        return a / b
    else:
        logging.error("Nieznane działanie!")
        raise ValueError("Niepoprawny numer działania.")