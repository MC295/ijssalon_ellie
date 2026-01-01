#2. dictionary met waarden voor aardbei 3, vanille 4 en chocolade 5
prijzen = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5
}
# 3. Bereken de aanbieding (aardbei vermenigvuldigd met 0.8)
aanbieding = prijzen["aardbei"] * 0.8

#4. reclametekst met een formatted string
reclame_tekst= f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"

#5 printopdracht van punt 4 verwijderd
komma_index= reclame_tekst.index(",") #5. index van de komma zoeken
nul_index= reclame_tekst.index("0",komma_index) #5. index van de eerste 0 na de komma zoeken
reclame_tekst2=reclame_tekst[:nul_index+1] #5. deel van de string nemen tem eerste 0 na de komma

#print uit stap 5 gewist
# 6 zet de  tekst uit reclame_tekst 2 om in hoofdletters
reclame_tekst3=reclame_tekst2.upper()

#7 print uit stap 6 wissen
#7 de tekst uit reclame_tekst3 splitsen
reclame_tekst4=reclame_tekst3.split(" ")

#8 print opdracht uit 7 gewist
# for loop van de tekst in reclame_tekst4 +printen
for el in reclame_tekst4:
    print (el)