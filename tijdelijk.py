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

#print de reclametekst
print(reclame_tekst)
