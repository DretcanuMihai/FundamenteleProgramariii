#acest modul contine functii ajutatoare generale

def copy_dictionar(dictio):
    """
    aceasta functie creeaza un nou dictionar, copie a lui dictio
    #date de intrare:->dictio - dictionarul ce-l copiem
    ##date de iesire:->dictio_copy - copia dictionarului
    """
    dictio_copy={}
    for elem in dictio:
        dictio_copy[elem]=dictio[elem]
    return dictio_copy

def test_copy_dictionar():
    dictio={}
    assert copy_dictionar(dictio)==dictio
    dictio={1:2, 2:"asd"}
    assert copy_dictionar(dictio)==dictio
    dictio={"ASD":123}
    assert copy_dictionar(dictio)==dictio

def aceeiasi_paritate(x, y):
    """
    functie ce verifica daca x are aceiasi paritate cu y
    #date de intrare:->x - un numar intreg a carui paritate o verificam
                     ->y - un numar intreg a carui paritate o comparam cu cea a lui x
    ##date de iesire:->True - daca cele doua numere au aceiasi paritate
                     ->False - in caz contrar
    """
    return (x%2==y%2)

def test_aceeasi_paritate():
    test=aceeiasi_paritate
    assert test(1,1)==True
    assert test(1,0)==False
    assert test(0, 1)==False
    assert test(1, 255)==True
    assert test(-255, -1)==True
    assert test(123, 23)==True
    assert test(23, 123)==True
    assert test(123, -22)==False
    assert test(-22, 123)==False
    assert test(0, 2)==True
    assert test(2, 0)==True
    assert test(-12, -222)==True
    assert test(-222, -12)==True

def incep_cu_acelasi_char(string1,string2):
    """
    functie ce verifica daca doua stringuri incep cu acelasi char
    #date de intrare:->string1 - un string nevid
                     ->string2 - un string nevid
    ##date de iesire:->True - daca cele doua stringuri incep cu acelasi char
                     ->False - in caz contrar
    """
    return string1[0]==string2[0]

def test_incep_cu_acelasi_char():
    test=incep_cu_acelasi_char
    assert test("acasa", "nasol")==False
    assert test("nasol", "acasa")==False
    assert test("hmm", "hot")==True
    assert test("hot","hmm")==True
    assert test("##21", "bzz")==False
    assert test("bzz", "##21")==False
    assert test("!21","!ff")==True
    assert test("!ff","!21")==True

def apartine_interval(x, interval):
    """
    functie ce verifica daca un  numar intreg apartine unui interval
    #date de intrare:->x - un numar intreg
                     ->interval - un dictionar ce in "st" tine marginea inferioara si in "dr" marginea superioara
                     a intervalului, st<=dt
    ##date de iesire:->True - daca x apartine intervalului inchis [st, dt]
                     ->False - in caz contrar
    """
    st=interval["st"]
    dr=interval["dr"]
    return (st<=x and x<=dr)

def test_apartine_interval():
    test=apartine_interval
    assert test(1, {"st":1, "dr":1,})==True
    assert test(-2, {"st":-5, "dr":5})==True
    assert test(2, {"st":-5, "dr":5})==True
    assert test(3, {"st":3, "dr":5})==True
    assert test(3, {"st":0, "dr":3})==True
    assert test(5, {"st":-22, "dr":3})==False
    assert test(5, {"st":44, "dr":255})==False

def run_all_tests():
    test_copy_dictionar()
    test_aceeasi_paritate()
    test_incep_cu_acelasi_char()
    test_apartine_interval()

run_all_tests()