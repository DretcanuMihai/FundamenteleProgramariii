#acest modul contine functii ce afiseaza mesaje

def print_bootup():
    print("Aplicatie pornita;")
    print("Introduceti 'meniu' pentru a vedea lista comenzilor posibile;")

def print_meniu():
    print("Lista comenzilor:")
    print("#########0.'meniu' - afiseaza lista comenzilor")
    print("#########1.'adauga' - tranzactie in record")
    print("2.'actualizare' - tranzactie din record")
    print("#########3.'sterge_zi' - sterge tranzactiile unei zile")
    print("4.'sterge_perioada' - sterge tranzactiile unei perioade")
    print("5.'sterge_tip' - sterge tranzactiile de un tip")
    print("6.'cautare_supsum' - tipareste tranzactiile cu suma mai mare ca cea introdusa")
    print("7.'cautare_supsum_prezi' - tipareste tranzactiile precedente unei zile alese cu suma mai mare ca cea introdusa")
    print("8.'cautare_tip' - tipareste tranzactiile de un anumit tip")
    print("#########9.'raport_sumtip' - afiseaza suma totala a tranzactiilor de un anumit tip")
    print("10.'raport_sold_zi' - afiseaza soldul la o anumita data")
    print("11.'raport_tip_ascsum' - afiseaza toate tranzactiile de un tip crescator dupa suma")
    print("12.'filtrare_notip' - afiseaza recordul omitand tranzactiile ce sunt de un anumit tip")
    print("13.'filtrare_iftip_nosubsum' - afiseaza recordul omitand tranzactiile ce au suma sub un minim")
    print("#########14.'undo' - duce recordul la versiunea precedenta")
    print("#########15.'afisare' - afiseaza toate tranzactiile curente")
    print("#########16.'exitapp' - opreste programul")

def print_iesire():
    print("Iesire din aplicatie...")

def print_record_gol():
    print("Recordul este gol;")

def print_record_cautat_gol():
    print("Recordul cautat este gol")

def print_mesaj_rog_adauga():
    print("Va rugam sa adaugati elemente in record inainte sa operati pe acesta;")

def print_comanda_nerecunoscuta():
    print("Comanda introdusa nerecunoscuta;")

def print_succes():
    print("Modificare realizata cu succes;")

def print_citire_data():
    print("Introduceti informatiile datei...")

def print_citire_tranzactie():
    print("Introduceti informatiile tranzactiei...")

def print_nicio_schimbare():
    print("Aceasta operatie nu a cauzat nicio schimbare in record;")

def print_back():
    print("Intoarcere in meniul principal...")

def print_no_prop():
    print("Nu exista tranzactii cu proprietatea ceruta;")

def print_citire_perioada():
    print("Introduceti pe rand informatiile datelor, mai intai ale celei inferioare apoi ale celei superioare")

def print_suma():
    print("Suma totala este de: ", end='')

def print_sold():
    print("Soldul este de: ",end='')

def print_nr_para_gresit():
    print("Eroare:Numarul de parametrii dati acestei comenzi este gresit sau exista spatii in plus;\nVerificati meniul pentru a sti ce parametrii sa oferiti si asigurativa ca toate datele introduse de la tastatura sunt despartite de exact un spatiu;")