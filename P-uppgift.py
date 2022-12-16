"""Här importeras kod som gör att elemnet godtyckligt kan skrivas ut ur en lista."""
import random

"""Till en början skapas en klass med atomen som objekt. Objektet har tre attribut."""
"""Atombeteckning, atommassa och atomnummer."""
class Atom:
    def __init__(self, atombeteckning, atommassa):
        self.atombeteckning = atombeteckning
        self.atommassa = atommassa
        self.atomnummer = None

"""En litsa skapas."""
class Grundämnen(object):
    def __init__(self):
        self.lista = []

"""klass-objekten (tillhörande klassen Atomen) adderas i listan som i ovanstående funktion skapats."""
"""Detta görs genom att data läses in från den angivna textfilen i uppgiften."""
def skapa_lista():
    alla_grundämnen = Grundämnen()
    with open("atomer") as fil:
        for rad in fil:
            args = rad.strip().split()
            alla_grundämnen.lista.append(Atom(*args))
    sorterad_lista(alla_grundämnen)

"""Listan med klass-objekten som element sorteras därefter efter atommassans numeriska värde."""
"""Därefter görs finjusteringar för att uppfylla kraven i uppgiften."""
"""Finjusteringarna görs genom operationer som leder till radbyten för elementen i listan."""
def sorterad_lista(alla_grundämnen):
    sorterad_lista = sorted(alla_grundämnen.lista, key=lambda sortera: float(sortera.atommassa), reverse=False)
    förändra_rader = [17, 26, 51, 89, 91]
    for rad in förändra_rader:
        föränding = sorterad_lista[rad]
        sorterad_lista[rad] = sorterad_lista[rad + 1]
        sorterad_lista[rad + 1] = föränding
    meny(sorterad_lista)
    alla_grundämnen.lista = sorterad_lista

"""I ovanstående fall har har listans element (klass-objekten) enbart bestått av attributen atommassa och atombeteckning."""
"""Atomnummer läggs här till som attribut till varje element i listan."""
"""Anledningen till att atomnummer har lagts till senare är eftersom att atomnumrena är en funktion av listans ordning."""
def antal_atomnummer(sorterad_lista):
    addera_atomnummer = 1
    for grundämne in sorterad_lista:
        grundämne.atomnummer = addera_atomnummer
        addera_atomnummer += 1

"""Denna funktion gör att väljaren kan välja mellan olika alternativ som visas upp på menyn."""
def meny(sorterad_lista):
    försök = 0
    while försök < 3:
        print("-------------MENY-------------\n1. Visa alla atomer\n2. Träna på atomnummer\n3. Träna på atombeteckningar\n4. Träna på atommassor \n5. Avsluta programmet\n------------------------------ ")
        menyval = (input("Skriv in siffran som motsvarar det som du vill göra här: "))
        antal_atomnummer(sorterad_lista)
        if menyval == str(1):
            alternativ_1(sorterad_lista)
            break
        elif menyval == str(2):
            alternativ_2(sorterad_lista)
            break
        elif menyval == str(3):
            alternativ_3(sorterad_lista)
            break
        elif menyval == str(4):
            alternativ_4(sorterad_lista)
            break
        elif menyval == str(5):
            alternativ_5()
        else:
            print("\nDet du skrev in var inte en siffra som motsvarar något av valen i menyn, var vänlig och prova igen.\n")
            försök += 1
            continue

"""Denna funktion körs om väljaren väljer alternativ 1 i meny-funktionen."""
"""Det gör att alla grundämnen samt deras egenskaper skrivs ut, numrerade efter atomnummer."""
def alternativ_1(sorterad_lista):
    print("\nDetta är alla grundämnen:\n")
    for grundämne in sorterad_lista:
        print(f"Atomnummer: {grundämne.atomnummer} Atombeteckning: {grundämne.atombeteckning} Atommassa: {grundämne.atommassa} ")

"""Denna funktion körs om väljaren väljer alternativ 2 i meny-funktionen."""
"""Detta gör att en godtycklig atombeteckning visas för personen som kör programmet."""
"""Personen har därefter 3 försök på sig att skriva in rätt atomnummer till den godtyckliga atombeteckningen."""
def alternativ_2(sorterad_lista):
    utskriven_atom = random.choice(sorterad_lista)
    försök = 0
    while försök < 3:
        gissning = (input(f"Vilket atomnummer har: {utskriven_atom.atombeteckning}? "))
        if gissning == str(utskriven_atom.atomnummer):
            print("Rätt svar!")
            break
        else:
            print("Fel svar, var vänlig och försök igen. ")
            försök +=1
            continue

"""Denna funktion körs om väljaren väljer alternativ 3 i meny-funktionen."""
"""Den gör som funktion innan denna bortsätt från att atomnummer och atombeteckning byter plats."""
def alternativ_3(sorterad_lista):
    utskriven_atom = random.choice(sorterad_lista)
    försök = 0
    while försök < 3:
        gissning = input(f"Vilken atombeteckning har följande atomnummer: {utskriven_atom.atomnummer}? ")
        if gissning == utskriven_atom.atombeteckning:
            print("Rätt svar!")
            break
        else:
            print("Fel svar, var vänlig och försök igen.")
            försök += 1
            continue

"""Denna funktion körs om väljaren väljer alternativ 4 i meny-funktionen."""
"""Funktionen gör så att tre godtyckliga atommassor skrivs ut."""
"""Personen som kör programmet ska sedan skriva in den rätta alternativet på atommassan till den godtyckligt utskrivna atomen."""
"""Gör så att det skrivs ut i godtycklig ordning."""
def alternativ_4(sorterad_lista):
    svarsalternativ_rätt = random.choice(sorterad_lista)
    svarsalternativ_fel1 = random.choice(sorterad_lista)
    svarsalternativ_fel2 = random.choice(sorterad_lista)
    försök = 0
    while försök < 3:
        användarens_gissning = (input(f"Vilken av följande atommassa ({svarsalternativ_fel1.atommassa}, {svarsalternativ_rätt.atommassa} eller {svarsalternativ_fel2.atommassa}) har grundämnet: {svarsalternativ_rätt.atombeteckning}? "))
        if användarens_gissning == (svarsalternativ_rätt.atommassa):
            print("Rätt svar!")
            break
        else:
            print("Fel svar, var vänlig och försök igen.")
            försök += 1
            continue

"""Denna funktion körs om väljaren väljer alternativ 5 i meny-funktionen."""
"""Funktionen gör så att programmet avslutas."""
def alternativ_5():
    print("Programmet avslutas.")
    exit()

"""listan är global då den används i flera olika funktoner."""
if __name__ == "__main__":
    skapa_lista()