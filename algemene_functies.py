#functie die waarden uit tabel teruggeeft maal zichzelf
def mijn_functie_1(a):
    return a*a

def mijn_functie_2(a,b):
    my_list=[a+b, a-b, a*b, a/b] 
    return my_list

#testing mijn_functie_2 met alle waarden uit de tabel
print (mijn_functie_2(12,3))
print (mijn_functie_2(12,2))
print (mijn_functie_2(10,5))
print (mijn_functie_2(100,20))
