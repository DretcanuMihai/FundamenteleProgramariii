#modul cu clasa de validator pentru nota

from Exceptii.exceptii import ValidatorNotaException

class ValidatorNota:
    def validare(self, nota):
        """
        functie ce valideaza o nota
        o nota este valida daca are:
        ->id-ul studentului mai mare ca 0 si mai mic ca 100000
        ->id-ul disciplinei mai mare ca 0 si mai mic ca 1000
        ->valoarea notei un float mai mare sau egal cu 1 si mai mic sau egal cu 10
        :param nota: -nota ce trebuie validata
        :return: nimic
        Daca nota este invalid, se va ridica un ValidatorNotaException cu mesajele ce convin de mai jos:
        ->"Eroare: id-ul studentului trebuie sa fie mai mare ca 0 si mai mic ca 100000;\n"
        ->"Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;\n"
        ->"Eroare: valoarea notei trebuie sa fie un float mai mare sau egal cu 1 si mai mic sau egal cu 10;\n"
        """
        erori=""
        id_student=nota.get_id_student()
        if(id_student<=0 or id_student>=100000):
            erori=erori+"Eroare: id-ul studentului trebuie sa fie mai mare ca 0 si mai mic ca 100000;\n"
        id_disciplina=nota.get_id_disciplina()
        if(id_disciplina<=0 or id_disciplina>=1000):
            erori=erori+"Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;\n"
        valoare=nota.get_valoare()
        if(valoare<1.0 or valoare>10.0):
            erori=erori+"Eroare: valoarea notei trebuie sa fie un float mai mare sau egal cu 1 si mai mic sau egal" \
                        " cu 10;\n"
        if(len(erori)>0):
            erori=erori[0:len(erori)-1]
            raise ValidatorNotaException(erori)

    def validare_id_stud(self, id_stud):
        """
        functie ce valideaza un id_stud
        :param id_stud: id-ul de validat
        :return: nimic
        functie ridica un ValidatorNotaException cu mesajul "Eroare: id-ul studentului trebuie sa fie mai mare ca 0 si
         mai mic ca 100000;"
        """
        if(id_stud<=0 or id_stud>=100000):
            raise ValidatorNotaException("Eroare: id-ul studentului trebuie sa fie mai mare ca 0 si mai mic ca 100000;")

    def validare_id_dis(self, id_dis):
        """
        functie ce valideaza un id_dis
        :param id_dis: id-ul de validat
        :return: nimic
        functie ridica un ValidatorNotaException cu mesajul "Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si
         mai mic ca 1000;"
        """
        if(id_dis<=0 or id_dis>=1000):
            raise ValidatorNotaException("Eroare: id-ul disciplinei trebuie sa fie mai mare ca 0 si mai mic ca 1000;")