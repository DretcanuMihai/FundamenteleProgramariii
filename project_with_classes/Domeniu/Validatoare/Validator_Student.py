#modul ce lucreaza cu validarea unei entitati de tip student
from Infrastructura.Functii_Ajutatoare.functii_siruri_de_caractere import FunctiiSiruriCaractere

from Exceptii.exceptii import ValidatorStudentException

class ValidatorStudent:
    def validare(self, stud):
        """
        functie ce valideaza un student
        :param stud: entitate de tip student ce trebuie validata
        :return: -
        functia nu returneaza nimic dar, daca entitatea este invalida, se va ridica o exceptie de tip
        ValidatorStudentException ce contine, dupa caz, mesajele:
        ->"Eroare: id-ul trebuie sa fie mai mare ca 0 si mai mic ca 100000;\n"
        ->"Eroare: numele trebuie sa fie un string de doua cuvinte pentru care doar prima litera este cu majuscula,
        despartite printr-un spatiu\n"
        Ultimul "\n" va disparea atunci cand este ridicata eroarea
        """
        erori=""
        id=stud.get_id()
        if(id<=0 or id>=100000):
            erori=erori+"Eroare: id-ul trebuie sa fie mai mare ca 0 si mai mic ca 100000;\n"
        nume=stud.get_nume()
        if(FunctiiSiruriCaractere().fn_corect(nume)==False):
            erori=erori+"Eroare: numele trebuie sa fie un string de doua cuvinte pentru care doar prima litera este" \
                        " cu majuscula, despartite printr-un spatiu;\n"
        if(len(erori)>0):
            erori=erori[:len(erori)-1]
            raise ValidatorStudentException(erori)

    def validare_id(self, id):
        """
        functie ce valideaza id-ul unui student
        :param id: intreg reprezentand id-ul
        :return: nimic
        Daca id-ul este invalid se va ridica un ValidatorStudentException cu mesajul "Eroare: id-ul trebuie sa fie mai
        mare ca 0 si mai mic ca 100000;"
        """
        if(id<=0 or id>=100000):
            raise ValidatorStudentException("Eroare: id-ul trebuie sa fie mai mare ca 0 si mai mic ca 100000;")
