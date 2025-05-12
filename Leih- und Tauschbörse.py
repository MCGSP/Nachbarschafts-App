artikel = []
wahl = input("Willkommen bei der Leih- und Tauschbörse. Möchtest du einen Artikel hinzufügen, leihen oder tauschen? Dann gib das entsprechende Wort ein: ")
while wahl != "x":
    if wahl == "hinzufügen":
        neuerArtikel = input("Was möchtest du hinzufügen?: ")
        artikel.insert(0,neuerArtikel)
        
    elif wahl == "leihen":
        for i in range(0, len(artikel)):
            print(artikel[i])
        artikel("Diese Artikel sind verfügbar. Welchen möchtest du leihen?: ")
        
    wahl = input("Möchtest du noch einen Artikel hinzufügen, leihen oder tauschen? Gib andernfalls x ein um das Programm zu beenden: ")