#modul ce contine clasa de serviciu pentru discipline

from Domeniu.Entitati.Entitate_Disciplina import Disciplina
from random import randint
from Infrastructura.Functii_Ajutatoare.functii_siruri_de_caractere import FunctiiSiruriCaractere
from Exceptii.exceptii import RandDisException


class SeriviciuDiscipline:
    def __init__(self, repo, validator):
        self.__repo=repo
        self.__validator=validator

    def numar_discipline(self):
        """
        functie ce returneaza numarul de discipline din repozitoriu
        :return: intreg reprezentand numarul de discipline
        """
        return len(self.__repo)

    def get_discipline(self):
        """
        functie ce reutnreaza o lista cu toate disciplinele din repozitoriu
        :return:
        """
        return self.__repo.get_discipline()
    def cauta(self, id):
        """
        functie ce cauta o disciplina dupa id
        :param id: intreg reprezetnand id-ul disciplinei ce este cautata
        :return: disciplina cauta sau None daca nu exista disciplina
        daca apar erori, acestea vor fi ridicate
        """
        self.__validator.validare_id(id)
        dis_cautata=self.__repo.cauta(id)
        return dis_cautata

    def adauga(self, id, nume_dis, nume_prof):
        """
        functie ce adauga o disciplina intr-un repozitoriu de discipline
        :param id: intreg - id-ul disciplinei
        :param nume_dis: string - numele disciplinei
        :param nume_prof: string - numele profesorului
        :return: Nimic - programul modifica in mod direct repo-ul
        daca apar erori, acestea vor fi ridicate
        """
        dis=Disciplina(id, nume_dis, nume_prof)
        self.__validator.validare(dis)
        self.__repo.adauga(dis)

    def sterge(self, id):
        """
        functie ce sterge o disciplina intr-un repo dupa id
        :param id: intreg - id-ul disciplinei de sters
        :return: nimic - programul modifica in mod direct repo-ul
        daca apar erori, ele vor fi ridiate
        """
        self.__validator.validare_id(id)
        self.__repo.sterge(id)

    def modifica(self,id, nume_dis, nume_prof):
        """
        functie ce modifica o disciplina intr-un repozitoriu de discipline
        :param id: intreg - id-ul disciplinei de modificat
        :param nume_dis: string - numele nou al disciplinei
        :param nume_prof: string - numele nou al profesorului
        :return: nimic
        daca apar erori, acestea vor fi ridicate
        """
        dis=Disciplina(id,nume_dis,nume_prof)
        self.__validator.validare(dis)
        self.__repo.modifica(dis)

    def generare_rand(self,numar):
        """
        functie ce genreaza un numar altearoiu de entitati valide si le adauga in repozitoriu
        :param numar: intreg reprezentand numarul  de entitati de generat
        :return: nimic - functia modifica in mod direct repozitoriul
        daca repozitoriul este plin, se va ridica un Exception cu mesajul "Eroare:Repozitoriu plin; Functia de generare
        aleatoriu nu va mai adauga elemente noi;"(repozitoriu are capacitate de 999 de entitati)
        daca numar este negativ sau 0, se va ridica un Exception cu mesajul "Eroare:Numarul de entitati trebuie sa fie
        pozitiv nenul"
        """
        if(numar<=0):
            raise Exception("Eroare:Numarul de entitati trebuie sa fie pozitiv nenul")
        f=FunctiiSiruriCaractere()
        while(numar):
            id=randint(1,999)
            nume=""
            numar_cuv=randint(0,3)
            while(numar_cuv):
                nume=nume+f.rand_cuv()+" "
                numar_cuv=numar_cuv-1
            nume=nume+f.rand_cuv()
            nume_prof=f.rand_cuv()+" "+f.rand_cuv()
            dis=Disciplina(id,nume,nume_prof)
            try:
                self.__repo.adauga(dis)
                numar=numar-1
            except:
                if(len(self.__repo)==999):
                    raise RandDisException("Eroare:Repozitoriu plin; Functia de generare aleatoriu nu va mai adauga elemente "
                                    "noi;")