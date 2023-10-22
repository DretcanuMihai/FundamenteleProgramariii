#modul ce contine clasa pentru interfata utilizator pentru melodii

from Exceptii.Exceptii import RepozitoriuMelodiiException,ValidatorMelodieException,ExportException,ValidatorAlteleException,RandomException

class UI_Melodii():
    def __init__(self,serviciu):
        """
        initializeaza o clasa de ui pentru interfata de utilizator la melodii
        :param serviciu: ServiciuMelodii
        """
        self.__serviciu=serviciu
    def __ui_meniu(self):
        """
        printeaza un meniu cu comenzile disponibile
        :return: None
        """
        print("Meniu:\n"
              "0.'exit' - iesire din aplicatie;\n"
              "1.'meniu' - afisare lista de comenzi;\n"
              "2.'modifica' - modifica o melodie din repozitoriu dupa titlu si artist;\n"
              "3.'export' - exporteaza intr-un fisier csv toate melodiile din repozitoriu;\n"
              "4.'random' - creaza aleatoriu un numar de entitati melodie;")
    def __ui_modifica(self):
        """
        interfata utilizator pentru modificarea unei melodii
        Utilizatorul introduce un titlu, un artist, un gen si o durata pentru melodie, identificarea facandu-se dupa
        titlu si artist
        :return: None
        """
        titlu=input("Introduceti titlul melodiei:")
        artist = input("Introduceti artistul melodiei:")
        gen = input("Introduceti genul melodiei:")
        durata = int(input("Introduceti durata melodiei:"))
        self.__serviciu.modifica_melodie(titlu,artist,gen,durata)
        print("Modificare realizata cu succes;")
    def __ui_export(self):
        """
        interfata utiliator pentru exportarea melodiilor
        Utilizaorul introduce un nume de fisier
        :return: None
        """
        nume_fisier=input("Introduceti numele fisierului:")
        self.__serviciu.export(nume_fisier)
        print("Exportare realizata cu succes;")
    def __ui_random(self):
        numar=int(input("Introduceti numarul de melodii de generat:"))
        lista=input("Introduceti lista de titluri si melodii:")
        nr=self.__serviciu.generator(numar,lista)
        print("S-au generat cu succes ",nr," melodii;")
    def __initializeaza_comenzi(self):
        """
        initializeaz aun dictionar de comenzi pentru aplicatie
        :return: dictionar cu chei string-uri asociate unor functii
        """
        comenzi={'meniu':self.__ui_meniu,
                 'modifica':self.__ui_modifica,
                 'export':self.__ui_export,
                 'random':self.__ui_random}
        return comenzi
    def ruleaza(self):
        """
        ruleaza interfata utilizator
        :return: None
        """
        comenzi=self.__initializeaza_comenzi()
        print("Aplicatie pornita cu succes;\nPentru a vedea o lista cu comenzile posibile introduceti comanda 'meniu'")
        while(True):
            cmd=input(">>>")
            if cmd=="exit":
                print("Iesire din aplicatie...")
                return
            elif cmd in comenzi:
                try:
                    comenzi[cmd]()
                except RepozitoriuMelodiiException as er:
                    print(er)
                except ValidatorMelodieException as er:
                    print(er)
                except ValidatorAlteleException as er:
                    print(er)
                except ExportException as er:
                    print(er)
                except RandomException as er:
                    print(er)
                except ValueError:
                    print("Valoare numerica invalida;")
            else:
                print("Comanda introdusa invalida;\nIntroduceti 'meniu' pentru a vedea o lista cu comenzile valabile;")