#acest modul se ocupa cu functiile ce manipuleaza si opereaza informatiile dintr-un record_info, structura ce contine
#un record actual in "record", dictionar ce contine date de acelasi tip identificabile prin id-ul tid si un istoric al
#recordurilor, "istoric", ce contine toate iteratiile precedente ale recordului
#functiile cu "_ri" lucreaza cu informatiile recordurilor
#toate functiile "_ri" ce vor modifica un record vor updata concomitent istoricul cu recordul respectiv inainte de a fi
#modificat
#tid-ul (identificatorul) poate fi de orice tip atat timp cat poate fi indice in dictionar (sper ca asta-i termenul)
#in contextul problemei mele, acesta va fi numar natural nenul
#!!!Functille ce au "nv" la sfarsit se folosesc fara a verifica daca tid-ul respectiv este valid situatiei in care
#!!!se foloseste
#!!!Functiile ce au "ri" la sfarsit opereaza pe informatiile recordurilor si vor updata istoricul inainte de a face
#!!!modificare propusa (mereu)
from functii_ajutatoare import copy_dictionar, apartine_interval,  incep_cu_acelasi_char, aceeiasi_paritate

def validare_tid_in_record(record, tid):
    """
    functie ce valideaza daca exista un element cu tid-ul tid in recordul record
    #date de intrare:->record - recordul in care se verifica existenta unui element cu tidul tid
                     ->tid - identificator numar natural nenul pentru care se verifica daca exista vreun element ce ii
                       este asociat
    ##date de iesire:-> -
    daca nu exista un element cu tid-ul tid in record va fi ridicata o exceptie cu mesajul "Eroare:nu exista
    element cu tid-ul specificat in lista;\n"
    functia nu returneaza nimic
    """
    if(tid not in record ):
        raise Exception("Eroare:nu exista element cu tid-ul specificat in lista;\n")

def test_validare_tid_in_record():
    test=validare_tid_in_record
    record={1:23, 4:22}
    test(record, 1)
    try:
        test(record, 2)
        assert(False)
    except Exception as exceptie:
        assert str(exceptie)=="Eroare:nu exista element cu tid-ul specificat in lista;\n"
    record={}
    try:
        test(record, 1)
        assert False
    except Exception as exceptie:
        assert str(exceptie)=="Eroare:nu exista element cu tid-ul specificat in lista;\n"

def initializare_record():
    """
    functie ce intializeaza un record gol
    #date de intrare:-> -
    ##date de iesire:->record - un record gol
    """
    record={"index":0}
    return record

def scrie_element_record(record, element, tid):
    """
    functie ce scrie un element intr-un record la tid-ul indicat
    #date de intrare:->record - recordul la care se adauga elementul
                     ->element - un element ,de tipul celor ce construiesc lista, ce este adaugat in record
                     ->tid - un identificator unic, numar natural nenul
    ##date de iesire:-> -
    Programul va modifica recordul si va scrie la tid-ul indicat elementul cerut
    """
    record[tid]=element

def get_element_nv(record, tid):
    """
    funcie ce ia din record elementul ce are identificator tidul din argument
    #date de intrare:->record - recordul din care scoatem elementul
                     ->tid - tid, un identificator numar natural nenul
    ##date de iesire:->element - elementul din recordul cu identificatorul tid
    """
    return record[tid]

def get_index(record):
    """
    functie ce ia din record indexul de generare
    #date de intrare:->record - recordul din care scoatem indexul
    ##date de iesire:->index  - indexul de generare
    """
    return record["index"]

def set_index(record, index):
    """
    functie ce seteaza indexul din record la o noua valoare
    #date de intrare:->record - recordul unde updatam indexul
                     ->index - indexul de generare nou
    ##date de iesire:-> -
    :param record:
    :param index:
    :return:
    """
    record["index"]=index

def test_baze_record_and_scrie_element():
    record=initializare_record()
    scrie_element_record(record, 2, 1)
    assert record=={"index":0,1:2}
    assert get_index(record)==0
    scrie_element_record(record, 255, 100)
    assert record=={"index":0,1:2, 100:255}
    assert get_element_nv(record, 1)==2
    assert get_element_nv(record, 100)==255
    assert get_index(record)==0
    set_index(record, 2)
    assert get_index(record)==2
    set_index(record, 5)
    assert get_index(record)==5

def initializare_record_info():
    """
    functia initializeaza un record_info gol si il returneaza
    #date de intrare:-> -
    ##date de iesire:->record_info - un record_info gol, caracterizat de record si istoric
    """
    record_info={}
    record=initializare_record()
    istoric=[]
    record_info["record"]=record
    record_info["istoric"]=istoric
    return record_info

def get_record(record_info):
    """
    functie ce ia recordul actual din informatiile recordurilor
    #date de intrare:->record_info - record_info-ul ce contine informatiile recordului de unde se ia recordul actual
    ##date de iesire:->record - recordul actual din record info
    """
    return record_info["record"]

def set_record(record_info, record):
    """
    functia seteaza recordul actual din informatiile recordurilor la recordul record
    #date de intrare:->record_info - informatiile recordurilor ce le modificam
                     ->record - recordul cu care suprascriem recordul actual din record_info
    ##date de iesire:-> -
    programul modifica direct
    """
    record_info["record"]=record

def get_istoric(record_info):
    """
    functie ce ia istoricul din informatiile recordurilor
    #date de intrare:->record_info - record_info-ul ce contine informatiile recordului de unde se ia istoricul
    ##date de iesire:->istoric
    """
    return record_info["istoric"]

def update_istoric(istoric, record):
    """
    functie ce updateaza istoricul,adaugand elementul record in varful istoricului
    #date de intrare:->istoric - istoricul ce se updateaza
                     ->record - recordul ce se adauga in varful istoricului
    ##date de iesire:-> -
    functia modifica in mod direct istoricul ce-l updateaza
    """
    record_copy=copy_dictionar(record)
    istoric.append(record_copy)

def test_update_istoric():
    istoric=[]
    record=initializare_record()
    update_istoric(istoric, record)
    assert istoric==[record]
    record1=initializare_record()
    scrie_element_record(record1, 2, 1)
    scrie_element_record(record1, 6, 2)
    update_istoric(istoric, record1)
    assert istoric==[record, record1]
    record2=initializare_record()
    scrie_element_record(record2, 55, 1)
    update_istoric(istoric, record2)
    assert istoric==[record,record1, record2]

def adauga_element_record_ri_nv(record_info, element):
    """
    functie ce modifica informatiile recordurilor, adaugand un element recordului actual
    #date de intrare:->record - recordul la care se adauga elementul
                     ->element - un element ,de tipul celor ce construiesc lista, ce este adaugat in record
    ##date de iesire:-> -
    Programul va modififica recordul actual din informatiile recordurilor si va adauga la tid-ul indicat elementul
    cerut, updatind si istoricul
    """
    record=get_record(record_info)
    istoric=get_istoric(record_info)
    update_istoric(istoric, record)
    index=get_index(record)
    index=index+1
    set_index(record, index)
    scrie_element_record(record, element, index)

def test_baze_record_info_and_adauga_element():
    record_info=initializare_record_info()
    record=initializare_record()
    assert get_record(record_info)==record
    assert get_istoric(record_info)==[]
    assert get_index(get_record(record_info))==0
    adauga_element_record_ri_nv(record_info, 123)
    record1=initializare_record()
    scrie_element_record(record1, 123, 1)
    set_index(record1, 1)
    assert get_record(record_info)==record1
    assert get_istoric(record_info)==[record]
    assert get_index(get_record(record_info))==1
    adauga_element_record_ri_nv(record_info, 245)
    record2=initializare_record()
    scrie_element_record(record2, 123, 1)
    scrie_element_record(record2, 245, 2)
    set_index(record2, 2)
    assert get_record(record_info)==record2
    assert get_istoric(record_info)==[record,record1]
    assert get_index(get_record(record_info))==2
    set_record(record_info, record)
    assert get_record(record_info)==record
    set_record(record_info, record1)
    assert get_record(record_info)==record1

def actualizare_element_record_ri(record_info, element, tid):
    """
    functie ce actualizeaza valoarea unui element din record cu identificatorul tid cu un element nou
    #date de intrare:->record - recordul ce va fi modificat
                     ->element - noua valoare a elementului ce va fi modificat
                     ->tid - identificatorul nr. natural nenul
    daca nu exista un elementul cu tid-ul tid in record, functia va ridica o exceptie cu mesajul "Eroare:nu exista
    element cu tid-ul specificat in lista;\n"
    functia nu returneaza nimic, modificarile avand loc direct in recordul record;
    """
    record=get_record(record_info)
    istoric=get_istoric(record_info)
    validare_tid_in_record(record, tid)
    update_istoric(istoric, record)
    scrie_element_record(record, element, tid)

def test_actualizare_element_record_ri():
    record_info=initializare_record_info()
    test=actualizare_element_record_ri
    record=initializare_record()
    try:
        test(record_info, 2, 1)
        assert False
    except Exception as exceptie:
        assert str(exceptie)=="Eroare:nu exista element cu tid-ul specificat in lista;\n"
        assert get_record(record_info)==record
        assert get_istoric(record_info)==[]
    adauga_element_record_ri_nv(record_info, 22)
    test(record_info, 33, 1)
    record1=initializare_record()
    scrie_element_record(record1, 22, 1)
    set_index(record1, 1)
    record2=initializare_record()
    scrie_element_record(record2, 33, 1)
    set_index(record2, 1)
    assert get_record(record_info)==record2
    assert get_istoric(record_info)==[record, record1]
    adauga_element_record_ri_nv(record_info, 99)
    record3=initializare_record()
    scrie_element_record(record3, 33, 1)
    scrie_element_record(record3, 99, 2)
    set_index(record3, 2)
    test(record_info, 1231, 2)
    record4=initializare_record()
    scrie_element_record(record4, 33, 1)
    scrie_element_record(record4, 1231, 2)
    set_index(record4, 2)
    assert get_record(record_info)==record4
    assert get_istoric(record_info)==[record, record1,record2,record3]
    try:
        test(record_info, 5, 5)
        assert False
    except Exception as exceptie:
        assert str(exceptie)=="Eroare:nu exista element cu tid-ul specificat in lista;\n"
        assert get_record(record_info)==record4
        assert get_istoric(record_info)==[record,record1,record2,record3]

def sterge_element_record_nv(record, tid):
    """
    functie ce sterge din record elementul cu identificatorul tid
    #date de intrare:->record - recordul ce sufera modificarea
                     ->tid - identificatorul, numar natural, al numarului sters
    ##date de iesire:-> -
    functia nu returneaza nimic, ci va modifica recordul;
    """
    del record[tid]

def test_sterge_element_record_nv():
    test=sterge_element_record_nv
    record=initializare_record()
    scrie_element_record(record, 22, 1)
    scrie_element_record(record,44,2)
    scrie_element_record(record,"ASD", 3)
    scrie_element_record(record, [1, 1], 5)
    record1=initializare_record()
    scrie_element_record(record1,44,2)
    scrie_element_record(record1,"ASD", 3)
    scrie_element_record(record1, [1, 1], 5)
    record2=initializare_record()
    scrie_element_record(record2,44,2)
    scrie_element_record(record2, [1, 1], 5)
    record3=initializare_record()
    scrie_element_record(record3,44,2)
    record4=initializare_record()
    test(record, 1)
    assert record==record1
    test(record, 3)
    assert record==record2
    test(record, 5)
    assert record==record3
    test(record, 2)
    assert record==record4

def subrecord_prop_info(record, prop, info):
    """
    functie ce cauta intr-un record un subrecord cu o proprietate ceruta ce depinde de niste informatii
    #date de intrare:->record - recordul in care cautam subrecordul
                     ->prop - o functie booleana ce verifica proprietatea ceruta, avand ca parametrii un element de
                     acelasi tip ca data din record si un element de acelasi tip ca informatia info
                     ->info - informatia necesara verificarii proprietatii prop
    ##date de iesire:->subrecord - un record format din elementele din record ce respecta proprietatea
    """
    subrecord=initializare_record()
    for el in record:
        element=get_element_nv(record, el)
        if(el!="index"):
            if(prop(element, info)==True):
                scrie_element_record(subrecord, element, el)
    set_index(subrecord, get_index(record))
    return subrecord

def test_subrecord_prop_info():
    test=subrecord_prop_info
    f1=aceeiasi_paritate
    f2=incep_cu_acelasi_char
    f3=apartine_interval
    record=initializare_record()
    scrie_element_record(record, 2, 1)
    scrie_element_record(record, -25, 2)
    scrie_element_record(record, 3, 3)
    record1=initializare_record()
    scrie_element_record(record1, 2, 1)
    record2=initializare_record()
    scrie_element_record(record2,-25, 2)
    scrie_element_record(record2, 3, 3)
    assert test(record, f1, 22)==record1
    assert test(record, f1, 123)==record2
    record=initializare_record()
    scrie_element_record(record, "#aaaf", 1)
    scrie_element_record(record, "hmmm", 2)
    scrie_element_record(record, "##f", 5)
    record1=initializare_record()
    scrie_element_record(record1, "#aaaf", 1)
    scrie_element_record(record1, "##f", 5)
    record2=initializare_record()
    scrie_element_record(record2, "hmmm", 2)
    record3=initializare_record()
    assert test(record, f2, "#ss")==record1
    assert test(record, f2, "haz")==record2
    assert test(record, f2, "nu")==record3
    record=initializare_record()
    scrie_element_record(record, 12, 1)
    scrie_element_record(record, -12, 2)
    scrie_element_record(record, 0, 3)
    record1=initializare_record()
    record2=initializare_record()
    scrie_element_record(record2, 12, 1)
    assert test(record, f3, {"st":-12, "dr":12})==record
    assert test(record, f3, {"st":100, "dr":200})==record1
    assert test(record, f3, {"st":10, "dr":120})==record2

def run_all_tests():
    test_validare_tid_in_record()
    test_baze_record_and_scrie_element()
    test_update_istoric()
    test_baze_record_info_and_adauga_element()
    test_actualizare_element_record_ri()
    test_sterge_element_record_nv()
    test_subrecord_prop_info()

run_all_tests()