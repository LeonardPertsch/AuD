"""
Hash-Tabelle: Personenregister
==============================

Personen werden in einer Liste gespeichert; zwei Hash-Tabellen (nach
Familienname und nach vollem Namen) erlauben schnelle Suche über Indizes.
"""

class Person:
    def __init__(self, familienname, vorname, geburtsdatum, geburtsort, adresse, geschlecht):
        self.familienname = familienname
        self.vorname = vorname
        self.geburtsdatum = geburtsdatum
        self.geburtsort = geburtsort
        self.adresse = adresse
        self.geschlecht = geschlecht

    def __repr__(self):
        return f"({self.familienname}, {self.vorname}, {self.geburtsdatum}, {self.geburtsort}, {self.adresse}, {self.geschlecht})"


# Hashtabellen und Hauptliste
HASH_SIZE = 100
familienname_hash = [[] for _ in range(HASH_SIZE)]
vollstaendiger_name_hash = [[] for _ in range(HASH_SIZE)]
personen_liste = []


# Hash-Funktion
def hash_funktion(word, length):
    result = 0
    for char in word:
        result = result * 31 + ord(char)
    return result % length


# Funktion zum Hinzufügen einer Person
def add_person(person):
    personen_liste.append(person)
    index = len(personen_liste) - 1

    hash_key_fam = hash_funktion(person.familienname, HASH_SIZE)
    familienname_hash[hash_key_fam].append(index)

    hash_key_voll = hash_funktion(person.familienname + person.vorname, HASH_SIZE)
    vollstaendiger_name_hash[hash_key_voll].append(index)


# Suche nach Familienname
def find_by_familienname(familienname):
    hash_key = hash_funktion(familienname, HASH_SIZE)
    return [personen_liste[i] for i in familienname_hash[hash_key] if personen_liste[i].familienname == familienname]


# Suche nach vollständigem Namen
def find_by_full_name(familienname, vorname):
    hash_key = hash_funktion(familienname + vorname, HASH_SIZE)
    return [personen_liste[i] for i in vollstaendiger_name_hash[hash_key] if
            personen_liste[i].familienname == familienname and personen_liste[i].vorname == vorname]


# Testfälle
add_person(Person("Müller", "Anna", "12.03.1985", "Berlin", "Musterstraße 1", "weiblich"))
add_person(Person("Müller", "Peter", "05.07.1990", "Hamburg", "Beispielweg 5", "männlich"))
add_person(Person("Schmidt", "Klaus", "08.11.1970", "München", "Hauptstraße 12", "männlich"))
add_person(Person("Meier", "Sophie", "25.06.1992", "Stuttgart", "Schulweg 3", "weiblich"))



# Abfragen
print(find_by_familienname("Müller"))  # Erwartet: [Anna Müller, Peter Müller]
print(find_by_full_name("Müller", "Anna"))  # Erwartet: [Anna Müller]
print(find_by_familienname("Schmidt"))  # Erwartet: [Klaus Schmidt]
print(find_by_familienname("Meier"))  # Erwartet: [Sophie Meier]
print(find_by_full_name("Müller", "Max"))  # Erwartet: [] (nicht vorhanden)

print(personen_liste)
print(vollstaendiger_name_hash)
print(familienname_hash)
