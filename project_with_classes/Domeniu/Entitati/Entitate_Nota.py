#modul pentru entitatea nota

class Nota:

    def __init__(self,id_student,id_disciplina,valoare):
        """
        functie de intializare a unei entitati de tip nota
        :param id_student: intreg - id-ul studentului caruia ii apartine nota
        :param id_disciplina: intreg - id-ul disciplinei la care este nota
        :param valoare: float - valoarea notei
        """
        self.__id_student=id_student
        self.__id_disciplina=id_disciplina
        self.__valoare=valoare

    def get_id_student(self):
        """
        functie ce returneaza id-ul studentului corepsunzator notei
        :return: intreg reprezentand id-ul studentului
        """
        return self.__id_student

    def get_id_disciplina(self):
        """
        functie ce returneaza id-ul disciplinei corepsunzatoare notei
        :return: intreg reprezentand id-ul disciplinei
        """
        return self.__id_disciplina

    def get_valoare(self):
        """
        functie ce returneaza valoarea unei note
        :return: float reprezentand valoarea notei
        """
        return self.__valoare

    def __eq__(self, other):
        """
        suprascrie ce inseamna ca ceva sa fie egla cu entitatea nota
        :param other: entitatea cu care se verifica egalitatea
        :return:True/False - True daca cele doua entitati sunt egale, False in caz contrar
        """
        try:
            return ((self.__id_student==other.__id_student)and(self.__id_disciplina==other.__id_disciplina))
        except:
            return False
    def __str__(self):
        """
        suprascrie ce inseamna convertirea entitatii in string
        :return: "Nota:*valoare*", unde valoare va fi afisat cu exact 2 zecimale
        """
        nota=str(self.get_valoare())
        if(len(nota)==3 or nota=="10.0"):
            nota=nota+"0"
        return "Nota:"+nota