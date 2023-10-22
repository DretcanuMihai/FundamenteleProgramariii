#modul ce lucreaza cu validarea unei entitati de tip disciplina

from Infrastructura.Functii_Ajutatoare.functii_siruri_de_caractere import FunctiiSiruriCaractere
from Exceptii.exceptii import ValidatorDisciplinaException

class ValidatorDisciplina():
    def validare(self, disciplina):
        """
        functie ce valideaza o entitate de tip disciplina
        :param disciplina: - entitatea de tip disciplina ce trebuie validata
        :return: - nimic
        Daca disciplina este de tip invalid, atunci va fi ridicata o exceptie de tip ValidatorDisciplinaException
        ce va contine, dupa caz, mesajele:
        ->"Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;\n"
        ->"Eroare: numele disciplinei trebuie sa fie un string nenul de cuvinte pentru care doar prima litera incepe cu
         majusculta, iar cuvintele sunt despartite cu cate un spatiu;\n"
        ->"Eroare: numele profesorului trebuie sa fie un string de doua cuvinte pentru care doar prima litera este cu
        majuscula, despartite printr-un spatiu\n"
        Ultimul "\n" va disparea cand se ridica eroarea
        """
        erori=""
        id=disciplina.get_id()
        if(id<=0 or id>=1000):
            erori=erori+"Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;\n"
        nume=disciplina.get_nume()
        if(FunctiiSiruriCaractere().fd_corect(nume)==False):
            erori=erori+"Eroare: numele disciplinei trebuie sa fie un string nenul de cuvinte pentru care doar prima" \
                        " litera incepe cu majusculta, iar cuvintele sunt despartite cu cate un spatiu;\n"
        nume_prof=disciplina.get_nume_prof()
        if(FunctiiSiruriCaractere().fn_corect(nume_prof)==False):
            erori=erori+"Eroare: numele profesorului trebuie sa fie un string de doua cuvinte pentru care doar prima" \
                        " litera este cu majuscula, despartite printr-un spatiu\n"
        if(len(erori)!=0):
            erori=erori[:len(erori)-1]
            raise ValidatorDisciplinaException(erori)

    def validare_id(self, id):
        """
        functie ce verifica daca un id este valid
        :param id: intreg - id-ul de verificat
        :return: nimic
        daca id-ul este invalid, atunci va fi ridicata o exceptie de tip ValidatorDisciplinaException cu mesajul
        "Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;"
        """
        if (id <= 0 or id >= 1000):
            raise ValidatorDisciplinaException("Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic"
                                               " ca 1000;")