#acest modul contine functiile necesare prelucrarii unor rapoarte
from functii_pentru_tranzactie import get_suma, creeaza_tranzactie, get_tip, get_tid
from functii_pentru_record_info import get_element_nv, initializare_record, scrie_element_record, sterge_element_record_nv
from functii_pentru_data import creeaza_data
from functii_ajutatoare import copy_dictionar


def suma_total(record):
    """
    functie ce returneaza suma totala a sumelor tranzactiilor unui record
    #date de intrare:->record - recordul cu tranzactii a caror suma este calculata
    ##date de iesire:->suma - suma sumelor tranzactiilor recordului
    """
    suma=0
    for tid in record:
        if(tid!="index"):
            suma=suma+get_suma(get_element_nv(record, tid))
    return suma

def test_suma_total():
    test=suma_total
    record=initializare_record()
    assert test(record)==0
    data=creeaza_data(1,1,1)
    tranzactie=creeaza_tranzactie(1, data, 2, "intrare")
    scrie_element_record(record,tranzactie,1)
    assert test(record)==2
    tranzactie=creeaza_tranzactie(2, data, 55, "intrare")
    scrie_element_record(record, tranzactie,2)
    assert test(record)==57
    tranzactie=creeaza_tranzactie(3, data, 123, "intrare")
    scrie_element_record(record, tranzactie, 3)
    assert test(record)==180

def sold_total(record):
    """
    functie ce calcueaza soldul determinat de o lista de tranzactii
    #date de intrare:->record - recordul cu tranzactii a caror sold se calculeaza
    ##date de iesire:->sold - soldul determinat de tranzactii
    :return:
    """
    sold=0.0
    for tid in record:
        if(tid!="index"):
            tranzactie=get_element_nv(record, tid)
            if(get_tip(tranzactie)=="intrare"):
                sold=sold+get_suma(tranzactie)
            else:
                sold=sold-get_suma(tranzactie)
    return sold

def test_sold_total():
    test=sold_total
    record=initializare_record()
    assert test(record)==0
    data=creeaza_data(1, 1, 1)
    tranzactie=creeaza_tranzactie(1, data, 5, "intrare")
    scrie_element_record(record, tranzactie,1)
    assert test(record)==5
    tranzactie=creeaza_tranzactie(2, data, 5, "iesire")
    scrie_element_record(record, tranzactie,2)
    assert test(record)==0
    tranzactie=creeaza_tranzactie(3, data, 25.01, "iesire")
    scrie_element_record(record, tranzactie, 3)
    assert test(record)==-25.01
    tranzactie=creeaza_tranzactie(4, data, 100.00, "intrare")
    scrie_element_record(record, tranzactie, 4)
    assert test(record)==74.99

def min_record(record):
    """
    functie ce returneaza prima tranzactie cu valoarea minima din record
    #date de intrare:->record - recordul nenul de tranzactii de unde luam elementul
    ##date de iesire:->minx - valoarea minima din record
    """
    suma_min=0
    for tid in record:
        if(tid!="index"):
            tranzactie=get_element_nv(record, tid)
            suma=get_suma(tranzactie)
            if(suma_min==0):
                suma_min=suma
                t_min=tranzactie
            elif suma<suma_min:
                suma_min=suma
                t_min=tranzactie
    return t_min

def test_min_record():
    test=min_record
    record=initializare_record()
    d=creeaza_data(1, 1, 1)
    t1=creeaza_tranzactie(1, d, 1, "intrare")
    scrie_element_record(record, t1, 1)
    assert test(record) ==t1
    t2=creeaza_tranzactie(1, d, 2, "iesire")
    scrie_element_record(record, t2, 2)
    assert test(record)==t1
    t3=creeaza_tranzactie(3, d, 0.09, "intrare")
    scrie_element_record(record, t3, 3)
    assert test(record)==t3

def ordonare_record(record):
    """
    functie ce ordoneaza un record de tranzactii dupa suma
    #date de intrare:->record - recordul de tranzactii ce va fi ordonat
    ##date de iesire:->lista_ordonata - lista ordonata
    """
    record_copie=copy_dictionar(record)
    lista_ordonata=[]
    for i in range(1, len(record)):
        t=min_record(record_copie)
        tid=get_tid(t)
        sterge_element_record_nv(record_copie, tid)
        lista_ordonata.append(t)
    return lista_ordonata




def test_ordonare_record():
    test=ordonare_record
    record=initializare_record()
    assert test(record)==[]
    d=creeaza_data(1, 1, 1)
    t1=creeaza_tranzactie(1, d, 1, "intrare")
    t2=creeaza_tranzactie(2, d, 3, "iesire")
    t3=creeaza_tranzactie(3, d, 123, "intrare")
    scrie_element_record(record, t1, 1)
    assert test(record)==[t1]
    scrie_element_record(record, t2, 2)
    scrie_element_record(record, t3, 3)
    assert test(record)==[t1,t2,t3]
    t4=creeaza_tranzactie(4, d, 122, "intrare")
    scrie_element_record(record, t4, 4)
    assert test(record)==[t1,t2,t4,t3]
    t5=creeaza_tranzactie(5, d, 123, "intrare")
    scrie_element_record(record, t5, 5)
    assert test(record)==[t1,t2,t4,t3,t5]

def run_all_tests():
    test_suma_total()
    test_sold_total()
    test_min_record()
    test_ordonare_record()

run_all_tests()