#modul ce contine clas apentru repozitoriul de note

from Exceptii.exceptii import RepNoteException
from Domeniu.Entitati.Entitate_Nota import Nota

class RepozitoriuNote:

    def __init__(self):
        """
        functie ce initializeaza un repozitoriu de note gol
        """
        self.__lista_note=[]

    def __len__(self):
        """
        functie ce suprascrie functia de lungime, returnand numarul de note din repozitoriu
        :return: intreg reprezentand numarul de note
        """
        return len(self.__lista_note)

    def get_all(self):
        """
        functie ce returneaza lista de nota
        :return: lista - o lista cu toate notele
        """
        return self.__lista_note

    def adauga_nota(self, nota,ind=0):
        """
        functie ce adauga o nota in repozitoriul de note
        :param nota: nota de adaugat in repo
        :return: nimic, programul modifica in mod direct repo-ul
        Daca exista deja o nota cu acelasi elev si disciplina, se va ridica un RepNoteException cu mesajul
        "Eroare:Exista deja o nota atribuita studentului respectiv la disciplina selectata;"
        """
        if(ind==len(self)):
            self.__lista_note.append(nota)
            return
        if(nota==self.__lista_note[ind]):
            raise RepNoteException("Eroare:Exista deja o nota atribuita studentului respectiv la disciplina selectata;")
        RepozitoriuNote.adauga_nota(self,nota,ind+1)

    def cauta_nota(self,id_stud,id_dis,ind=0):
        """
        functie ce cauta o nota in repozitoriul de note dupa id-ul studentului si id-ul disciplinei
        :param id_stud: intreg reprezentand id-ul studentului
        :param id_dis: intreg reprezentand id-ul disciplinei
        :return: nota - nota cautata
        Daca nu exista nota cautata, se va ridica un RepNoteException cu mesajul
        "Eroare:Nu exista nota cautata;"
        """
        if(ind>=len(self)):
            raise RepNoteException("Eroare:Nu exista nota cautata;")
        elem=self.__lista_note[ind]
        if(elem.get_id_student()==id_stud and elem.get_id_disciplina()==id_dis):
            return elem
        else:
            return self.cauta_nota(id_stud,id_dis,ind+1)

    def sterge_nota(self, id_stud, id_dis,ind=0):
        """
        functie ce sterge o nota din repozitoriu dupa id-ul studentului careia este atribuit si id-ul disciplinei
        :param id_stud: intreg, id-ul studentului
        :param id_dis: intreg, id-ul disciplinei
        :return: nimic
        Daca nu exista nota cautata, se va ridica un RepNoteException cu mesajul
        "Eroare:Nu exista nota cautata;"
        """
        if(ind>=len(self)):
            raise RepNoteException("Eroare:Nu exista nota cautata;")
        elem=self.__lista_note[ind]
        if(elem.get_id_student()==id_stud and elem.get_id_disciplina()==id_dis):
            del self.__lista_note[ind]
            return
        else:
            RepozitoriuNote.sterge_nota(self,id_stud,id_dis,ind+1)
        """
        Calcul de complexitate:
        o)Vom nota cu n numarul de elemente din lista noastra
        ->caz favorabil: elementul de sters se afla pe prima pozitie - teta(1)
        ->caz nefavorabil: elementul de sters nu se afla in lista - teta(n)
        ->caz mediu: Suma k=1,n din k*P(k) = Suma k=1,n+1 din k*(1/(n+1)) = (1/(n+1))*(Suma k=1,n din k) =
        =(1/(n+1))* (n+1)(n+2)/2 =(n+2)/2 -> teta(n)
        ->caz general: O(n) 
        """

class RepozitoriuNoteFisier(RepozitoriuNote):
    def __init__(self,nume_fisier):
        RepozitoriuNote.__init__(self)
        self.__cale_fisier="./Infrastructura/Repozitorii/BazeDeDate/"+nume_fisier
        self.__citeste_tot()

    def __citeste_tot(self):
        try:
            fisier=open(self.__cale_fisier,"r")
            for linie in fisier:
                linie=linie.strip()
                if(linie!=""):
                    linie=linie.split(";")
                    nota=Nota(int(linie[0]),int(linie[1]),float(linie[2]))
                    RepozitoriuNote.adauga_nota(self,nota)
            fisier.close()
        except IOError:
            RepozitoriuNote.__init__(self)
            return

    def __scrie_tot(self):
        l=self.get_all()
        try:
            fisier=open(self.__cale_fisier,"w")
            for elem in l:
                fisier.write(str(elem.get_id_student())+";"+str(elem.get_id_disciplina())+";"+str(elem.get_valoare())+"\n")
            fisier.close()
        except IOError:
            fisier.close()
            raise RepNoteException("Eroare:Salvarea datelor in fisier a esuat;")
    def adauga_nota(self, nota):
        RepozitoriuNote.adauga_nota(self,nota)
        self.__scrie_tot()
    def sterge_nota(self, id_stud, id_dis):
        RepozitoriuNote.sterge_nota(self,id_stud,id_dis)
        self.__scrie_tot()