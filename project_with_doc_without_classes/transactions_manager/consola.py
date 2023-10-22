#consola principala, functiile de tip UI si initializarea comenzilor (user interface)

from functii_mesaje import *
from functii_pentru_record_info import initializare_record_info, get_record, get_element_nv
from functii_pentru_tranzactie import tranzactie_to_string, suma_to_string
from functii_functionalitati import adauga_tranzactie, actualizeaza_tranzactie, record_mod, cautare_subrecord, rapoarte_record, undo

def afisare_record(record):
    """
    functie ce afiseaza tranzactiile din recordul record
    #date de intrare:-> record - recordul ce il afisam
    ##date de iesire:-> -
    """
    if(len(record)==1):
        print_record_gol()
    for tid in record:
        if(tid!="index"):
            tranzactie=get_element_nv(record, tid)
            tranzactie=tranzactie_to_string(tranzactie)
            print(tranzactie)

def afisare_record_ri(record_info):
    """
    functie ce afiseaza  recordul actual din informatiile recordurilor
    #date de intrare:->record_info - informatiile recordurilor de unde luam recordul actual
    ##date de iesire:-> -
    """
    record=get_record(record_info)
    afisare_record(record)

def citire_zi():
    return input("Introduceti ziua:")

def citire_luna():
    return input("Introduceti luna:")

def citire_an():
    return input("Introduceti anul:")

def citire_data():
    print_citire_data()
    zi=citire_zi()
    luna=citire_luna()
    an=citire_an()
    return [zi, luna, an]

def citire_perioada():
    print_citire_perioada()
    print_citire_data()
    zi1=citire_zi()
    luna1=citire_luna()
    an1=citire_an()
    print_citire_data()
    zi2=citire_zi()
    luna2=citire_luna()
    an2=citire_an()
    return [zi1,luna1,an1,zi2,luna2,an2]

def citire_suma():
    return input("Introduceti suma:")

def citire_tip():
    return input("Introduceti tipul:")

def citire_tid():
    return input("Introduceti tidul:")

def citire_data_si_suma():
    print_citire_data()
    zi=citire_zi()
    luna=citire_luna()
    an=citire_an()
    suma=citire_suma()
    return[zi, luna, an,suma]

def citire_suma_si_tip():
    suma=citire_suma()
    tip=citire_tip()
    return[suma,tip]

def ui_adauga_tranzactie(record_info):
    """
    functie de interfata utilizator pentru functia ce adauga o tranzactie in informatiile recordului
    """
    print_citire_tranzactie()
    print_citire_data()
    zi=citire_zi()
    luna=citire_luna()
    an=citire_an()
    suma=citire_suma()
    tip=citire_tip()
    try:
        adauga_tranzactie(record_info, zi, luna,an, suma, tip)
        print_succes()
    except Exception as eroare:
        print(str(eroare))
        print_back()

def ui_actualizare_tranzactie(record_info):
    """
    functie de interfata utilizator pentru functia ce actualizeaza o tranzactie in informatiile recordului
    """
    tid=citire_tid()
    print_citire_tranzactie()
    print_citire_data()
    zi=citire_zi()
    luna=citire_luna()
    an=citire_an()
    suma=citire_suma()
    tip=citire_tip()
    try:
        actualizeaza_tranzactie(record_info, tid, zi, luna, an, suma, tip)
        print_succes()
    except Exception as eroare:
        print(str(eroare))
        print_back()

def initializare_citiri_mod():
    """
    functii ce initializeaza dictionarul cu functii de citire a informatiilor necesare unor conditii de modificare
    #date de intrare:-> -
    ##date de iesire:->citiri - un dictionar de functii de citire
    """
    citiri={}
    citiri["sterge_zi"] = citire_data
    citiri["sterge_perioada"] = citire_perioada
    citiri["sterge_tip"] = citire_tip
    return citiri

def ui_record_mod(record_info, cond):
    """
    functie de interfata utilizator pentru functiile ce modifica recordul dupa niste conditii
    """
    citiri=initializare_citiri_mod()
    info=citiri[cond]()
    try:
        record_mod(record_info, cond, info)
        print_succes()
    except Exception as eroare:
        print(str(eroare))
        print_back()

def initializare_citiri_cautare():
    """
    functie ce initializeaza dictionarul cu functii de citire a informatiilor necesare unor conditii de cautare
    #date de intrare:-> -
    ##date de iesire:->citiri - un dictionar de functii de citire
    """
    citiri={}
    citiri["cautare_supsum"] = citire_suma
    citiri["cautare_supsum_prezi"] = citire_data_si_suma
    citiri["cautare_tip"] = citire_tip
    citiri["filtrare_notip"] = citire_tip
    citiri["filtrare_iftip_nosubsum"] = citire_suma_si_tip
    return citiri

def ui_cautare_subrecord(record_info, cond):
    """
    functie de interfata utilizator pentru functiile ce cauta anumite subrecorduri in record
    """
    citiri=initializare_citiri_cautare()
    info=citiri[cond]()
    try:
        subrecord=cautare_subrecord(record_info, cond, info)
        afisare_record(subrecord)
    except Exception as eroare:
        print(str(eroare))
        print_back()

def initializare_citiri_rapoarte():
    """
    functie ce initializeaza dictionarul cu functii de citire a informatiilor necesare unor conditii de rapoarte
    #date de intrare:-> -
    ##date de iesire:->citiri - un dictionar de functii de citire
    """
    citiri={}
    citiri["raport_sumtip"] = citire_tip
    citiri["raport_sold_zi"] = citire_data
    citiri["raport_tip_ascsum"] = citire_tip
    return citiri

def afisare_raport_sumtip(suma):
    """
    functie ce afiseaza o suma totala
    #date de intrare:->suma - suma de afisat
    """
    print_suma()
    print(suma_to_string(suma))

def afisare_raport_sold_zi(sold):
    """
    functie ce afiseaza un sold
    #date de intrare:->sold - soldul de afisat
    """
    print_sold()
    print(suma_to_string(sold))

def afisare_raport_tip_ascsum(record_lista):
    for i in range(0, len(record_lista)):
        tranzactie=record_lista[i]
        tranzactie=tranzactie_to_string(tranzactie)
        print(tranzactie)

def initializare_afisari_rapoarte():
    """
    functii ce initializeaza dictionarul cu functii de afisare a unui raport de record
    #date de intrare:-> -
    ##date de iesire:->afisari - un dictionar cu functii de afisare a raportului
    """
    afisari={}
    afisari["raport_sumtip"] = afisare_raport_sumtip
    afisari["raport_sold_zi"] = afisare_raport_sold_zi
    afisari["raport_tip_ascsum"] = afisare_raport_tip_ascsum
    return afisari

def ui_rapoarte_record(record_info, cond):
    """
    functie de interfata utilizator pentru functiile ce determina rapoarte
    """
    citiri=initializare_citiri_rapoarte()
    info=citiri[cond]()
    try:
        rap=rapoarte_record(record_info, cond, info)
        afisari=initializare_afisari_rapoarte()
        afisari[cond](rap)
    except Exception as eroare:
        print(str(eroare))
        print_back()


def ui_undo(record_info):
    """
    functie ce incearca sa apeleze functia undo
    """
    try:
        undo(record_info)
        print_succes()
    except Exception as eroare:
        print(str(eroare))

def initializare_comenzi_conditionale():
    """
    functie ce initializeza dictionarul cu comenzi conditionale
    #date de intrare:-> -
    ##date de iesire:->commands - un dictionar cu functiile pentru functionalitatile conditionale accesibile din meniu
    """
    commands={}
    commands["sterge_zi"] = ui_record_mod
    commands["sterge_perioada"] = ui_record_mod
    commands["sterge_tip"] = ui_record_mod
    commands["cautare_supsum"] = ui_cautare_subrecord
    commands["cautare_supsum_prezi"] = ui_cautare_subrecord
    commands["cautare_tip"] = ui_cautare_subrecord
    commands["raport_sumtip"] =ui_rapoarte_record
    commands["raport_sold_zi"] = ui_rapoarte_record
    commands["raport_tip_ascsum"] = ui_rapoarte_record
    commands["filtrare_notip"] = ui_cautare_subrecord
    commands["filtrare_iftip_nosubsum"] = ui_cautare_subrecord
    return commands

def initializare_comenzi_neconditionale():
    """
    functie ce initializeaza dictionarul cu comenzi
    #date de intrare:-> -
    ##date de iesire:->commands - un dictionar cu functiile pentru functionalitatile neconditionale accesibile din meniu
    """
    commands={}
    commands["actualizare"] = ui_actualizare_tranzactie
    return commands

def consola():
    """
    consola principala, de unde se citesc comenzile si se acceseaza functionalitatile
    #date de intrare:-> -
    ##date de iesire:-> -
    """
    print_bootup()
    record_info=initializare_record_info()
    commands_nc=initializare_comenzi_neconditionale()
    commands_c=initializare_comenzi_conditionale()
    rulare=True
    while(rulare):
        cmd=input(">>>")
        if(cmd=="exitapp"):
            print_iesire()
            rulare=False
        elif(cmd=="meniu"):
            print_meniu()
        elif(cmd=="adauga"):
            ui_adauga_tranzactie(record_info)
        elif(cmd=="undo"):
            ui_undo(record_info)
        elif(cmd=="afisare"):
            afisare_record_ri(record_info)
        elif(cmd in commands_nc):
            if (len(get_record(record_info)) == 1):
                print_mesaj_rog_adauga()
            else:
                commands_nc[cmd](record_info)
        elif(cmd in commands_c):
            if (len(get_record(record_info)) == 1):
                print_mesaj_rog_adauga()
            else:
                commands_c[cmd](record_info, cmd)
        else:
            print_comanda_nerecunoscuta()

def consola_bulk():
    print_bootup()
    record_info = initializare_record_info()
    rulare = True
    while(rulare):
        command=input(">>>")
        command=command.split(";")
        while(len(command)!=0):
            comanda_actuala=command.pop(0)
            comanda_actuala=comanda_actuala.strip()
            comanda_actuala=comanda_actuala.split(" ")
            cmd=comanda_actuala[0]
            if (cmd == "exitapp"):
                if(len(comanda_actuala)==1):
                    print_iesire()
                    rulare = False
                    return
                else:
                    print_nr_para_gresit()
            elif (cmd == "meniu"):
                if(len(comanda_actuala)==1):
                    print_meniu()
                else:
                    print_nr_para_gresit()
            elif (cmd=="adauga"):
                if(len(comanda_actuala)==6):
                    info=comanda_actuala
                    try:
                        adauga_tranzactie(record_info, info[1],info[2],info[3],info[4],info[5])
                    except Exception as eroare:
                        print(eroare)
                else:
                    print_nr_para_gresit()
            elif(cmd=="undo"):
                if(len(comanda_actuala)==1):
                    try:
                        undo(record_info)
                    except Exception as eroare:
                        print(eroare)
                else:
                    print_nr_para_gresit()
            elif(cmd=="afisare"):
                if(len(comanda_actuala)==1):
                    afisare_record_ri(record_info)
                else:
                    print_nr_para_gresit()
            elif((len(get_record(record_info))==1)and(cmd=="sterge_zi" or cmd=="raport_sumtip")):
                print_mesaj_rog_adauga()
            elif(cmd=="sterge_zi"):
                if(len(comanda_actuala)==4):
                    try:
                        info=comanda_actuala
                        record_mod(record_info, info[0], [info[1],info[2],info[3]])
                    except Exception as eroare:
                        print(eroare)
                else:
                    print_nr_para_gresit()
            elif(cmd=="raport_sumtip"):
                if(len(comanda_actuala)==2):
                    try:
                        info=comanda_actuala
                        rap=rapoarte_record(record_info, info[0],info[1])
                        afisare_raport_sumtip(rap)
                    except Exception as eroare:
                        print(eroare)
                else:
                    print_nr_para_gresit()
            else:
                print_comanda_nerecunoscuta()



#consola()
consola_bulk()