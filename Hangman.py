import requests
import random
def get_woerter():
    url = "http://www.netzmafia.de/software/wordlists/deutsch.txt"
    textt = []
    r = requests.get(url)
    textt.append(r.text.replace("\n", ",").split(","))
    return textt


def strichmaennchen():
    leben = 10
    deutsche_woerter = get_woerter()
    list = deutsche_woerter[0]
    wort = random.choice(list).upper()
    geratene_buchstaben = set()
    alle_buchstaben = set(wort.upper())
    while len(alle_buchstaben) > 0 and leben > 0:
        print("Diese Buchstaben hast du schon benutzt: ", " ".join(geratene_buchstaben))
        print("Du hast noch: " + str(leben) + " Leben.")
        char_input = input("Rate einen Buchstaben: ").upper()
        if char_input in alle_buchstaben:
            alle_buchstaben.remove(char_input)
        elif char_input in geratene_buchstaben:
            print("Den Buchstaben hast du schon eingetippt.")
        elif char_input not in alle_buchstaben:
            print("Leider falsch.")
            leben -= 1
        else:
            print("Ungültiger Buchstabe. Bitte versuche erneut")
        geratene_buchstaben.add(char_input)
        woerterliste = [letter if letter in geratene_buchstaben else "-" for letter in wort]
        print("Das jetzige Wort lautet: ", " ".join(woerterliste))
    if leben == 0:
        print("Game over leider keine Leben mehr übrig. Das Wort lautete " + wort)
        return
    print("Du hast gewonnen")

strichmaennchen()