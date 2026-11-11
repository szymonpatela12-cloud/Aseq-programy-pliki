import random

# Słowa i losowanie
słowa = [
    "banan", "cytryna", "drzewo", "fotel",
    "kanapa", "klocki", "lampka", "motyl"
]
słowo = random.choice(słowa)

# Tworzenie pustych list
odgadniete = []
użyte_litery = []

# Tworzenie podkreślników
for litera in słowo:
    odgadniete.append("_")

# Główna pętla gry
while "_" in odgadniete:

    print(" ".join(odgadniete))
    print("Użyte litery:", użyte_litery)

    zgadywana = input("Podaj literę: ").lower()

    # Sprawdzanie pustego wpisu
    if zgadywana == "":
        print("Błąd, podaj literę ponownie")
        continue

    # Sprawdzanie długości wpisu
    if len(zgadywana) > 1:
        print("Podaj tylko jedną literę")
        continue

    # Sprawdzanie użytych liter
    if zgadywana in użyte_litery:
        print("Ta litera była już użyta!")
        continue

    # Dodawanie litery do listy użytych
    użyte_litery.append(zgadywana)

    # Sprawdzanie, czy litera znajduje się w słowie
    if zgadywana in słowo:
        print("Dobra litera!")

        for numer, litera in enumerate(słowo):
            if litera == zgadywana:
                odgadniete[numer] = litera

    else:
        print("Nie ma takiej litery!")

# Zakończenie gry
print(" ".join(odgadniete))
print("Gratulacje! Odgadłeś słowo:", słowo)