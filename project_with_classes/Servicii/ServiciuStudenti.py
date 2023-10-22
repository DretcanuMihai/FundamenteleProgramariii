#modul ce contine clasa de controloare a unui repozitoriu de studenti

from Domeniu.Entitati.Entitate_Student import Student
from Infrastructura.Functii_Ajutatoare.functii_siruri_de_caractere import FunctiiSiruriCaractere
from random import randint
from Exceptii.exceptii import RandStudException


class ServiciuStudenti:
    def __init__(self, repo, validator):
        """
        functie ce initializeaza o entitate ControlorStudent
        :param repo: - repozitoriul ce il va folosi
        :param validator: - validatorul ce il va folosi
        """
        self.__repo=repo
        self.__validator=validator

    def numar_studenti(self):
        """
        functie ce verifica numarul de studenti dintr-un repozitoriu
        :return: nr_studenti - numarul de studenti din repozitoriu
        """
        return len(self.__repo)

    def get_studenti(self):
        """
        functie ce returneaza repozitoriul cu studenti
        :return: repo - repozitoriul cu studenti
        """
        return self.__repo.get_studenti()

    def adauga(self, id, nume):
        """
        functie ce valideaza si adauga un student in repozitoriul de studentu
        :param id: - un numar intreg
        :param nume: - un string reprezentand numele
        :return: - nimic, functia modifica in mod direct repozitoriul
        Daca apar erori,acestea vor fi ridicate avand tipul specific
        """
        stud=Student(id,nume)
        self.__validator.validare(stud)
        self.__repo.adauga(stud)

    def cauta(self, id):
        """
        functie ce cauta un student dupa ID-ul sau
        :param id: - un numar intreg
        :return: - stud , entitatea de tip student cu id-ul specificat
        Daca apar erori, acestea vor fi ridiate avand tipul specific
        """
        self.__validator.validare_id(id)
        stud_cautat=self.__repo.cauta(id)
        return stud_cautat

    def sterge(self, id):
        """
        functie ce sterge un student din repozitoriu
        :param id: - id-ul studentului ce va fi sters
        :return: nimic - functia modifica in mod direct repozitoriul
        Daca apar erori, acestea vor fi ridicate avand tipul specific
        """
        self.__validator.validare_id(id)
        self.__repo.sterge(id)

    def modifica(self, id, nume):
        """
        functie ce modifica datele unui Student din repozitoriu
        :param id: - id-ul studentului ce va fi modificat
        :param nume: - numele nou al studentului
        :return: nimic - functia modifica in mod direct repozitoriul
        Daca apar erori, acestea vor fi ridicate avand tipul specific
        """
        stud=Student(id,nume)
        self.__validator.validare(stud)
        self.__repo.modifica(stud)

    def generare_rand(self,numar):
        """
        functie ce genreaza un numar altearoiu de entitati valide si le adauga in repozitoriu
        :param numar: intreg reprezentand numarul  de entitati de generat
        :return: nimic - functia modifica in mod direct repozitroiul
        daca repozitoriul este plin, se va ridica un Exception cu mesajul "Eroare:Repozitoriu plin; Functia de generare
        aleatoriu nu va mai adauga elemente noi;" (repozitoriu are capacitate de 99999 de entitati)
        daca numar este negativ sau 0, se va ridica un Exception cu mesajul "Eroare:Numarul de entitati trebuie sa fie
        pozitiv nenul"
        """
        if(numar<=0):
            raise Exception("Eroare:Numarul de entitati trebuie sa fie pozitiv nenul")
        f=FunctiiSiruriCaractere()
        while(numar):
            id=randint(1,99999)
            nume=f.rand_cuv()+" "+f.rand_cuv()
            st=Student(id,nume)
            try:
                self.__repo.adauga(st)
                numar=numar-1
            except:
                if(len(self.__repo)==99999):
                    raise RandStudException("Eroare:Repozitoriu plin; Functia de generare aleatoriu nu va mai adauga elemente "
                                    "noi;")



