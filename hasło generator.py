import random

print("--------------")

ilość = int(input("Podaj ilość haseł: min 1 maks 10: "))

print("--------------")

while ilość < 1 or ilość > 10:
    print("Możesz wybrać od 1 do 10 haseł.")
    ilość = int(input("Podaj ponownie ilość haseł: "))
    print("--------------")


długość = int(input("Podaj długość hasła: "))

print("--------------")

while długość < 4 or długość > 25:
    print("Hasło wychodzi poza granice (min 4, maks 25).")
    długość = int(input("Podaj ponownie długość hasła: "))
    print("--------------")


małe_litery = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

duże_litery = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

liczby = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

znaki_specjalne = [
    "!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "+", "="
]


# Wybór znaków

while True:

    dostępne_znaki = []
    wybrano = 0

    małe = input("Czy dodać małe litery? (t/n): ").lower()
    print("--------------")

    duże = input("Czy dodać duże litery? (t/n): ").lower()
    print("--------------")

    cyfry = input("Czy dodać liczby? (t/n): ").lower()
    print("--------------")

    specjalne = input("Czy dodać znaki specjalne? (t/n): ").lower()
    print("--------------")


    if małe == "t":
        dostępne_znaki += małe_litery
        wybrano += 1

    if duże == "t":
        dostępne_znaki += duże_litery
        wybrano += 1

    if cyfry == "t":
        dostępne_znaki += liczby
        wybrano += 1

    if specjalne == "t":
        dostępne_znaki += znaki_specjalne
        wybrano += 1


    if wybrano == 0:
        print("Musisz wybrać przynajmniej jedną kategorię.")
        print("--------------")
    else:
        break


# Generowanie haseł

def generuj_hasło():

    hasło = []

    if małe == "t":
        hasło.append(random.choice(małe_litery))

    if duże == "t":
        hasło.append(random.choice(duże_litery))

    if cyfry == "t":
        hasło.append(random.choice(liczby))

    if specjalne == "t":
        hasło.append(random.choice(znaki_specjalne))


    reszta = długość - len(hasło)

    for i in range(reszta):
        hasło.append(random.choice(dostępne_znaki))


    random.shuffle(hasło)

    hasło = "".join(hasło)

    return hasło


# Wyświetlanie haseł

for x in range(ilość):

    hasło = generuj_hasło()

    print(hasło)

    print("--------------")