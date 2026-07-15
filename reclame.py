from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting= prijs-(prijs*korting)
    string_prijs = f"{prijs:.2f}"
    string_prijs_na_korting = f"{prijs_na_korting:.2f}"
    return (f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {string_prijs} euro voor {string_prijs_na_korting} euro.")

def inkomsten_totaal(inkomsten, btw):
    totaal= sum(inkomsten)
    btw_bedrag=totaal*btw
    return (f"Het totaal van alle inkomsten van deze week is {totaal:.2f} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden.")

def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return [hoogste, laagste]

def gemiddelde(mijn_lijst):
    gem = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gem:.2f} euro."

def meervoudig(invoer_lijst):
    resultaat = laag_en_hoog(invoer_lijst)
    return resultaat

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    resultaat = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return resultaat

