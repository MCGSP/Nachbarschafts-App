artikel = ["Fernseher", "Tisch", "Pulli", "Salz", "Pfeffer", "Pfanne", "Stuhl", "Schuhe", "Monopoly", "Rucksack"] # Liste wird erstellt
print("Willkommen bei der Leih- und Tauschbörse!")
wahl = input("Möchtest du einen Artikel hinzufügen, leihen oder tauschen? Dann gib den jeweiligen Anfangsbuchstaben ein: ")

while wahl != "x": # Schleife die sich nur bei der Eingabe "x" vom Benutzer beendet (also wenn der Benutzer das Programm beenden will)
    if wahl == "h" or wahl == "H":
        neuerArtikel = input("Was möchtest du hinzufügen?: ") # Variable um genau den Artikel den 
        artikel.insert(0,neuerArtikel)                        # der Benutzer eingibt hinzuzufügen
        print("Dein/e " + str(neuerArtikel) + " wurde hinzugefügt.")
        
    elif wahl == "l" or wahl == "L":
        print("Diese Artikel sind verfügbar:")
        for a in artikel: # Zählschleife um alle Artikel anzuzeigen
            print(a)
        artikelLeihen = input("Welchen möchtest du leihen?: ")
        for b in artikel:
            if b == artikelLeihen: # Jeder Durchgang der Zählschleife prüft mithilfe einer Variable einen Artikel in
                artikel.remove(b)# der Liste, ob er der vom Benutzer ausgeliehene Artikel ist und entfernt ihn dann
        print("Der/die " + str(artikelLeihen) + " gehört ab jetzt für eine gewisse Zeit dir.")
        
    elif wahl == "t" or wahl == "T":
        print("Diese Artikel sind verfügbar:")
        for a in artikel: # Zählschleife um alle Artikel anzuzeigen
            print(a)
        eintauschArtikel = input("Welchen Artikel gibst du ab?: ")
        artikelTausch = input("Und welchen Artikel nimmst du dafür?: ")
        c = "a"
        for i in (0, len(artikel)):
            if c == artikelTausch: # Wieder eine prüfende Zählschleife, nur wird
                c = eintauschArtikel  # hier dann der Artikel durch einen neuen ersetzt
        print("Du hast dein/e " + str(eintauschArtikel) + " gegen den/die " + str(artikelTausch) + " getauscht.")
    
    wahl = input("Möchtest du noch einen Artikel hinzufügen, leihen oder tauschen? Gib andernfalls x ein um das Programm zu beenden: ")