#modul ce defineste clasa de repozitoriu de discipline

from Exceptii.exceptii import RepDisException
from Domeniu.Entitati.Entitate_Disciplina import Disciplina

class RepozitoriuDiscipline:
    def __init__(self):
        """
        functie ce intializeaza un repozitoriu cu o lista goala de discipline
        """
        self.__lista_discipline=[]

    def __len__(self):
        """
        funtie ce determina cate discipline se afla intr-un repozitoriu
        :return: l - intreg reprezentand numarul de discipline
        """
        return len(self.__lista_discipline)

    def get_discipline(self):
        """
        functie ce returneaza o lista cu disciplinele din repozitoriu
        :return: lista - lista cu discipline
        """
        return self.__lista_discipline

    def cauta(self,id):
        """
        functie ca cauta o disciplina dupa id in repozitoriu
        :param id: nr intreg reprezentand id-ul dupa care se cauta
        :return: disciplina - disciplina cu id-ul id
        Daca nu exista o discilpina cu id-ul introdus se va ridica un RepDisException cu mesajul
        "Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        """
        for elem in self.__lista_discipline:
            if(elem.get_id()==id):
                return elem
        raise RepDisException("Eroare:Nu exista o disciplina cu ID-ul respectiv;")

    def adauga(self,disciplina):
        """
        functie ce adauga o disciplina in repozitoriul de discilpine
        :param disciplina: - o entitate de tip disciplina valida
        :return: nimic - functia modifica in mod direct repozitoriul
        Daca exista deja o discilplina cu id-ul introdus se va ridica un RepDisException cu mesajul
        "Eroare:Exista deja o disciplina cu ID-ul respectiv;"
        """
        if disciplina in self.__lista_discipline:
            raise RepDisException("Eroare:Exista deja o disciplina cu id-ul respectiv;")
        self.__lista_discipline.append(disciplina)

    def sterge(self, id):
        """
        functie ce sterge o disciplina din repozitoriu dupa id
        :param id: - un intreg reprezentand id-ul discplinei ce trebuie stearsa
        :return: nimic - functia modifica in mod direct repozitoriul
        Daca nu exista o discilpina cu id-ul introdus se va ridica un RepDisException cu mesajul
        "Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        """
        for i in range(0,len(self)):
            if(self.__lista_discipline[i].get_id()==id):
                del self.__lista_discipline[i]
                return
        raise RepDisException("Eroare:Nu exista o disciplina cu ID-ul respectiv;")

    def modifica(self, disciplina):
        """
        functie ce modifica o disciplina din repozitoriu dupa id
        :param disciplina: - o entitate de tip disciplina ce va suprascrie elementul din repozitoriu cu id-ul egal
        cu id-ul propriu
        :return: nimic - functia modifica in mod direct repozitoriul
        Daca nu exista o discilpina cu id-ul introdus se va ridica un RepDisException cu mesajul
        "Eroare:Nu exista o disciplina cu ID-ul respectiv;"
        """
        for i in range(0,len(self)):
            if(disciplina==self.__lista_discipline[i]):
                self.__lista_discipline[i].set_nume(disciplina.get_nume())
                self.__lista_discipline[i].set_nume_prof(disciplina.get_nume_prof())
                return
        raise RepDisException("Eroare:Nu exista o disciplina cu ID-ul respectiv;")

class RepozitoriuDisciplineFisier(RepozitoriuDiscipline):
    def __init__(self,nume_fisier):
        RepozitoriuDiscipline.__init__(self)
        self.__cale_fisier = "./Infrastructura/Repozitorii/BazeDeDate/" + nume_fisier
        self.__citeste_tot()

    def __citeste_tot(self):
        try:
            fisier = open(self.__cale_fisier, "r")
            for linie in fisier:
                linie = linie.strip()
                if (linie != ""):
                    linie = linie.split(";")
                    dis = Disciplina(int(linie[0]), linie[1],linie[2])
                    RepozitoriuDiscipline.adauga(self, dis)
            fisier.close()
        except IOError:
            RepozitoriuDiscipline.__init__(self)
            return

    def __scrie_tot(self):
        l = self.get_discipline()
        try:
            fisier = open(self.__cale_fisier, "w")
            for elem in l:
                fisier.write(str(elem.get_id()) + ";" + elem.get_nume()+";"+elem.get_nume_prof() + "\n")
            fisier.close()
        except IOError:
            fisier.close()
            raise RepDisException("Eroare:Salvarea datelor in fisier a esuat;")
    def adauga(self,disciplina):
        RepozitoriuDiscipline.adauga(self,disciplina)
        self.__scrie_tot()
    def sterge(self, id):
        RepozitoriuDiscipline.sterge(self,id)
        self.__scrie_tot()
    def modifica(self, disciplina):
        RepozitoriuDiscipline.modifica(self,disciplina)
        self.__scrie_tot()