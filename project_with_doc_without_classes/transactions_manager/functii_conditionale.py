#functii conditionale/booleane ce vor ajuta la selectarea elementelor dintr-un record de tranzactii
from functii_pentru_data import creeaza_data, data_in_perioada, comp_data
from functii_pentru_tranzactie import get_data, creeaza_tranzactie, get_tip, get_suma

def data_tranzactie_difera(tranzactie, data):
    """
    functie ce veirfica daca data unei tranzactii nu este egala cu o data
    #date de intrare:->tranzactie - tranzactia verificata
                     ->data - data cu care verificam
    ##date de iesire:->True - daca data tranzactiei este diferita de data noastra
                     ->False - in caz contrar
    """
    data_t=get_data(tranzactie)
    return data_t!=data

def test_data_tranzactie_difera():
    test=data_tranzactie_difera
    data=creeaza_data(1, 1, 1)
    tranzactie=creeaza_tranzactie(1, data, 10.00, "intrare")
    assert test(tranzactie, data)==False
    data1=creeaza_data(2, 2, 2)
    tranzactie=creeaza_tranzactie(1, data1, 10.00, "iesire")
    assert test(tranzactie, data)==True
    assert test(tranzactie, data1)==False

def tranzactie_inafara_perioadei(tranzactie, info):
    """
    functie ce verifica daca data unei tranzactii nu este cuprinsa intre doua date
    #date de intrare:->tranzactie - tranzactia verificata
                     ->info - o lista cu data1 si data1 pe pozitiile 0 si 1
    ##date de iesire:->True - daca data tranzactiei nu este cuprinsa intre cele doua date
                     ->False - in caz contrar
    """
    data=get_data(tranzactie)
    data1=info[0]
    data2=info[1]
    return (not data_in_perioada(data, data1, data2))

def test_tranzactie_inafara_perioadei():
    test=tranzactie_inafara_perioadei
    data=creeaza_data(3, 3, 3)
    data1=creeaza_data(2, 2, 2)
    data2=creeaza_data(4, 4, 4)
    info=[data1, data2]
    tranzactie=creeaza_tranzactie(1, data, 1, "intrare")
    assert test(tranzactie, info)==False
    data=creeaza_data(2, 2, 2)
    tranzactie=creeaza_tranzactie(1, data, 1, "intrare")
    assert test(tranzactie, info)==False
    data=creeaza_data(4, 4, 4)
    tranzactie=creeaza_tranzactie(1, data, 1, "intrare")
    assert test(tranzactie, info)==False
    data=creeaza_data(1, 1, 1)
    tranzactie=creeaza_tranzactie(1, data, 1, "intrare")
    assert test(tranzactie, info)==True
    data=creeaza_data(5, 5, 5)
    tranzactie=creeaza_tranzactie(1, data, 1, "intrare")
    assert test(tranzactie, info)==True

def tip_tranzactie_difera(tranzactie, tip):
    """
    functie ce verifica daca tipul unei tranzactii este diferit de un anumit tip
    #date de intrare:->tranzactie - tranzactia ce o verificam
                     ->tip - tipul cu care comparam
    ##date de iesire:->True - daca tipul functiei nu este tip
                     ->False - in caz contrar
    """
    tip_t=get_tip(tranzactie)
    return tip_t!=tip

def test_tip_tranzactie_difera():
    test=tip_tranzactie_difera
    data=creeaza_data(1, 2, 3)
    tranzactie=creeaza_tranzactie(1, data, 1, "iesire")
    assert test(tranzactie, "iesire")==False
    assert test(tranzactie, "intrare")==True
    tranzactie=creeaza_tranzactie(1, data, 1, "intrare")
    assert test(tranzactie, "iesire")==True
    assert test(tranzactie, "intrare")==False

def tip_tranzactie_bun(tranzactie, tip):
    """
    functie ce verifica daca tipul unei tranzactii este tip
    #date de intrare:->tranzactie - tranzactia verificata
                     ->tip - tipul cu care verificam
    ##date de iesire:->True - daca tipul tranzactiei este tip
                     ->False - in caz contrar
    """
    return get_tip(tranzactie)==tip

def test_tip_tranzactie_bun():
    test=tip_tranzactie_bun
    data=creeaza_data(1, 1, 1)
    tranzactie=creeaza_tranzactie(1, data, 1, "iesire")
    assert test(tranzactie, "iesire")==True
    assert test(tranzactie, "intrare")==False
    tranzactie=creeaza_tranzactie(1, data, 1, "intrare")
    assert test(tranzactie, "iesire")==False
    assert test(tranzactie, "intrare")==True

def suma_tranzactie_mai_mare(tranzactie, suma):
    """
    functie ce verifica daca suma unei tranzactii este mai mare ca o suma data
    #date de intrare:->tranzactie - tranzactia ce o verificam
                     ->suma - suma de comparatie, nr rational pozitiv
    ##date de iesire:->True - daca suma tranzactiei este mai mare ca suma
                     ->False - in caz contrar
    """
    suma_t=get_suma(tranzactie)
    return suma_t>suma

def test_suma_tranzactie_mai_mare():
    test=suma_tranzactie_mai_mare
    data=creeaza_data(1, 1, 1)
    tranzactie=creeaza_tranzactie(1, data, 100.00, "intrare")
    assert test(tranzactie, 99.00)==True
    assert test(tranzactie, 100.00)==False
    assert test(tranzactie, 100.01)==False
    tranzactie=creeaza_tranzactie(1, data, 4.0, "iesire")
    assert test(tranzactie, 5.00)==False
    assert test(tranzactie, 4.00)==False
    assert test(tranzactie, 3.99)==True

def suma_tip_tranzactie_mai_mare(tranzactie, info):
    """
    functie ce verifica daca data unei tranzactii este precedenta unei zile si suma acesteia este mai mare decat o suma
    data
    #date de intrare:->tranzactie - tranzactia ce o verificam
                     ->info - lista ce contine pe pozitia 0 data, iar pe pozitia 1 suma ce trebuie utilizate in
                     validare
    ##date de iesire:->True - data tranzactia verifica conditiile
                     ->False - in caz contrar
    """
    suma_t=get_suma(tranzactie)
    data_t=get_data(tranzactie)
    data=info[0]
    suma=info[1]
    return ((suma_t>suma) and comp_data(data, data_t))

def test_suma_tranzactie_tip_mai_mare():
    test=suma_tip_tranzactie_mai_mare
    data=creeaza_data(2, 2, 2)
    tranzactie=creeaza_tranzactie(1, data, 20.0, "intrare")
    assert test(tranzactie, [data, 1.0])==False
    assert test(tranzactie, [data,20.0])==False
    assert test(tranzactie, [data,21.0])==False
    data=creeaza_data(1, 1, 1)
    assert test(tranzactie, [data,1.0])==False
    assert test(tranzactie, [data,20.0])==False
    assert test(tranzactie, [data,21.0])==False
    data=creeaza_data(3, 3, 3)
    assert test(tranzactie, [data,1.0])==True
    assert test(tranzactie, [data,20.0])==False
    assert test(tranzactie, [data,21.0])==False

def if_tip_nosubsum(tranzactie, info):
    """
    functie ce verifica daca o tranzactie indeplineste urmatoarea conditie: daca tipul acesteia este diferit de tipul
    dat, conditia este indeplinita; in caz contrar, daca suma tranzactiei depaseste sau este egala cu suma data,
    conditia este din nou indeplinita; in caz contrar, nu este indeplinita
    #date de intrare:->tranzactie - tranzactia ce o verificam
                     ->info - o lista ce contine pe pozitia 0 suma, iar pe pozitia 1 tipul
    ##date de iesire:->True - daca conditia este indeplinita
                     ->False - in caz contrar
    """
    suma_t=get_suma(tranzactie)
    tip_t=get_tip(tranzactie)
    suma=info[0]
    tip=info[1]
    return ((tip!=tip_t)or(suma_t>=suma))

def test_if_tip_nosubsum():
    test=if_tip_nosubsum
    data=creeaza_data(1, 1, 1)
    tranzactie=creeaza_tranzactie(1, data, 20.00, "intrare")
    assert test(tranzactie,[19.99, "iesire"])==True
    assert test(tranzactie,[20.00, "iesire"])==True
    assert test(tranzactie,[20.01, "iesire"])==True
    assert test(tranzactie,[19.99, "intrare"])==True
    assert test(tranzactie,[20.00, "intrare"])==True
    assert test(tranzactie,[20.01, "intrare"])==False

def data_tranzactie_buna(tranzactie, data):
    """
    functie ce verifica daca data unei tranzactii este precedenta sau egala cu o data
    #date de intrare:->tranzactie - tranzactia verificata
                     ->data - data cu care se compara
    ##date de iesire:->True - daca data tranzactiei este precedenta sau egala cu data data
                     ->False - in caz contrar
    """
    return (not comp_data(get_data(tranzactie), data))

def test_data_tranzactie_buna():
    test=data_tranzactie_buna
    data=creeaza_data(1, 1, 1)
    tranzactie=creeaza_tranzactie(1, data,1, "intrare")
    assert test(tranzactie, data)==True
    data=creeaza_data(2, 2, 2)
    assert test(tranzactie, data)==True
    tranzactie=creeaza_tranzactie(1, data, 1, "iesire")
    assert test(tranzactie, data)==True
    data=creeaza_data(1, 1, 1)
    assert test(tranzactie, data)==False

def run_all_tests():
    test_data_tranzactie_difera()
    test_tranzactie_inafara_perioadei()
    test_tip_tranzactie_difera()
    test_tip_tranzactie_bun()
    test_suma_tranzactie_mai_mare()
    test_suma_tranzactie_tip_mai_mare()
    test_if_tip_nosubsum()
    test_data_tranzactie_buna()

run_all_tests()