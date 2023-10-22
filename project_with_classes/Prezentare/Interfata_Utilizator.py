#modul ce contine clasa de interfata a utilizatorului

from Prezentare.Mesaje import Mesaje
from Exceptii.exceptii import *

class Interfata_Utilizator:
    def __init__(self, seriviciu_studenti, seriviciu_discipline, serviciu_note):
        """
        functie ce initializeaza
        :param seriviciu_studenti:
        """
        self.__ss=seriviciu_studenti
        self.__sd=seriviciu_discipline
        self.__sn=serviciu_note
        self.__mesaje=Mesaje()

    def __UI_afisare_studenti(self):
        """
        interfata utilizator pentru afisarea repozitoriului de studenti
        :return: - nimic
        """
        repo=self.__ss.get_studenti()
        if(len(repo)==0):
            self.__mesaje.rep_stud_gol()
        else:
            for elem in repo:
                print(str(elem))

    def __UI_adauga_student(self):
        """
        interfata utilizator pentru adaugare student in repozitoriu
        :return: - nimic
        """
        id=int(input("Introduceti id-ul:"))
        nume=input("Introduceti numele:")
        self.__ss.adauga(id,nume)
        self.__mesaje.succes()

    def __UI_cauta_student(self):
        """
        interfata utilizator pentru adaugare student in repozitoriu
        :return: - nimic
        """
        id=int(input("Introduceti id-ul:"))
        student=self.__ss.cauta(id)
        print(str(student))

    def __UI_sterge_student(self):
        """
        interfata utilizator pentru stergerea unui student din repozitoriu
        :return: - nimic
        """
        id=int(input("Introduceti id-ul:"))
        self.__sn.sterge_student(id)
        self.__mesaje.succes()

    def __UI_modifica_student(self):
        """
        interfata utilizator pentru stergerea unui student din repozitoriu
        :return: - nimic
        """
        id=int(input("Introduceti id-ul:"))
        nume=input("Introduceti numele:")
        self.__ss.modifica(id,nume)
        self.__mesaje.succes()

    def __UI_afisare_discipline(self):
        """
        interfata utilizator pentru afisarea disciplinelor din repozitoriu
        :return: - nimic
        """
        repo=self.__sd.get_discipline()
        if(len(repo)==0):
            self.__mesaje.rep_dis_gol()
        else:
            for elem in repo:
                print(str(elem))

    def __UI_adauga_disciplina(self):
        """
        intefata utilizator pentru adaugarea unei discipline
        :return: - nimic
        """
        id=int(input("Introduceti id-ul:"))
        nume=input("Introduceti numele disciplinei:")
        nume_profesor=input("Introduceti numele profesorului:")
        self.__sd.adauga(id,nume,nume_profesor)
        self.__mesaje.succes()

    def __UI_cauta_disciplina(self):
        """
        intefata utilizator pentru cautarea unei discipline
        :return: - nimic
        """
        id=int(input("Introduceti id-ul:"))
        dis=self.__sd.cauta(id)
        print(str(dis))

    def __UI_modifica_disciplina(self):
        """
        intefata utilizator pentru modificarea unei discipline
        :return: - nimic
        """
        id=int(input("Introduceti id-ul:"))
        nume=input("Introduceti numele disciplinei:")
        nume_profesor=input("Introduceti numele profesorului:")
        self.__sd.modifica(id,nume,nume_profesor)
        self.__mesaje.succes()

    def __UI_sterge_disciplina(self):
        """
        intefata utilizator pentur stergerea unei discipline
        :return: - nimic
        """
        id=int(input("Introduceti id-ul:"))
        self.__sn.sterge_disciplina(id)
        self.__mesaje.succes()

    def __UI_generare_studenti(self):
        """
        interfata utilizator pentru generarea aleatorie a unor studenti
        :return: - nimic
        """
        nr=int(input("Introduceti numarul de entitati de generat:"))
        self.__ss.generare_rand(nr)
        self.__mesaje.succes()

    def __UI_generare_discipline(self):
        """
        interfata utilizator pentru generarea aleatorie a unor discipline
        :return: - nimic
        """
        nr=int(input("Introduceti numarul de entitati de generat:"))
        self.__sd.generare_rand(nr)
        self.__mesaje.succes()

    def __UI_afiseaza_note(self):
        """
        interfata utilizator pentru afisarea tutoror notelor din repozitoriu
        :return: nimic
        """
        l=self.__sn.get_all_for_print()
        if(len(l)==0):
            self.__mesaje.rep_note_gol()
        else:
            for elem in l:
                print(str(elem[0])+"||"+str(elem[1])+"||"+str(elem[2]))

    def __UI_adauga_nota(self):
        """
        interfata utilizator pentru adaugarea unei note
        :return: - nimic
        """
        id_stud=int(input("Introduceti id-ul studentului:"))
        id_dis=int(input("Introduceti id-ul disciplinei:"))
        val=float(input("Introduceti valoarea notei (va fi rotunjita la 2 zecimale):"))
        val=round(val,2)
        self.__sn.adauga_nota(id_stud,id_dis,val)
        self.__mesaje.succes()

    def __UI_raport_note_alfabetic(self):
        """
        interfata utilizator pentru generarea raportului de note aranjat alfabetic
        :return: - nimic
        """
        id_dis=int(input("Introcueti id-ul disciplinei:"))
        R=self.__sn.raport_disciplina_aflabetic(id_dis)
        if(len(R)==1):
            print("Nu exista studenti in repozitoriu")
        else:
            print(str(R[0])+" || Raport:")
            for i in range(1,len(R)):
                elem=R[i]
                if(elem[1]==None):
                    print("-> "+str(elem[0])+" || Studentul nu are nota la aceasta materie")
                else:
                    print("-> "+str(elem[0])+" || "+str(elem[1]))

    def __UI_raport_note_descrescator(self):
        """
        interfata utilizator pentru generarea raportului de note aranjat descrescator dupa valoare
        :return: - nimic
        """
        id_dis=int(input("Introcueti id-ul disciplinei:"))
        R=self.__sn.raport_disciplina_descrescator(id_dis)
        if(len(R)==1):
            print("Nu exista studenti in repozitoriu")
        else:
            print(str(R[0])+" || Raport:")
            for i in range(1,len(R)):
                elem=R[i]
                if(elem[1]==None):
                    print("-> "+str(elem[0])+" || Studentul nu are nota la aceasta materie")
                else:
                    print("-> "+str(elem[0])+" || "+str(elem[1]))

    def __UI_20_la_suta(self):
        """
        interfata utilizaotr pentru obtinerea primilor 20% din elevi dupa medie
        :return: - nimic
        """
        R=self.__sn.raport_20_la_suta()
        if(len(R)==0):
            print("Eroare:Nu exista studenti in repozitoriu, deci raportul nu are sens;")
        else:
            for elem in R:
                print(str(elem[0])+"|| Media:"+str(elem[1]))

    def __UI_top_profesori(self):
        """
        interfata utilizator pentru obtinerea tuturor profesorilor ordonati dupa medie
        :return: - nimic
        """
        R=self.__sn.raport_profesori_descrescator()
        if(len(R)==0):
            print("Eroare:Nu exista discipline in repozitoriu, deci raportul nu are sens;")
        else:
            for elem in R:
                print(elem[0]+"|| Media notelor date:"+str(elem[1]))

    def __UI_comenzi(self):
        """
        functie ce initializeaza un dictionar de comenzi UI
        :return: comenzi - un dictionar de comenzi UI
        """
        comenzi={"meniu":self.__mesaje.meniu,
                 "afisare_studenti":self.__UI_afisare_studenti,
                 "adauga_student":self.__UI_adauga_student,
                 "cauta_student":self.__UI_cauta_student,
                 "modifica_student":self.__UI_modifica_student,
                 "sterge_student":self.__UI_sterge_student,
                 "afisare_discipline":self.__UI_afisare_discipline,
                 "adauga_disciplina":self.__UI_adauga_disciplina,
                 "cauta_disciplina":self.__UI_cauta_disciplina,
                 "modifica_disciplina":self.__UI_modifica_disciplina,
                 "sterge_disciplina":self.__UI_sterge_disciplina,
                 "generare_studenti":self.__UI_generare_studenti,
                 "generare_discipline":self.__UI_generare_discipline,
                 "afisare_note":self.__UI_afiseaza_note,
                 "adauga_nota":self.__UI_adauga_nota,
                 "raport_note_alfabetic":self.__UI_raport_note_alfabetic,
                 "raport_note_descrescator":self.__UI_raport_note_descrescator,
                 "raport_20_la_suta":self.__UI_20_la_suta,
                 "raport_profesori_medie":self.__UI_top_profesori
                 }
        return comenzi


    def ruleaza(self):
        """
        functia de consola
        :return: nimic - functia nu returneaza nimic, doar afiseaza consola
        """
        afiseaza=self.__mesaje
        comenzi=self.__UI_comenzi()
        afiseaza.start()
        while(True):
            cmd=input(">>>")
            if(cmd=="exit"):
                afiseaza.exit()
                return
            elif(cmd in comenzi):
                try:
                    comenzi[cmd]()
                except ValueError:
                    afiseaza.date_invalide()
                except ValidatorStudentException as eroare:
                    print(str(eroare))
                except RepStudException as eroare:
                    print(str(eroare))
                except ValidatorDisciplinaException as eroare:
                    print(str(eroare))
                except RepDisException as eroare:
                    print(str(eroare))
                except RandDisException as eroare:
                    print(str(eroare))
                except RandStudException as eroare:
                    print(str(eroare))
                except ValidatorNotaException as eroare:
                    print(str(eroare))
                except RepNoteException as eroare:
                    print(str(eroare))
            else:
                afiseaza.comanda_nerecunoscuta()