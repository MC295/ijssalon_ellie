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

print (reclame_tekst2) #print de string 
