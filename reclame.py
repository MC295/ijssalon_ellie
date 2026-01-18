def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting= prijs-(prijs*korting)
    string_prijs = f"{prijs:.2f}"
    string_prijs_na_korting = f"{prijs_na_korting:.2f}"
    return (f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {string_prijs} euro voor {string_prijs_na_korting} euro.")

def inkomsten_totaal(inkomsten):
    return sum(inkomsten)
#test of de functie inkomsten_totaal werkt 
print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345]))