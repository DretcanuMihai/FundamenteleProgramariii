#modulul ce contine clasa de repozitoriu pentru studenti

from Exceptii.exceptii import RepStudException
from Domeniu.Entitati.Entitate_Student import Student

class RepozitoriuStudenti:
    def __init__(self):
        """
        functie ce initializeaza un repozitoriu cu o lista de studenti vida
        """
        self.__lista_studenti=[]

    def __len__(self):
        """
        functie ce returneaza numarul de elemente din repozitoriu
        :return: l - intreg reprezentand numarul de elemente din repozitoriu
        """
        return len(self.__lista_studenti)

    def get_studenti(self):
        """
        functie ce returneaza lista cu studenti dintr-un repozitoriu
        :return: ls - lista cu studenti
        """
        return self.__lista_studenti

    def cauta(self, id):
        """
        functie ce cauta intr-un repozitoriu un student dupa id
        :param id: - un numar intreg, strict pozitiv ce reprezinta id-ul studentului ce-l cautam
        :return: elem - entitatea de tip student ce o cautam
        functia ridica un RepStudException cu mesajul "Eroare:Nu exista un student cu acest ID;" daca nu exista un
        element cu id-ul dat
        """
        for i in range(0, len(self)):
            elem=self.__lista_studenti[i]
            if(elem.get_id()==id):
                return elem
        raise RepStudException("Eroare:Nu exista un student cu acest ID;")

    def adauga(self,student):
        """
        functie ce adauga un student in lista de studenti
        :param student: - entitate de tip student ce va fi adaugata in lista
        :return:nimic - functia nu returneaza nimic, modificand in mod direct repozitoriul
        functia ridica un RepStudException cu mesajul "Eroare:Exista deja un student cu ID-ul respectiv;"
        """
        if student in self.__lista_studenti:
            raise RepStudException("Eroare:Exista deja un student cu ID-ul respectiv;")
        self.__lista_studenti.append(student)

    def sterge(self, id):
        """
        functie ce sterge studentul cu un anumit id din lista de studenti
        :param id: - numar intreg ce reprezinta id-ul studentului ce va fi sters
        :return:nimic - functie nu returneaza nimic, modificand in mod direct repozitoriul
        functia ridica un RepStudException cu mesajul "Eroare:Nu exista un student cu acest ID;" daca nu exista un
        element cu id-ul dat
        """
        for i in range(0, len(self)):
            elem=self.__lista_studenti[i]
            if(elem.get_id()==id):
                del self.__lista_studenti[i]
                return
        raise RepStudException("Eroare:Nu exista un student cu acest ID;")

    def modifica(self, stud):
        """
        functie ce modifica datele unui student din repozitoriu cu niste date noi, elementul modificat fiind cel
        determina de id-ul aflat in stud
        :param stud: - entitate de tip Student din care se iau datele noi
        :return: - nimic - functie nu returneaza nimic, modificand in mod direct repozitoriul
        functia ridica un RepStudException cu mesajul "Eroare:Nu exista un student cu acest ID;" daca nu exista un
        element cu id-ul dat in stud
        """
        id=stud.get_id()
        for i in range(0, len(self)):
            elem=self.__lista_studenti[i]
            if(elem.get_id()==id):
                self.__lista_studenti[i].set_nume(stud.get_nume())
                return
        raise RepStudException("Eroare:Nu exista un student cu acest ID;")

class RepozitoriuStudentiFisier(RepozitoriuStudenti):
    def __init__(self,nume_fisier):
        RepozitoriuStudenti.__init__(self)
        self.__cale_fisier="./Infrastructura/Repozitorii/BazeDeDate/"+nume_fisier
        self.__citeste_tot()

    def __citeste_tot(self):
        try:
            fisier=open(self.__cale_fisier,"r")
            for linie in fisier:
                linie=linie.strip()
                if(linie!=""):
                    linie=linie.split(";")
                    student=Student(int(linie[0]),linie[1])
                    RepozitoriuStudenti.adauga(self,student)
            fisier.close()
        except IOError:
            RepozitoriuStudenti.__init__(self)
            return

    def __scrie_tot(self):
        l=self.get_studenti()
        try:
            fisier=open(self.__cale_fisier,"w")
            for elem in l:
                fisier.write(str(elem.get_id())+";"+elem.get_nume()+"\n")
            fisier.close()
        except IOError:
            fisier.close()
            raise RepStudException("Eroare:Salvarea datelor in fisier a esuat;")

    def adauga(self,student):
        RepozitoriuStudenti.adauga(self,student)
        self.__scrie_tot()
    def sterge(self, id):
        RepozitoriuStudenti.sterge(self,id)
        self.__scrie_tot()
    def modifica(self, stud):
        RepozitoriuStudenti.modifica(self,stud)
        self.__scrie_tot()

class RepozitoriuStudentiDoarFisier:
    def __init__(self,nume_fisier):
        self.__cale_fisier="./Infrastructura/Repozitorii/BazeDeDate/"+nume_fisier
    def adauga(self,student):
        fisier=open(self.__cale_fisier,"r")
        ok=True
        for linie in fisier:
            linieS=linie.strip()
            if(linieS==""):
                continue
            linieS=linieS.split(";")
            if(student.get_id()==int(linieS[0])):
                ok=False
        fisier.close()
        if(ok==False):
            raise RepStudException("Eroare:Exista deja un student cu ID-ul respectiv;")
        fisier=open(self.__cale_fisier,"a")
        fisier.write(str(student.get_id())+";"+student.get_nume()+"\n")
        fisier.close()

    def sterge(self,id):
        fisier=open(self.__cale_fisier,"r")
        fisier_aux=open("./Infrastructura/Repozitorii/BazeDeDate/auxiliar.txt","w")
        ok=False
        for linie in fisier:
            linieS=linie.strip()
            if(linieS==""):
                continue
            linieS=linieS.split(";")
            if(id==int(linieS[0])):
                ok=True
            else:
                fisier_aux.write(linie)
        fisier.close()
        fisier_aux.close()
        if(ok==False):
            raise RepStudException("Eroare:Nu exista un student cu acest ID;")
        fisier=open(self.__cale_fisier,"w")
        fisier_aux=open("./Infrastructura/Repozitorii/BazeDeDate/auxiliar.txt","r")
        for linie in fisier_aux:
            fisier.write(linie)
        fisier.close()
        fisier_aux.close()

    def modifica(self,student):
        fisier=open(self.__cale_fisier,"r")
        fisier_aux=open("./Infrastructura/Repozitorii/BazeDeDate/auxiliar.txt","w")
        ok=False
        for linie in fisier:
            linieS = linie.strip()
            if (linieS == ""):
                continue
            linieS = linieS.split(";")
            if (student.get_id() == int(linieS[0])):
                ok = True
                fisier_aux.write(str(student.get_id())+";"+student.get_nume()+"\n")
            else:
                fisier_aux.write(linie)
        fisier.close()
        fisier_aux.close()
        if(ok==False):
            raise RepStudException("Eroare:Nu exista un student cu acest ID;")
        fisier = open(self.__cale_fisier, "w")
        fisier_aux = open("./Infrastructura/Repozitorii/BazeDeDate/auxiliar.txt", "r")
        for linie in fisier_aux:
            fisier.write(linie)
        fisier.close()
        fisier_aux.close()
    def cauta(self,id):
        fisier = open(self.__cale_fisier, "r")
        for linie in fisier:
            linieS=linie.strip()
            if(linieS==""):
                continue
            linieS=linieS.split(";")
            if(id==int(linieS[0])):
                fisier.close()
                return Student(int(linieS[0]),linieS[1])
        fisier.close()
        raise RepStudException("Eroare:Nu exista un student cu acest ID;")
    def get_studenti(self):
        fisier=open(self.__cale_fisier,"r")
        l=[]
        for linie in fisier:
            linieS=linie.strip()
            if(linieS==""):
                continue
            linieS=linieS.split(";")
            l.append(Student(int(linieS[0]),linieS[1]))
        fisier.close()
        return l