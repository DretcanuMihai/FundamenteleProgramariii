# acest modul se ocupa cu functiile ce manipuleaza,valideaza si opereaza cu informatiile de tip "data", formate
# din zi, luna, an - numere intregi

def creeaza_data(zi, luna, an):
    """
    #functie ce construieste o data pornind de la o zi, o luna si un an, toate numere intregi
    #date de intrare: ->zi - numar intreg
                      ->luna - numar intreg
                      ->an - numar intreg
    ##date de iesire: ->data - o data cu ziua zi, luna luna si anul an
    """
    data=[]
    data.append(zi)
    data.append(luna)
    data.append(an)
    return data

def get_zi(data):
    """
    functie ce da ziua ce descrie o data
    #date de intrare:->data - o data
    ##date de iesire:->zi - ziua, numar intreg, ce descrie data
    """
    return data[0]

def get_luna(data):
    """
    functie ce da luna ce descrie o data
    #date de intrare:->data - o data
    ##date de iesire:->luna - luna, numar intreg, ce descrie data
    """
    return data[1]

def get_an(data):
    """
    functie ce da anul ce descrie o data
    #date de intrare:->data - o data
    ##date de iesire:->an - anul, numar intreg, ce descrie data
    """
    return data[2]

def test_baze_data():
    """
    teste pentru functia de creare, setteri si getteri
    """
    data = creeaza_data(11, 1, 2010)
    assert get_zi(data) == 11
    assert get_luna(data) == 1
    assert get_an(data) == 2010
    data = creeaza_data(31, 3, 1997)
    assert get_zi(data) == 31
    assert get_luna(data) == 3
    assert get_an(data) == 1997

def an_bisect(an):
    """
    programul veirfica daca un nr. intreg pozitiv an corepsunde unui an bisect sau nu
    #date de intrare:->an - nr intreg, mai mare ca 0
    ##date de iesire:->True - daca nr. an corespunde unui an bisect
                     ->False - in caz contrar
    """
    if an % 4 != 0:
        return False
    if an % 100 != 0:
        return True
    if an % 400 != 0:
        return False
    return True

def test_an_bisect():
    assert an_bisect(2001) == False
    assert an_bisect(2004) == True
    assert an_bisect(1900) == False
    assert an_bisect(2000) == True
    assert an_bisect(2005) == False

def initializare_calendar(an):
    """
    programul returneaza un dictionar care asociaza fiecarei luni din an numarul
    sau de zile (lunile sunt reprezentate ca nr. intregi de la 1 la 12)
    #date de intrare:->an - numar intreg, mai mare ca 0
    ##date de iesire:->calendar - dictionar ce corespunde anului an
    """
    calendar = {}
    calendar[1] = 31
    calendar[2] = 28
    calendar[3] = 31
    calendar[4] = 30
    calendar[5] = 31
    calendar[6] = 30
    calendar[7] = 31
    calendar[8] = 31
    calendar[9] = 30
    calendar[10] = 31
    calendar[11] = 30
    calendar[12] = 31
    if (an_bisect(an)):
        calendar[2] = 29
    return calendar

def test_initializare_calendar():
    test=initializare_calendar
    calendar={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    assert test(2009)==calendar
    calendar[2]=29
    assert test(2020)==calendar

def validare_data(data):
    """
    programul valideaza daca o data reprezinta o actuala data caldendaristica
    #date de intrare:->data - de tip data, reprezinta data ce va fi validata
    ##date de iesire:-> - ,daca data este valida
    Daca data este invalida, va fi ridicat exceptie de tip Exception cu mesajul
    "Eroare:data trebuie sa corespunda unei actuale date calendaristice;\n"
    """
    zi = get_zi(data)
    luna = get_luna(data)
    an = get_an(data)
    if (an < 1) or (luna < 1) or (luna > 12) or (zi < 1) or (zi > 31):
        raise Exception("Eroare:data trebuie sa corespunda unei actuale date calendaristice;\n")
    calendar = initializare_calendar(an)
    if (zi > calendar[luna]):
        raise Exception("Eroare:data trebuie sa corespunda unei actuale date calendaristice;\n")

def test_validare_data():
    data = creeaza_data(1, 2, -2020)
    try:
        validare_data(data)
        assert (False)
    except Exception as exceptie:
        assert str(exceptie) == "Eroare:data trebuie sa corespunda unei actuale date calendaristice;\n"
    data = creeaza_data(29, 2, 2020)
    validare_data(data)
    data = creeaza_data(29, 2, 2021)
    try:
        validare_data(data)
        assert (False)
    except Exception as exceptie:
        assert str(exceptie) == "Eroare:data trebuie sa corespunda unei actuale date calendaristice;\n"
    data = creeaza_data(1, 0, 2000)
    try:
        validare_data(data)
        assert (False)
    except Exception as exceptie:
        assert str(exceptie) == "Eroare:data trebuie sa corespunda unei actuale date calendaristice;\n"
    data = creeaza_data(29, 13, 2020)
    try:
        validare_data(data)
        assert (False)
    except Exception as exceptie:
        assert str(exceptie) == "Eroare:data trebuie sa corespunda unei actuale date calendaristice;\n"
    data = creeaza_data(29, 2, 1900)
    try:
        validare_data(data)
        assert False
    except Exception as exceptie:
        assert str(exceptie) == "Eroare:data trebuie sa corespunda unei actuale date calendaristice;\n"
    data = creeaza_data(29, 2, 1600)
    validare_data(data)
    data = creeaza_data(13, 12, 2012)
    validare_data(data)

def data_to_string(data):
    """
    functie ce returneaza un string ce corespunde unei date, astfel:
    zi/luna/an - unde zi si luna vor avea un 0 in fata daca ele sunt formate dintr-o singura cifra
    #date de intrare:->data - o data calendaristica
    ##date de iesire:->mesaj - stringul ce corespunde datei
    """
    mesaj=""
    zi=get_zi(data)
    luna=get_luna(data)
    an=get_an(data)
    if(zi<10):
        mesaj=mesaj+"0"
    mesaj=mesaj+str(zi)+"/"
    if(luna<10):
        mesaj=mesaj+"0"
    mesaj=mesaj+str(luna)+"/"
    mesaj=mesaj+str(an)
    return mesaj

def test_data_to_string():
    data=creeaza_data(1, 1, 2001)
    assert data_to_string(data)=="01/01/2001"
    data=creeaza_data(12, 12, 2012)
    assert data_to_string(data)=="12/12/2012"
    data=creeaza_data(5, 12, 1995)
    assert data_to_string(data)=="05/12/1995"
    data=creeaza_data(12, 4, 335)
    assert data_to_string(data)=="12/04/335"

def comp_data(data1, data2):
    """
    functie ce returneaza True daca data1>data2 si false in caz contrar
    #date de intrare:->data1 - o data
                     ->data2 - o data
    ##date de iesire:->True - daca data1 este mai tarzie ca data2
                     ->False - in caz contrar
    """
    an1=get_an(data1)
    an2=get_an(data2)
    if(an1!=an2):
        return an1>an2
    luna1=get_luna(data1)
    luna2=get_luna(data2)
    if(luna1!=luna2):
        return luna1>luna2
    zi1=get_zi(data1)
    zi2=get_zi(data2)
    return zi1>zi2

def test_comp_data():
    test=comp_data
    data1=creeaza_data(1, 1, 1)
    data2=creeaza_data(2, 2, 2)
    assert test(data1, data2)==False
    assert test(data2, data1)==True
    data2=creeaza_data(1, 1, 1)
    assert test(data1, data2)==False
    assert test(data2, data1)==False
    data1=creeaza_data(2, 5, 2)
    data2=creeaza_data(2, 2, 2)
    assert test(data1,data2)==True
    assert test(data2, data1)==False
    data1=creeaza_data(1, 2, 2)
    data2=creeaza_data(2, 2, 2)
    assert test(data1, data2)==False
    assert test(data2, data1)==True

def data_in_perioada(data, data1, data2):
    """
    functie ce verifica daca o data se afla intr-o perioada determinata de data1 si data2
    #date de intrare:->data - data ce se verifica daca se afla in perioada de timp
                     ->data1 - data ce reprezinta limita inferioara a intervalului
                     ->data2 - data ce reprezinta limita superioara a intervalului
    ##date de iesire:->True - daca data se afla in interval (incluzand limitele)
                     ->False - in caz contrar
    """
    return ((comp_data(data, data1) or data==data1) and(comp_data(data2, data) or data==data2))

def test_data_in_perioada():
    test=data_in_perioada
    data=creeaza_data(1, 1, 2000)
    data1=creeaza_data(1, 1, 1995)
    data2=creeaza_data(1, 1, 2001)
    assert test(data, data1, data2)==True
    data=data2
    assert test(data, data1, data2)==True
    data=data1
    assert test(data,data1,data2)==True
    data=creeaza_data(1, 1, 1990)
    assert test(data, data1, data2)==False
    data=creeaza_data(1, 1, 2005)
    assert test(data, data1, data2)==False

def validare_perioada(data1, data2):
    """
    functie ce valideaza o perioada de timp daca data1 este precedenta data2
    #date de intrare:->data1 - data ce ar fi limita inferioara
                     ->data2 - data ce ar fi limita superiaora
    ##date de iesire:-> -
    programul nu returneaza nimic, dar daca perioada este invalida, atunci va fi ridicata o exceptie cu mesajul
    "Eroare:perioada de timp invalida;prima data trebuie sa fie precedenta celei de-a doua date si diferita de
    aceasta;\n"
    """
    if(comp_data(data1,data2) or data1==data2):
        raise Exception("Eroare:perioada de timp invalida;prima data trebuie sa fie precedenta celei de-a doua date si diferita de aceasta;\n")

def test_validare_perioada():
    test=validare_perioada
    data1=creeaza_data(1, 1, 1)
    data2=creeaza_data(2, 2, 2)
    test(data1, data2)
    try:
        validare_perioada(data2,data1)
        assert False
    except Exception as eroare:
        assert str(eroare)=="Eroare:perioada de timp invalida;prima data trebuie sa fie precedenta celei de-a doua date si diferita de aceasta;\n"
    data2=creeaza_data(1, 1, 1)
    try:
        validare_perioada(data1, data2)
        assert False
    except Exception as eroare:
        assert str(eroare)=="Eroare:perioada de timp invalida;prima data trebuie sa fie precedenta celei de-a doua date si diferita de aceasta;\n"

def creeaza_valideaza_data(zi, luna, an):
    """
    functie ce creeaza si valideaza o data pornind de la zi, luna, an
    #date de intrare:->zi - string reprezentand ziua
                     ->luna - string reprezentand luna
                     ->an - sgtring reprezentand anul
    ##date de iesire:->data - o structura de data valida
    Daca apar erori, acestea vor fi ridicate ca exceptie
    """
    try:
        zi=int(zi)
        luna=int(luna)
        an=int(an)
        if(zi<=0 or luna<=0 or an <=0):
            raise Exception("Eroare:ziua, luna si anul datei trebuie sa fie de tip nr. natural nenul;\n")
        data=creeaza_data(zi, luna, an)
    except:
        raise Exception("Eroare:ziua, luna si anul datei trebuie sa fie de tip nr. natural nenul;\n")
    try:
        validare_data(data)
        return data
    except Exception as ex:
        raise Exception(str(ex))

def test_creeaza_valideaza_data():
    test=creeaza_valideaza_data
    data=test("12", "12", "2020")
    assert data==creeaza_data(12, 12, 2020)
    data=test("1", "1", "1")
    assert data==creeaza_data(1, 1, 1)
    try:
        data=creeaza_valideaza_data("asd", "1", "12")
        assert False
    except Exception as eroare:
        assert str(eroare)=="Eroare:ziua, luna si anul datei trebuie sa fie de tip nr. natural nenul;\n"
    try:
        data=creeaza_valideaza_data("-1", "1", "1")
        assert False
    except Exception as eroare:
        assert str(eroare) == "Eroare:ziua, luna si anul datei trebuie sa fie de tip nr. natural nenul;\n"
    try:
        data=creeaza_valideaza_data("29", "2", "2005")
        assert False
    except Exception as eroare:
        assert str(eroare)=="Eroare:data trebuie sa corespunda unei actuale date calendaristice;\n"

def creeaza_valideaza_perioada(zi1, luna1, an1, zi2, luna2, an2):
    eroare1=""
    eroare2=""
    try:
        data1=creeaza_valideaza_data(zi1, luna1, an1)
    except Exception as eroare:
        eroare1=str(eroare)
    try:
        data2=creeaza_valideaza_data(zi2, luna2, an2)
    except Exception as eroare:
        eroare2=str(eroare)
    if (eroare1 != eroare2):
        eroare1 = eroare1 + eroare2
    if (len(eroare1) != 0):
        raise Exception(str(eroare1))
    try:
        validare_perioada(data1, data2)
        return [data1,data2]
    except Exception as eroare:
        raise Exception(eroare)

def test_creeaza_valideaza_perioada():
    test=creeaza_valideaza_perioada
    d1=creeaza_data(1, 1, 1)
    d2=creeaza_data(2, 2, 2)
    assert test("1", "1", "1", "2", "2", "2")==[d1, d2]
    d2=creeaza_data(12, 12, 2012)
    assert test("1", "1", "1", "12", "12", "2012")==[d1, d2]
    try:
        i=test("1", "1", "1", "1", "1", "1")
        assert False
    except Exception as eroare:
        assert str(eroare)=="Eroare:perioada de timp invalida;prima data trebuie sa fie precedenta celei de-a doua date si diferita de aceasta;\n"
    try:
        i=test("2", "2", "2", "1", "1", "1")
        assert False
    except Exception as eroare:
        assert str(eroare)=="Eroare:perioada de timp invalida;prima data trebuie sa fie precedenta celei de-a doua date si diferita de aceasta;\n"
    try:
        i=test("asd","asd","asd","29","2","2021")
        assert False
    except Exception as eroare:
        mesaj=""
        mesaj=mesaj+"Eroare:ziua, luna si anul datei trebuie sa fie de tip nr. natural nenul;\n"
        mesaj=mesaj+"Eroare:data trebuie sa corespunda unei actuale date calendaristice;\n"
        assert mesaj==str(eroare)

def run_all_tests():
    test_baze_data()
    test_an_bisect()
    test_initializare_calendar()
    test_validare_data()
    test_data_to_string()
    test_comp_data()
    test_data_in_perioada()
    test_validare_perioada()
    test_creeaza_valideaza_data()
    test_creeaza_valideaza_perioada()


run_all_tests()