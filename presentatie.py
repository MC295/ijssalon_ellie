from helper import onderstreep

def presenteer(mijn_dictionary,totaal):
    for item, waarde in mijn_dictionary.items():
        print(f"{item} : {waarde} euro")

    totaal_regel = f"Totaal : {totaal} euro"
    print("=" * len(totaal_regel))
    print(totaal_regel)
