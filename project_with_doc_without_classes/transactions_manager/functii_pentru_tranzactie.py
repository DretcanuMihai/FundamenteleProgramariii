# acest modul se ocupa cu functiile ce manipuleaza, valideaza si opereaza cu informatiile de tip "tranzactie" formate
# din tid - numar natural , data - data de tip data, suma - numar real pozitiv cu exact doua cifre dupa virgula,
# tip - string ce este fie "intrare", fie "iesire"
# tid-ul nu va putea fi setat in mod diret de utilizator, ci va fi egal cu n+1, unde n este numarul de tranzactii
# adaugate precedent
from functii_pentru_data import creeaza_data, validare_data, data_to_string, creeaza_valideaza_data

def creeaza_tranzactie(tid, data, suma, tip):
    """
    functie ce creaza o tranzactie cu tid-ul tid, data data, suma suma si tipul tip
    #date de intrare:->tid - integer
                     ->data - data (calendaristica)
                     ->suma - float
                     ->tip - string
    ##date de iesire:->tranzactie - o tranzactie descrisa de tid, data, suma si tip
    """
    tranzactie=[]
    tranzactie.append(tid)
    tranzactie.append(data)
    tranzactie.append(suma)
    tranzactie.append(tip)
    return tranzactie


def get_tid(tranzactie):
    """
    functie ce da tid-ul ce descrie o tranzactie
    #date de intrare:->tranzactie - o tranzactie
    ##date de iesire:->tid - tid-ul ce descrie tranzactie, un integer
    """
    return tranzactie[0]

def set_tid(tranzactie, tid):
    """
    functie ca schimba tid-ul unei tranzactii cu unul nou
    #date de intrare:->tranzactie - tranzactia careia dorim sa-i schimbam tidul
                     ->tid - tid-ul nou al tranzactiei
    ##date de iesire:-> -
    programul nu returneaza nimic, modificand direct tranzactia
    """
    tranzactie[0]=tid

def get_data(tranzactie):
    """
    functie ce da data ce descrie o tranzactie
    #date de intrare:->tranzactie - o tranzactie
    ##date de iesire:->data - data ce descrie tranzactia, o data
    """
    return tranzactie[1]


def get_suma(tranzactie):
    """
    functie ce da suma ce descrie o tranzactie
    #date de intrare:->tranzactie - o tranzactie
    ##date de iesire:->suma - suma ce descrie tranzactia, un numar rational
    """
    return tranzactie[2]


def get_tip(tranzactie):
    """
    functie ce da tipul ce descrie o tranzactie
    #date de intrare:->tranzactie - o tranzactie
    ##date de iesire:->tip - tipul ce descrie tranzactia, un string
    """
    return tranzactie[3]


def test_baze_tranzactie():
    data=creeaza_data(1, 1, 2001)
    tranzactie = creeaza_tranzactie(1, data, 200.01, "intrare")
    assert get_tid(tranzactie) == 1
    assert get_data(tranzactie) == data
    assert get_suma(tranzactie) == 200.01
    assert get_tip(tranzactie) == "intrare"
    data=creeaza_data(5, 7, 2011)
    tranzactie=creeaza_tranzactie(2, data, 0.79, "iesire")
    assert get_tid(tranzactie)==2
    assert get_data(tranzactie)==data
    assert get_suma(tranzactie)==0.79
    assert get_tip(tranzactie)=="iesire"
    set_tid(tranzactie, 1)
    assert get_tid(tranzactie)==1
    set_tid(tranzactie, 7)
    assert get_tid(tranzactie)==7
    set_tid(tranzactie, 0)
    assert get_tid(tranzactie)==0
    set_tid(tranzactie, 255)
    assert get_tid(tranzactie)==255

def validare_suma(suma):
    """
    functia valideaza o suma daca aceasta este un numar rational strict pozitiv cu exact doua cifre dupa virgula
    #date de intrare:->suma - suma de verificat, nr. rational pozitiv
    ##date de iesire:-> -
    Daca suma este invalida, programul va ridica o exceptie cu mesajul "Eroare:suma trebuie sa aiba maxim doua cifre
    nenule fix dupa virgula;\n"
    """
    if(suma<0.0001):
        raise Exception("Eroare:suma trebuie sa fie un numar rational pozitiv cu maxim doua cifre nenule fix dupa virgula;\n")
    suma=str(suma)
    if(suma[len(suma)-3]!="." and suma[len(suma)-2]!="."):
        raise Exception("Eroare:suma trebuie sa fie un numar rational pozitiv cu maxim doua cifre nenule fix dupa virgula;\n")

def test_validare_suma():
    test=validare_suma
    try:
        test(-100.00)
        assert False
    except Exception as exceptie:
        assert str(exceptie)=="Eroare:suma trebuie sa fie un numar rational pozitiv cu maxim doua cifre nenule fix dupa virgula;\n"
    try:
        test(10.001)
        assert False
    except Exception as exceptie:
        assert str(exceptie)=="Eroare:suma trebuie sa fie un numar rational pozitiv cu maxim doua cifre nenule fix dupa virgula;\n"
    test(.01)
    test(10.99)
    test(11.00)

def validare_tip(tip):
    """
    functia valideaza un tip daca acesta este un string egal cu "intrare" sau "iesire"
    #date de intrare:->tip - tipul, un string
    ##date de iesire:-> -
    Daca tipul introdus este invalid, atunci va fi ridicata o exceptie cu mesajul "Eroare:tipul trebuie sa fie un
     string egal cu 'intrare' sau cu 'iesire';\n"
    """
    if(tip!="intrare" and tip!="iesire"):
        raise Exception("Eroare:tipul trebuie sa fie un string egal cu 'intrare' sau cu 'iesire';\n")

def test_validare_tip():
    test=validare_tip
    try:
        test("intrar")
        assert False
    except Exception as exceptie:
        assert str(exceptie)=="Eroare:tipul trebuie sa fie un string egal cu 'intrare' sau cu 'iesire';\n"
    try:
        test("")
        assert False
    except Exception as exceptie:
        assert str(exceptie)=="Eroare:tipul trebuie sa fie un string egal cu 'intrare' sau cu 'iesire';\n"
    test("intrare")
    test("iesire")

def validare_tranzactie(tranzactie):
    """
    functie ce valideaza o tranzactie daca data acesteia reprezinta o data calendaristica corecta, suma este un numar
    rational strict pozitiv cu 2 cifre dupa virgula, iar tipul este un string egal cu "intrare" sau "iesire"
    #date de intrare:->tranzactie - o tranzactie ce va fi validata
    ##date de iesire:-> -
    Daca tranzactie este valida, programul nu va returna nimic; In caz contrar, vor fi ridicate erorile cu mesaj:
    ->"Eroare:data trebuie sa corespunda unei actuale date calendaristice;\n" daca data este invalida
    ->"Eroare:suma trebuie sa fie un numar rational pozitiv cu maxim doua cifre nenule fix dupa virgula;\n" daca suma este invalida
    ->"Eroare:tipul trebuie sa fie un string egal cu 'intrare' sau cu 'iesire';\n" daca tipul sumei este invalid
    """
    erori=""
    data=get_data(tranzactie)
    suma=get_suma(tranzactie)
    tip=get_tip(tranzactie)
    try:
        validare_data(data)
    except Exception as exceptie:
        erori=erori+str(exceptie)
    try:
        validare_suma(suma)
    except Exception as exceptie:
        erori=erori+str(exceptie)
    try:
        validare_tip(tip)
    except Exception as exceptie:
        erori=erori+str(exceptie)
    if(len(erori)!=0):
        raise Exception(erori)

def test_validare_tranzactie():
    test=validare_tranzactie
    data=creeaza_data(1, 1, 2020)
    tranzactie=creeaza_tranzactie(1, data, 100.01, "intrare")
    test(tranzactie)
    tranzactie=creeaza_tranzactie(2, data, .01, "intrar")
    try:
        test(tranzactie)
        assert False
    except Exception as exceptie:
        assert str(exceptie)=="Eroare:tipul trebuie sa fie un string egal cu 'intrare' sau cu 'iesire';\n"
    tranzactie=creeaza_tranzactie(3, data, 100.001, "iesire")
    try:
        test(tranzactie)
        assert False
    except Exception as exceptie:
        assert str(exceptie)=="Eroare:suma trebuie sa fie un numar rational pozitiv cu maxim doua cifre nenule fix dupa virgula;\n"
    tranzactie=creeaza_tranzactie(4, data, 0.000000000001, "iesir")
    try:
        test(tranzactie)
        assert False
    except Exception as exceptie:
        mesaj=""
        mesaj=mesaj+"Eroare:suma trebuie sa fie un numar rational pozitiv cu maxim doua cifre nenule fix dupa virgula;\n"
        mesaj=mesaj+"Eroare:tipul trebuie sa fie un string egal cu 'intrare' sau cu 'iesire';\n"
        assert str(exceptie)==mesaj
    data=creeaza_data(29, 2, 2019)
    tranzactie=creeaza_tranzactie(5, data, 100.00, "iesire")
    try:
        test(tranzactie)
        assert False
    except Exception as exceptie:
        assert str(exceptie)=="Eroare:data trebuie sa corespunda unei actuale date calendaristice;\n"
    tranzactie=creeaza_tranzactie(6, data, -143.00, "ffd")
    try:
        test(tranzactie)
        assert False
    except Exception as exceptie:
        mesaj=""
        mesaj=mesaj+"Eroare:data trebuie sa corespunda unei actuale date calendaristice;\n"
        mesaj=mesaj+"Eroare:suma trebuie sa fie un numar rational pozitiv cu maxim doua cifre nenule fix dupa virgula;\n"
        mesaj=mesaj+"Eroare:tipul trebuie sa fie un string egal cu 'intrare' sau cu 'iesire';\n"
        assert str(exceptie)==mesaj

def tranzactie_to_string(tranzactie):
    """
    functie ce returneaza un string ce corespunde unei tranzactii astfel:
    #date de intrare:->tranzactie - tranzactia ce va fi convertita
    ##date de iesire:->mesaj - stringul ce corespunde tranzactiei
    mesajul de tip string va fi format astfel:
    T|tid|: |data| suma:|suma| tip:|tip|, unde |data| reprezinta scrierea datei ca |zi|/|luna|/|an|, zilei si lunii
    fiindu-le adaugate cate un 0 la stanga daca sunt reprezentate pe o singura cifra
    """
    tid=get_tid(tranzactie)
    tid=str(tid)
    data=get_data(tranzactie)
    data=data_to_string(data)
    suma=get_suma(tranzactie)
    suma=str(suma)
    if(suma[-2]=="."):
        suma=suma+"0"
    tip=get_tip(tranzactie)
    mesaj="T"+tid+": "+data+" "+suma+"RON "+tip
    return mesaj

def test_tranzactie_to_string():
    test=tranzactie_to_string
    data=creeaza_data(1, 2, 2012)
    tranzactie=creeaza_tranzactie(1, data, 12.1, "intrare")
    assert test(tranzactie)=="T1: 01/02/2012 12.10RON intrare"
    data=creeaza_data(29, 2, 2020)
    tranzactie=creeaza_tranzactie(55, data, .01, "iesire")
    assert test(tranzactie)=="T55: 29/02/2020 0.01RON iesire"
    data=creeaza_data(1, 1,  500)
    tranzactie=creeaza_tranzactie(24, data, 100.00, "iesire")
    assert test(tranzactie)=="T24: 01/01/500 100.00RON iesire"

def suma_to_string(suma):
    """
    functie ce transforma o suma intr-un string caracteristic
    #date de intrare:->suma - suma ce va fi transformata
    ##date de iesire:->mesaj - stringul caracteristic
    """
    mesaj=str(suma)+"00"
    k=2
    while(mesaj[k-2]!="."):
        k=k+1
    mesaj=mesaj[:k+1]
    mesaj=mesaj+" RON"
    return mesaj

def test_suma_to_string():
    test=suma_to_string
    assert test(5.0)=="5.00 RON"
    assert test(-2.0)=="-2.00 RON"
    assert test(245.0)=="245.00 RON"
    assert test(.01)=="0.01 RON"
    assert test(1.99999)=="1.99 RON"
    assert test(2.432321)=="2.43 RON"

def creeaza_valideaza_suma(suma):
    """
    functie ce creeaza si valideaza o suma
    #date de intrare:->suma - un string ce reprezinta suma
    ##date de iesire:->suma - un nr. rational pozitiv, reprezentand suma, daca aceasta este valida
    Daca nu este valida, se vor ridica erorile respective
    """
    try:
        suma=float(suma)
        if(suma<0):
            raise Exception("Eroare:suma trebuie sa fie de tip nr. rational pozitiv;\n")
    except:
        raise Exception("Eroare:suma trebuie sa fie de tip nr. rational pozitiv;\n")
    try:
        validare_suma(suma)
        return suma
    except Exception as er:
        raise Exception(er)

def test_creeaza_valideaza_suma():
    test=creeaza_valideaza_suma
    suma=test("123")
    assert suma==123
    suma=test("1")
    assert suma==1
    suma=test("0.01")
    assert suma==0.01
    try:
        suma=test("asd")
        assert False
    except Exception as eroare:
        assert str(eroare)=="Eroare:suma trebuie sa fie de tip nr. rational pozitiv;\n"
    try:
        suma=test("-1")
        assert False
    except Exception as eroare:
        assert str(eroare)=="Eroare:suma trebuie sa fie de tip nr. rational pozitiv;\n"
    try:
        suma=test("100.999")
    except Exception as eroare:
        assert str(eroare)=="Eroare:suma trebuie sa fie un numar rational pozitiv cu maxim doua cifre nenule fix dupa virgula;\n"

def creeaza_valideaza_tip(tip):
    """
    functie ce creeaza si valideaza un tip
    #date de intrare:->tip - un string ce reprezinta tipul
    ##date de iesire:->tip - stringul ce reprezinta tipul, daca acesta este valid
    Daca nu este valida, se vor ridica erorile respective
    """
    try:
        validare_tip(tip)
        return tip
    except Exception as er:
        raise Exception(er)

def test_creeaza_valideaza_tip():
    test=creeaza_valideaza_tip
    assert test("intrare")=="intrare"
    assert test("iesire")=="iesire"
    try:
        tip=test("asd")
        assert False
    except Exception as eroare:
        assert str(eroare)=="Eroare:tipul trebuie sa fie un string egal cu 'intrare' sau cu 'iesire';\n"
    try:
        tip=test("2121")
        assert False
    except Exception as eroare:
        assert str(eroare)=="Eroare:tipul trebuie sa fie un string egal cu 'intrare' sau cu 'iesire';\n"

def creeaza_valideaza_tranzactie(zi, luna, an, suma, tip):
    """
    functie ce creeaza si valideaza o tranzactie pornind de la zi, luna, an, suma si tip
    #date de intrare:->zi - string reprezentand ziua datei tranzactiei
                     ->luna - string reprezentand luna datei tranzactiei
                     ->an - string reprezentand anul datei tranzactiei
                     ->suma - string reprezentand suma tranzactiei
                     ->tip - string reprezentand tipul tranzatiei
    ##date de iesire:->tranzactie - tranzactia determinata de datele de intrare
    Daca apar erori, acestea vor fi ridicate ca exceptie
    """
    erori=""
    try:
        data=creeaza_valideaza_data(zi, luna, an)
    except Exception as eroare:
        erori=erori+str(eroare)
    try:
        suma=creeaza_valideaza_suma(suma)
    except Exception as eroare:
        erori=erori+str(eroare)
    try:
        tip=creeaza_valideaza_tip(tip)
    except Exception as eroare:
        erori=erori+str(eroare)
    if(len(erori)>0):
        raise Exception(str(erori))
    tranzactie=creeaza_tranzactie(0,data, suma, tip)
    return tranzactie

def test_creeaza_valideaza_tranzactie():
    test=creeaza_valideaza_tranzactie
    d=creeaza_data(12, 7, 1996)
    t=creeaza_tranzactie(0, d, 21.23, "intrare")
    assert t==test("12", "7", "1996", "21.23", "intrare")
    d=creeaza_data(31, 1, 2018)
    t=creeaza_tranzactie(0, d, 99.99, "iesire")
    assert t==test("31", "1", "2018", "99.99", "iesire")
    try:
        t=test("29", "2", "2010", "10.333", "asd")
        assert False
    except Exception as eroare:
        mesaj=""
        mesaj=mesaj+"Eroare:data trebuie sa corespunda unei actuale date calendaristice;\n"
        mesaj=mesaj+"Eroare:suma trebuie sa fie un numar rational pozitiv cu maxim doua cifre nenule fix dupa virgula;\n"
        mesaj=mesaj+"Eroare:tipul trebuie sa fie un string egal cu 'intrare' sau cu 'iesire';\n"
        assert str(eroare)==mesaj
    try:
        t=test("asd","asd","asd","asd","dddddd")
        assert False
    except Exception as eroare:
        mesaj=""
        mesaj=mesaj+"Eroare:ziua, luna si anul datei trebuie sa fie de tip nr. natural nenul;\n"
        mesaj=mesaj+"Eroare:suma trebuie sa fie de tip nr. rational pozitiv;\n"
        mesaj=mesaj+"Eroare:tipul trebuie sa fie un string egal cu 'intrare' sau cu 'iesire';\n"
        assert mesaj==str(eroare)

def creeaza_valideaza_tid(tid):
    """
    functie ce creeaza si valideaza un tid
    #date de intrare:->tid - un string ce reprezinta tidul
    ##date de iesire:->tid - un tid, numar natural nenul, daca acesta este valid
    Daca apar erori, acestea vor fi ridicate iar progrmaul nu va ridica nimic
    """
    try:
        tid=int(tid)
    except:
        raise Exception("Eroare:tid-ul trebuie sa fie de tip nr. natural nenul;\n")
    if(tid<=0):
        raise Exception("Eroare:tid-ul trebuie sa fie de tip nr. natural nenul;\n")
    return tid

def test_creeaza_valideaza_tid():
    test=creeaza_valideaza_tid
    assert test("1")==1
    assert test("123")==123
    assert test("24")==24
    try:
        tid=test("0")
        assert False
    except Exception as eroare:
        assert str(eroare)=="Eroare:tid-ul trebuie sa fie de tip nr. natural nenul;\n"
    try:
        tid=test("-1")
        assert False
    except Exception as eroare:
        assert str(eroare)=="Eroare:tid-ul trebuie sa fie de tip nr. natural nenul;\n"
    try:
        tid=test("0.1")
        assert False
    except Exception as eroare:
        assert str(eroare)=="Eroare:tid-ul trebuie sa fie de tip nr. natural nenul;\n"
    try:
        tid=test("asd")
        assert False
    except Exception as eroare:
        assert str(eroare)=="Eroare:tid-ul trebuie sa fie de tip nr. natural nenul;\n"

def creeaza_valideaza_data_si_suma(zi, luna, an, suma):
    """
    functie ce creeaza si valideaza o lista cu o data si o suma pornind de la informatiile respectivelor
    #date de intrare:->zi - string reprezentand ziua datei
                     ->luna - string reprezentand luna datei
                     ->an - string reprezentand anul datei
                     ->suma - string reprezentand suma
    ##date de iesire:->info - lista cu informatiile respective, pe pozitia 0 fiind data iar pe pozitia 1 suma
    Daca apar erori, acestea vor fi ridicate ca exceptie
    """
    erori=""
    try:
        data=creeaza_valideaza_data(zi, luna, an)
    except Exception as eroare:
        erori=erori+str(eroare)
    try:
        suma=creeaza_valideaza_suma(suma)
    except Exception as eroare:
        erori=erori+str(eroare)
    if(len(erori)>0):
        raise Exception(str(erori))
    return [data, suma]

def test_creeaza_valideaza_data_si_suma():
    test=creeaza_valideaza_data_si_suma
    d=creeaza_data(1, 1, 2001)
    assert test("1", "1", "2001", "200.25")==[d, 200.25]
    d=creeaza_data(29, 2, 2004)
    assert test("29", "2", "2004", "400")==[d, 400.0]
    try:
        i=test("asd","asd","asd","asd")
        assert False
    except Exception as eroare:
        mesaj=""
        mesaj=mesaj+"Eroare:ziua, luna si anul datei trebuie sa fie de tip nr. natural nenul;\n"
        mesaj=mesaj+"Eroare:suma trebuie sa fie de tip nr. rational pozitiv;\n"
        assert str(eroare)==mesaj
    try:
        i=test("29","2","2005", "123.123")
        assert False
    except Exception as eroare:
        mesaj=""
        mesaj=mesaj+"Eroare:data trebuie sa corespunda unei actuale date calendaristice;\n"
        mesaj=mesaj+"Eroare:suma trebuie sa fie un numar rational pozitiv cu maxim doua cifre nenule fix dupa virgula;\n"
        assert str(eroare)==mesaj

def creeaza_valideaza_suma_si_tip(suma, tip):
    """
    functie ce creeaza si valideaza o suma si un tip si le returneaza ca o lista
    #date de intrare:->suma - string reprezentand suma
                     ->tip - string reprezentand tipul
    ##date de iesire:->info - lista ce contine suma pe pozitia 0 si tip pe pozitia 1
    Daca apar erori, acestea vor fi ridicate ca exceptie
    """
    erori=""
    try:
        suma=creeaza_valideaza_suma(suma)
    except Exception as eroare:
        erori=erori+str(eroare)
    try:
        tip=creeaza_valideaza_tip(tip)
    except Exception as eroare:
        erori=erori+str(eroare)
    if(len(erori)>0):
        raise Exception(str(erori))
    return [suma, tip]

def test_creeaza_valideaza_suma_si_tip():
    test=creeaza_valideaza_suma_si_tip
    assert test("123", "intrare")==[123.0, "intrare"]
    assert test("0.05", "iesire")==[0.05, "iesire"]
    assert test("45.5", "iesire")==[45.5, "iesire"]
    try:
        i=test("asd", "asd")
        assert False
    except Exception as eroare:
        mesaj=""
        mesaj=mesaj+"Eroare:suma trebuie sa fie de tip nr. rational pozitiv;\n"
        mesaj=mesaj+"Eroare:tipul trebuie sa fie un string egal cu 'intrare' sau cu 'iesire';\n"
        assert str(eroare)==mesaj
    try:
        i=test("55.5555", "intrar")
        assert False
    except Exception as eroare:
        mesaj=""
        mesaj=mesaj+"Eroare:suma trebuie sa fie un numar rational pozitiv cu maxim doua cifre nenule fix dupa virgula;\n"
        mesaj=mesaj+"Eroare:tipul trebuie sa fie un string egal cu 'intrare' sau cu 'iesire';\n"
        assert str(eroare)==mesaj

def run_all_tests():
    test_baze_tranzactie()
    test_validare_suma()
    test_validare_tip()
    test_validare_tranzactie()
    test_tranzactie_to_string()
    test_suma_to_string()
    test_creeaza_valideaza_suma()
    test_creeaza_valideaza_tip()
    test_creeaza_valideaza_tranzactie()
    test_creeaza_valideaza_tid()
    test_creeaza_valideaza_data_si_suma()
    test_creeaza_valideaza_suma_si_tip()

run_all_tests()