#modul ce contine definirea entiatii student

class Student:
    def __init__(self, id, nume):
        """
        functie ce creeaza o entitate de tip student
        :param id: un intreg
        :param nume: un string
        """
        self.__id=id
        self.__nume=nume
    def get_id(self):
        """
        functie ce returneaza id-ul unui Student
        :return: id - un intreg reprezentand id-ul studentului
        """
        return self.__id
    def get_nume(self):
        """
        functie ce returneaza numele unui student
        :return: nume - un string reprezentand numele studentului
        """
        return self.__nume

    def set_nume(self, nume_nou):
        """
        functie ce schimba numele unui Student
        :param nume_nou: string - noul nume
        :return: -
        functia nu returneaza nimic, schimband in mod activ entitatea
        """
        self.__nume=nume_nou

    def __eq__(self,other):
        """
        doua entitati "Student" vor fi egale daca au acelasi identificator
        :param other: entitatea de tip Student cu care verificam daca este egal
        :return: True - daca au acelasi ID (False in caz contrar)
        """
        try:
            return self.__id==other.__id
        except:
            return False

    def __str__(self):
        """
        functie ce returneaza string-ul specific unei entitati de tip Student
        :return: "Student - ID:*id*; Nume:*nume*"
        """
        return "Student - ID:"+str(self.get_id())+"; Nume:"+self.get_nume()