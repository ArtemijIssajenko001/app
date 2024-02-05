nimed=["Mati","Kati"]
try:
    while True:
        valik=input("Andmete lisamine-add\nAndmete nätamine-show\n Kustutamine-del\nJärjendi pööramine-rev\nAndmete kustutamine-clear\nAndemete sortimine-sort\n")
        if valik=="add":
           valik=int(input("Kas lisame mitu inimest(mitu) lisamine või positsioonile(pos)" ))
           if valik=="mitu":
               mitu=int(input("Mitu inimest lisame?"))
               for i in range(mitu):
                   nimi=input("Sisesta nimi: ")
                   nimed.append(nimi)
           else:
               indeks=int(input("Kuhu lisamine "))
               nimi=input("Mis nimi: ")
               nimed.insert(indeks-1,nimi)
        elif valik=="del":
            valik=input("Kas kustutame nimi(nimi) või indeksi järgi (ind)?")
            if valik=="nimi":
                nimi=input("Mis nimi in vaja kustutada? ")
                kogus=nimed.count(nimi)
                if kogus>0:
                    for i in range(kogus):
                       nimed.remove(nimi)
                else:
                    print(f"Nimi {nimi} ei ole nimekirjas")
            else:
                indeks=int(input("Mis on järjekordne number?"))
                nimed.pop(indeks-1)
        elif valik=="show":
            print(nimed)
        elif valik=="rev":
             nimed.reverse()
             print(nimed)
        elif valik=="sort":
             nimed.sort()
             print(nimed)
        elif valik=="clear":
             nimed.clear()
             print(nimed)
        elif valik=="ots":
            nimi=input("Mis nime otsime? ")
            if nimed .count(nimi)>0:
                for i in range(len(nimed)):
                    ind=nimed.index(nimi,i)
                    print(f"{nimi} on indeksiga {ind+1}")
            else:
                print(f"{nimi} ei ole nimekirjas")
except :
    print("Kasutage õiget tüüpi andmeid")
