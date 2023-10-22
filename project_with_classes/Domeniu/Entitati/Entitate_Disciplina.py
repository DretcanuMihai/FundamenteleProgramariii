#modul ce contine definirea entiatii disciplina

class Disciplina:
    def __init__(self, id, nume, nume_prof):
        """
        functie ce creeaza o entitate de tip disciplina
        :param id: un intreg
        :param nume: un string
        :param nume_prof: un string
        """
        self.__id=id
        self.__nume=nume
        self.__nume_prof=nume_prof

    def get_id(self):
        """
        functie ce returneaza id-ul unei discipline
        :return: id - un intreg reprezentand id-ul diciplinei
        """
        return self.__id

    def get_nume(self):
        """
        functie ce returneaza numele unei discipline
        :return: id - un intreg reprezentand id-ul disciplinei
        """
        return self.__nume
    def get_nume_prof(self):
        """
        functie ce returneaza numele profesorului
        :return: nume_prof - un string reprezentand numele profesorului
        """
        return self.__nume_prof
    def set_nume(self, nume_nou):
        """
        functie ce seteaza numele disciplinei la un nume nou
        :param nume_nou: -un string reprezentand numele nou
        :return: nimic - modifica in mod direct entitatea
        """
        self.__nume=nume_nou
    def set_nume_prof(self, nume_prof_nou):
        """
        functie ce seteaza numele profesorului disciplinei la un nume nou
        :param nume_prof_nou: - un string reprezentand numele nou al profesorului
        :return: nimic - modifica in mod direct entitatea
        """
        self.__nume_prof=nume_prof_nou

    def __eq__(self, other):
        """
        doua entitati Disciplina vor fi egale daca au acelasi ID
        :param other: - o disciplina
        :return: True - daca sunt egale, False contrar
        """
        try:
            return self.__id==other.__id
        except:
            return False
    def __str__(self):
        """
        functie ce returneaza string-ul specific unei entitati de tip Disciplina
        :return: "Disciplina - ID:*id*; Nume:*nume*; Nume profesor:*nume profesor*"
        """
        return "Disciplina - ID:"+str(self.__id)+"; Nume:"+self.__nume+"; Nume profesor:"+self.__nume_prof