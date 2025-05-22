artikel = ["Fernseher", "Tisch", "Pulli", "Salz", "Pfeffer", "Pfanne", "Stuhl", "Schuhe", "Monopoly", "Rucksack"] # Liste wird erstellt
print("Willkommen bei der Leih- und Tauschbörse!")
wahl = input("Möchtest du einen Artikel hinzufügen, leihen oder tauschen? Dann gib den jeweiligen Anfangsbuchstaben ein: ")

while wahl != "x": # Schleife die sich nur bei der Eingabe "x" vom Benutzer beendet
    if wahl == "hinzufügen":
        neuerArtikel = input("Was möchtest du hinzufügen?: ") # Variable um genau den Artikel den 
        artikel.insert(0,neuerArtikel)                        # der Benutzer eingibt hinzuzufügen
        
    elif wahl == "leihen":
        print("Diese Artikel sind verfügbar:")
        for a in artikel: # Zählschleife um alle Artikel anzuzeigen
            print(a)
        artikelLeihen = input("Welchen möchtest du leihen?: ")
        for b in artikel:
            if b == artikelLeihen: # Jeder Durchgang der Zählschleife prüft einen Artikel in der Liste,
                artikel.remove(b)  # ob er der vom Benutzer ausgeliehene Artikel ist und entfernt ihn dann
        
    elif wahl == "tauschen":
        print("Diese Artikel sind verfügbar:")
        for a in artikel: # Zählschleife um alle Artikel anzuzeigen
            print(a)
        eintauschArtikel = input("Welchen Artikel gibst du ab?: ")
        artikelTausch = input("Und welchen Artikel nimmst du dafür?: ")
        for c in artikel:
            if c == artikelTausch: # Wieder eine prüfende Zählschleife, nur wird
                c = artikelTausch  # hier dann der Artikel durch einen neuen ersetzt
    
    wahl = input("Möchtest du noch einen Artikel hinzufügen, leihen oder tauschen? Gib andernfalls x ein um das Programm zu beenden: ")