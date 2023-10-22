#modul cu functiile pentru functionalitati

from functii_pentru_tranzactie import creeaza_valideaza_tranzactie,set_tid, creeaza_valideaza_tid, creeaza_valideaza_tip, creeaza_valideaza_suma, creeaza_valideaza_data_si_suma, creeaza_valideaza_suma_si_tip
from functii_pentru_record_info import get_index, get_record, adauga_element_record_ri_nv, initializare_record_info, validare_tid_in_record, actualizare_element_record_ri, subrecord_prop_info, get_istoric, update_istoric, set_record, scrie_element_record, set_index
from functii_pentru_data import creeaza_valideaza_data, creeaza_valideaza_perioada
from functii_conditionale import *
from functii_prelucrari_rapoarte import *

def adauga_tranzactie(record_info, zi, luna, an, suma, tip):
    """
    functie ce adauga o tranzactie in informatiile unor recorduri de tranzactii
    #date de intrare:->record_info - informatiile recordului de modificat
                     ->zi - string reprezentand ziua
                     ->luna - string reprezentand luna
                     ->an - string reprezentand anul
                     ->suma - string reprezentand suma
                     ->tip - string reprezentand tipul
    ##date de iesire:-> -
    programul modifica in mod direct informatiile recordului
    daca apar erori, recordul nu se modifica si se va ridica o exceptie
    """
    try:
        tranzactie=creeaza_valideaza_tranzactie(zi, luna, an, suma, tip)
    except Exception as eroare:
        raise Exception(eroare)
    index=get_index(get_record(record_info))+1
    set_tid(tranzactie, index)
    adauga_element_record_ri_nv(record_info, tranzactie)

def test_adauga_tranzactie():
    test=adauga_tranzactie
    record_info=initializare_record_info()
    test(record_info, "1", "1", "1", "123", "intrare")
    ri=initializare_record_info()
    tranzactie=creeaza_valideaza_tranzactie("1", "1", "1", "123", "intrare")
    set_tid(tranzactie, 1)
    adauga_element_record_ri_nv(ri, tranzactie)
    assert ri==record_info
    test(record_info, "17", "3", "2004", "22.22", "iesire")
    tranzactie=creeaza_valideaza_tranzactie("17", "3", "2004", "22.22", "iesire")
    set_tid(tranzactie, 2)
    adauga_element_record_ri_nv(ri, tranzactie)
    assert ri==record_info
    try:
        test(record_info, "asd","asd", "asd", "12.22", "oops")
        assert False
    except Exception as eroare:
        mesaj=""
        mesaj=mesaj+"Eroare:ziua, luna si anul datei trebuie sa fie de tip nr. natural nenul;\n"
        mesaj=mesaj+"Eroare:tipul trebuie sa fie un string egal cu 'intrare' sau cu 'iesire';\n"
        assert str(eroare)==mesaj

def actualizeaza_tranzactie(record_info, tid, zi, luna, an, suma, tip):
    """
    functie ce actualizeaza o tranzactie de pe un anumit tid
    #date de intrare:->record_info - informatiile recordului de modificat
                     ->tid - string reprezentand tid-ul
                     ->zi - string reprezentand ziua
                     ->luna - string reprezentand luna
                     ->an - string reprezentand anul
                     ->suma - string reprezentand suma
                     ->tip - string reprezentand tipul
    ##date de iesire:-> -
    programul modifica in mod direct informatiile recordului
    daca apar erori, recordul nu se modifica si se va ridica o exceptie
    """
    erori=""
    try:
        tid=creeaza_valideaza_tid(tid)
        validare_tid_in_record(get_record(record_info), tid)
    except Exception as eroare:
        erori=erori+str(eroare)
    try:
        tranzactie=creeaza_valideaza_tranzactie(zi, luna, an, suma, tip)
    except Exception as eroare:
        erori=erori+str(eroare)
    if(len(erori)>0):
        raise Exception(erori)
    set_tid(tranzactie, tid)
    actualizare_element_record_ri(record_info, tranzactie, tid)

def test_actualizare_tranzactie():
    record_info=initializare_record_info()
    adauga_tranzactie(record_info, "12", "12", "12", "200", "intrare")
    adauga_tranzactie(record_info, "1", "1", "2020", "25.25", "iesire")
    adauga_tranzactie(record_info, "31", "1", "2000", "1444", "iesire")
    actualizeaza_tranzactie(record_info,"1", "22", "1", "2012", "200", "intrare")
    ri=initializare_record_info()
    adauga_tranzactie(ri, "12", "12", "12", "200", "intrare")
    adauga_tranzactie(ri, "1", "1", "2020", "25.25", "iesire")
    adauga_tranzactie(ri, "31", "1", "2000", "1444", "iesire")
    tranzactie=creeaza_valideaza_tranzactie("22", "1", "2012", "200", "intrare")
    set_tid(tranzactie, 1)
    actualizare_element_record_ri(ri, tranzactie, 1)
    assert ri==record_info
    actualizeaza_tranzactie(record_info, "3", "12", "12", "12", "12", "intrare")
    tranzactie=creeaza_valideaza_tranzactie("12", "12", "12", "12", "intrare")
    set_tid(tranzactie, 3)
    actualizare_element_record_ri(ri, tranzactie, 3)
    assert ri==record_info
    try:
        actualizeaza_tranzactie(record_info, "-1", "asd", "asd", "asd", "asd", "asd")
        assert False
    except Exception as eroare:
        mesaj=""
        mesaj=mesaj+"Eroare:tid-ul trebuie sa fie de tip nr. natural nenul;\n"
        mesaj=mesaj+"Eroare:ziua, luna si anul datei trebuie sa fie de tip nr. natural nenul;\n"
        mesaj=mesaj+"Eroare:suma trebuie sa fie de tip nr. rational pozitiv;\n"
        mesaj=mesaj+"Eroare:tipul trebuie sa fie un string egal cu 'intrare' sau cu 'iesire';\n"
        assert str(eroare)==mesaj
    try:
        actualizeaza_tranzactie(record_info, "4", "1", "1", "1", "1", "iesire")
        assert False
    except Exception as eroare:
        assert str(eroare)=="Eroare:nu exista element cu tid-ul specificat in lista;\n"

def up_creeaza_valideaza_perioada(info):
    return creeaza_valideaza_perioada(info[0], info[1], info[2], info[3], info[4], info[5])

def up_creeaza_valideaza_data(info):
    return creeaza_valideaza_data(info[0], info[1], info[2])

def up_creeaza_valideaza_data_si_suma(info):
    return creeaza_valideaza_data_si_suma(info[0], info[1], info[2], info[3])

def up_creeaza_valideaza_suma_si_tip(info):
    return creeaza_valideaza_suma_si_tip(info[0],info[1])

def initializare_validari_mod():
    """
    functii ce initializeaza dictionarul cu functii de validare a informatiilor necesare unor conditii de modificare
    #date de intrare:-> -
    ##date de iesire:->citiri - un dictionar de functii de validare
    """
    validari={}
    validari["sterge_zi"] = up_creeaza_valideaza_data
    validari["sterge_perioada"] = up_creeaza_valideaza_perioada
    validari["sterge_tip"] = creeaza_valideaza_tip
    return validari

def initializare_conditii_mod():
    """
    functie ce initializeaza dictionarul cu conditii pentru functia de tip modificare
    #date de intrare:-> -
    ##date de iesire:->conditii - un dictionar de functii de tip boolean
    """
    conditii={}
    conditii["sterge_zi"] = data_tranzactie_difera
    conditii["sterge_perioada"] = tranzactie_inafara_perioadei
    conditii["sterge_tip"] = tip_tranzactie_difera
    return conditii

def record_mod(record_info, cond, info):
    """
    functie ce modifica un record_info in functie de o conditie cond si niste informatii info
    #date de intrare:->record_info - informatiile recordului de modificat
                     ->cond - conditia, de preferat string
                     ->info - informatiile (orice tip de data ce corespunde conditiei)
    ##date de iesire:-> -
    Programul modifica in mod direct informatiile recordului
    """
    validari=initializare_validari_mod()
    try:
        info=validari[cond](info)
    except Exception as eroare:
        raise Exception(eroare)
    conditii=initializare_conditii_mod()
    record=get_record(record_info)
    subrecord=subrecord_prop_info(record, conditii[cond], info)
    if(subrecord==record):
        raise Exception("Aceasta operatie nu a cauzat nicio schimbare in record;")
    istoric=get_istoric(record_info)
    update_istoric(istoric, record)
    set_record(record_info, subrecord)

def test_record_mod():
    test=record_mod
    record_info=initializare_record_info()
    adauga_tranzactie(record_info, "12", "12", "12", "200", "intrare")
    adauga_tranzactie(record_info, "1", "1", "2020", "25.25", "iesire")
    adauga_tranzactie(record_info, "31", "1", "2000", "1444", "iesire")
    test(record_info, "sterge_perioada", ["1", "1", "1", "1", "1", "2001"])
    ri=initializare_record_info()
    r=get_record(ri)
    tranzactie=creeaza_valideaza_tranzactie("1", "1", "2020", "25.25", "iesire")
    set_tid(tranzactie, 2)
    scrie_element_record(r, tranzactie, 2)
    set_index(r, 3)
    assert get_record(record_info)==r
    try:
        test(record_info, "sterge_zi", ["1", "1", "1"])
        assert False
    except Exception as eroare:
        assert str(eroare)=="Aceasta operatie nu a cauzat nicio schimbare in record;"
    test(record_info, "sterge_tip", "iesire")
    ri=initializare_record_info()
    r=get_record(ri)
    set_index(r, 3)
    assert get_record(record_info)==get_record(ri)

def initializare_validari_cautare():
    """
    functie ce initializeaza dictionarul cu functii de validare a informatiilor necesare unor conditii de cautare
    #date de intrare:-> -
    ##date de iesire:->citiri - un dictionar de functii de validare
    """
    validari={}
    validari["cautare_supsum"] = creeaza_valideaza_suma
    validari["cautare_supsum_prezi"] = up_creeaza_valideaza_data_si_suma
    validari["cautare_tip"] = creeaza_valideaza_tip
    validari["filtrare_notip"] = creeaza_valideaza_tip
    validari["filtrare_iftip_nosubsum"] = up_creeaza_valideaza_suma_si_tip
    return validari

def initializare_conditii_cautare():
    """
    functie ce initializeaza dictionarul cu conditii de cautare a unui subrecord intr-un record
    #date de intrare:-> -
    ##date de iesire:->conditii - un dictionar de functii de tip boolean
    """
    conditii={}
    conditii["cautare_supsum"] = suma_tranzactie_mai_mare
    conditii["cautare_supsum_prezi"] = suma_tip_tranzactie_mai_mare
    conditii["cautare_tip"] = tip_tranzactie_bun
    conditii["filtrare_notip"] = tip_tranzactie_difera
    conditii["filtrare_iftip_nosubsum"] = if_tip_nosubsum
    return conditii

def initializare_erori_np_cautare():
    """
    functie ce initializeaza o lista cu conditiile pentru care se afiseaza eroarea "no_prop"
    #date de intrare:-> -
    ##date de iesire:->lista - o lista cu conditiile mentionate mai sus
    """
    lista=[]
    lista.append("cautare_supsum")
    lista.append("cautare_supsum_prezi")
    lista.append("cautare_tip")
    return lista

def cautare_subrecord(record_info, cond, info):
    """
    functie ce cauta in recordul actual elementele ce satisfac o conditie si returneaza un record cu respectivele
    #date de intrare:->record_info - informatiile recordului de unde luam recordul
                     ->cond - conditia, de preferat string
                     ->info - informatiile (orice tip de data ce corespunde conditiei)
    ##date de iesire:->subrecord - subrecordul ce respecta conditiile
    Daca apar erori, acestea vor fi ridicate ca exceptie
    """
    validari=initializare_validari_cautare()
    try:
        info=validari[cond](info)
    except Exception as eroare:
        raise Exception(eroare)
    conditii=initializare_conditii_cautare()
    record=get_record(record_info)
    subrecord=subrecord_prop_info(record, conditii[cond],info)
    np=initializare_erori_np_cautare()
    if(len(subrecord)==1)and (cond in np):
        raise Exception("Nu exista tranzactii cu proprietatea ceruta;")
    return subrecord

def test_cautare_subrecord():
    test=cautare_subrecord
    record_info=initializare_record_info()
    adauga_tranzactie(record_info, "21", "1", "2009", "100.01", "intrare")
    adauga_tranzactie(record_info, "13", "2", "2010", "100", "intrare")
    adauga_tranzactie(record_info, "2", "1", "2009", "124", "intrare")
    adauga_tranzactie(record_info, "24", "7", "2000", "99", "iesire")
    adauga_tranzactie(record_info, "23", "1", "2016", "123", "iesire")
    ri=initializare_record_info()
    r=get_record(ri)
    set_index(r, 5)
    tranzactie=creeaza_valideaza_tranzactie("21", "1", "2009", "100.01", "intrare")
    set_tid(tranzactie, 1)
    scrie_element_record(r, tranzactie, 1)
    tranzactie=creeaza_valideaza_tranzactie("2", "1", "2009", "124", "intrare")
    set_tid(tranzactie, 3)
    scrie_element_record(r, tranzactie, 3)
    assert r==test(record_info, "cautare_supsum_prezi", ["1","1","2013", "100"])
    ri=initializare_record_info()
    adauga_tranzactie(ri, "21", "1", "2009", "100.01", "intrare")
    adauga_tranzactie(ri, "13", "2", "2010", "100", "intrare")
    adauga_tranzactie(ri, "2", "1", "2009", "124", "intrare")
    r=get_record(ri)
    set_index(r, 5)
    assert r==test(record_info, "filtrare_notip", "iesire")
    set_index(r, 3)
    try:
        r=test(ri, "cautare_tip", "iesire")
        assert False
    except Exception as eroare:
        assert str(eroare)=="Nu exista tranzactii cu proprietatea ceruta;"
    try:
        r=test(record_info,"filtrare_iftip_nosubsum", ["asd", "asd"])
        assert False
    except Exception as eroare:
        mesaj=""
        mesaj=mesaj+"Eroare:suma trebuie sa fie de tip nr. rational pozitiv;\n"
        mesaj=mesaj+"Eroare:tipul trebuie sa fie un string egal cu 'intrare' sau cu 'iesire';\n"
        assert str(eroare)==mesaj

def initializare_validari_rapoarte():
    """
    functii ce initializeaza dictionarul cu validari pentru informatiile necesare unor rapoarte de record
    #date de intrare:-> -
    ##date de iesire:->validari - un dictionar de functii de validare
    """
    validari={}
    validari["raport_sumtip"] = creeaza_valideaza_tip
    validari["raport_sold_zi"] = up_creeaza_valideaza_data
    validari["raport_tip_ascsum"] = creeaza_valideaza_tip
    return validari

def initializare_conditii_rapoarte():
    """
    functii ce initializeaza dictionarul cu conditii pentru rapoartele a unui record
    #date de intrare:-> -
    ##date de iesire:->conditii - un dictionar de functii de tip boolean
    """
    conditii={}
    conditii["raport_sumtip"] = tip_tranzactie_bun
    conditii["raport_sold_zi"] = data_tranzactie_buna
    conditii["raport_tip_ascsum"] = tip_tranzactie_bun
    return conditii

def initializare_prelucrari_rapoarte():
    """
    functii ce initalizeaza dictionarul cu functii de prelucrare/gasire a informatiilor rapoartelor
    #date de intrare:-> -
    ##date de iesire:-> prelucrari - un dictionar de functii de prelucrare
    """
    prelucrari={}
    prelucrari["raport_sumtip"] = suma_total
    prelucrari["raport_sold_zi"] = sold_total
    prelucrari["raport_tip_ascsum"] = ordonare_record
    return prelucrari

def rapoarte_record(record_info, cond, info):
    """
    functie ce determina si afiseaza anumite rapoarte legate de recordul actual
    #date de intrare:->record_info - informatiile recordului cu care lucram
                     ->cond - conditia, de preferat string
                     ->info - informatiile (orice tip de data ce corespunde conditiei)
    ##date de iesire:->rap - informatia generata de raport
    Daca apar erori, acestea vor fi ridicate ca exceptie
    """
    validari=initializare_validari_rapoarte()
    try:
        info=validari[cond](info)
    except Exception as eroare:
        raise Exception(eroare)
    conditii=initializare_conditii_rapoarte()
    record=get_record(record_info)
    subrecord=subrecord_prop_info(record, conditii[cond], info)
    if(len(subrecord)==1 and cond!="raport_sold_zi"):
        raise Exception("Nu exista tranzactii cu proprietatea ceruta;")
    prelucrari=initializare_prelucrari_rapoarte()
    rap=prelucrari[cond](subrecord)
    return rap

def test_rapoarte_record():
    test=rapoarte_record
    record_info=initializare_record_info()
    adauga_tranzactie(record_info, "21", "1", "2009", "100.01", "intrare")
    adauga_tranzactie(record_info, "13", "2", "2010", "100", "intrare")
    adauga_tranzactie(record_info, "2", "1", "2009", "124", "intrare")
    adauga_tranzactie(record_info, "24", "7", "2000", "99", "iesire")
    adauga_tranzactie(record_info, "23", "1", "2016", "123", "iesire")
    assert test(record_info, "raport_sumtip", "intrare")==324.01
    assert test(record_info, "raport_sold_zi", ["1", "1", "2011"])==225.01
    record_info=initializare_record_info()
    adauga_tranzactie(record_info, "21", "1", "2009", "100.01", "intrare")
    adauga_tranzactie(record_info, "13", "2", "2010", "100", "intrare")
    adauga_tranzactie(record_info, "2", "1", "2009", "124", "intrare")
    try:
        rap=test(record_info, "raport_tip_ascsum","iesire")
        assert False
    except Exception as eroare:
        assert str(eroare)=="Nu exista tranzactii cu proprietatea ceruta;"

def undo(record_info):
    """
    functie ce da undo la operatiile de modificare efectuate asupra recordului
    #date de intrare:->record_info - informatiile recordului pe care aplicam undo
    ##date de iesire:-> -
    functia modifica in mod direct infomratiile recordului
    daca istoricul este gol, se va ridica o exceptie cu mesjaul "Eroare:Nu exista un stadiu precedent al informatiilor recordului;"
    """
    istoric=get_istoric(record_info)
    if(len(istoric)==0):
        raise Exception("Eroare:Nu exista un stadiu precedent al informatiilor recordului;")
    set_record(record_info, istoric.pop())

def test_undo():
    record_info=initializare_record_info()
    try:
        undo(record_info)
        assert False
    except Exception as eroare:
        assert str(eroare)=="Eroare:Nu exista un stadiu precedent al informatiilor recordului;"
    adauga_tranzactie(record_info,"1","1","1","1","intrare")
    adauga_tranzactie(record_info,"2","2","2","2","intrare")
    adauga_tranzactie(record_info,"3","3","3","3","iesire")
    record_mod(record_info,"sterge_tip","intrare")
    actualizeaza_tranzactie(record_info,"3","1","1","1","1","intrare")
    adauga_tranzactie(record_info,"4","4","4","4","iesire")
    undo(record_info)
    ri=initializare_record_info()
    adauga_tranzactie(ri, "1", "1", "1", "1", "intrare")
    adauga_tranzactie(ri, "2", "2", "2", "2", "intrare")
    adauga_tranzactie(ri, "3", "3", "3", "3", "iesire")
    record_mod(ri, "sterge_tip", "intrare")
    actualizeaza_tranzactie(ri, "3", "1", "1", "1", "1", "intrare")
    assert get_record(ri)==get_record(record_info)
    assert get_istoric(ri)==get_istoric(record_info)
    undo(record_info)
    ri=initializare_record_info()
    adauga_tranzactie(ri, "1", "1", "1", "1", "intrare")
    adauga_tranzactie(ri, "2", "2", "2", "2", "intrare")
    adauga_tranzactie(ri, "3", "3", "3", "3", "iesire")
    record_mod(ri, "sterge_tip", "intrare")
    assert get_record(ri)==get_record(record_info)
    assert get_istoric(ri)==get_istoric(record_info)
    undo(record_info)
    ri=initializare_record_info()
    adauga_tranzactie(ri, "1", "1", "1", "1", "intrare")
    adauga_tranzactie(ri, "2", "2", "2", "2", "intrare")
    adauga_tranzactie(ri, "3", "3", "3", "3", "iesire")
    assert get_record(ri)==get_record(record_info)
    assert get_istoric(ri)==get_istoric(record_info)
    adauga_tranzactie(record_info,"4","4","4","4","intrare")
    undo(record_info)
    assert get_record(ri)==get_record(record_info)
    assert get_istoric(ri)==get_istoric(record_info)
    undo(record_info)
    ri=initializare_record_info()
    adauga_tranzactie(ri, "1", "1", "1", "1", "intrare")
    adauga_tranzactie(ri, "2", "2", "2", "2", "intrare")
    assert get_record(ri)==get_record(record_info)
    assert get_istoric(ri)==get_istoric(record_info)
    undo(record_info)
    undo(record_info)
    ri=initializare_record_info()
    assert get_record(ri)==get_record(record_info)
    assert get_istoric(ri)==get_istoric(record_info)
    try:
        undo(record_info)
        assert False
    except Exception as eroare:
        assert str(eroare)=="Eroare:Nu exista un stadiu precedent al informatiilor recordului;"

def run_all_tests():
    test_adauga_tranzactie()
    test_actualizare_tranzactie()
    test_record_mod()
    test_cautare_subrecord()
    test_rapoarte_record()
    test_undo()

run_all_tests()