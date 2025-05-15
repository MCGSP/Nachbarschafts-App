artikel = [] # Liste wird erstellt
print("Willkommen bei der Leih- und Tauschbörse!")
wahl = input("Möchtest du einen Artikel hinzufügen, leihen oder tauschen? Dann gib das entsprechende Wort ein: ")
while wahl != "x": # Schleife die sich nur bei der Eingabe "x" vom Benutzer beendet
    if wahl == "hinzufügen":
        neuerArtikel = input("Was möchtest du hinzufügen?: ") # Variable um genau den Artikel den 
        artikel.insert(0,neuerArtikel)                        # der Benutzer eingibt hinzuzufügen
        
    elif wahl == "leihen":
        print("Diese Artikel sind verfügbar:")
        for i in range(0, len(artikel)): # Zählschleife um alle Artikel anzuzeigen
            print(artikel[i])
        artikelLeihen = input("Welchen möchtest du leihen?: ")
        for i in range(0, len(artikel)):
            if artikel[i] == artikelLeihen: # Jeder Durchgang der Zählschleife prüft einen Artikel in der Liste,
                artikel.pop(i)              # ob er der vom Benutzer ausgeliehene Artikel ist und entfernt ihn dann
        
    elif wahl == "tauschen":
        print("Diese Artikel sind verfügbar:")
        for i in range(0, len(artikel)): # Zählschleife um alle Artikel anzuzeigen
            print(artikel[i])
        eintauschArtikel = input("Welchen Artikel gibst du ab?: ")
        artikelTausch = input("Und welchen Artikel nimmst du dafür?: ")
        for i in range(0, len(artikel)):
            if artikel[i] == eintauschArtikel:
                artikel[i] = artikelTausch
    
    wahl = input("Möchtest du noch einen Artikel hinzufügen, leihen oder tauschen? Gib andernfalls x ein um das Programm zu beenden: ")