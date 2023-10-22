
def comparare_nume_id(x,y):
    """
    functie de comparare a doua liste x,y ce contin pe prima pozitie o entitate de tip student, iar pe a doua pozitie
    o entitate de tip nota; mai intai compara numele studentilor alfabetic, apoi id-urile lor
    :param x: lista ce contine pe prima pozitie o entitate de tip student, iar pe a doua o entitate de tip nota
    :param y: lista ce contine pe prima pozitie o entitate de tip student, iar pe a doua o entitate de tip nota
    :return: 1 - daca x>y; 0 - daca x=y; -1 - daca x<1
    """
    if(x[0].get_nume()>y[0].get_nume()):
        return 1
    elif(x[0].get_nume()==y[0].get_nume()):
        if(x[0].get_id()>y[0].get_id()):
            return 1
        elif(x[0].get_id()==y[0].get_id()):
            return 0
        else:
            return -1
    else:
        return -1

def comparare_valoare_id(x,y):
    """
    functie de comparare a doua liste x,y ce contin pe prima pozitie o entitate de tip student, iar pe a doua pozitie
    un float ce reprezinta o nota; mai intai compara valoarea notei, apoi descrescator id-urile
    :param x: lista ce contine pe prima pozitie o entitate de tip student, iar pe a doua o entitate de tip nota
    :param y: lista ce contine pe prima pozitie o entitate de tip student, iar pe a doua o entitate de tip nota
    :return: 1 - daca x>y; 0 - daca x=y; -1 - daca x<1
    """
    if(x[1].get_valoare()>y[1].get_valoare()):
        return 1
    elif(x[1].get_valoare()==y[1].get_valoare()):
        if(x[0].get_id()<y[0].get_id()):
            return 1
        elif(x[0].get_id()==y[0].get_id()):
            return 0
        else:
            return -1
    else:
        return -1

def comparare_medie_id(x,y):
    """
    functie de comparare a doua liste x,y ce contin pe prima pozitie o entitate de tip student, iar pe a doua pozitie
    un float ce reprezinta media; mai intai compara valoarea mediei, apoi descrescator id-urile
    :param x: lista ce contine pe prima pozitie o entitate de tip student, iar pe a doua un float
    :param y: lista ce contine pe prima pozitie o entitate de tip student, iar pe a doua un float
    :return: 1 - daca x>y; 0 - daca x=y; -1 - daca x<1
    """
    if(x[1]>y[1]):
        return 1
    elif(x[1]==y[1]):
        if(x[0].get_id()<y[0].get_id()):
            return 1
        elif(x[0].get_id()==y[0].get_id()):
            return 0
        else:
            return -1
    else:
        return -1

def comparare_medie_alfabetic_profesori(x,y):
    """
    functie de comparare a doua liste x,y ce contin pe prima pozitie un string, iar pe a doua pozitie
    un intreg ce reprezinta media; mai intai compara valoarea mediei, apoi invers alfabetic string-urile
    :param x: lista ce contine pe prima pozitie un string, iar pe a doua un intreg
    :param y: lista ce contine pe prima pozitie o entitate de tip student, iar pe a doua un intreg
    :return: 1 - daca x>y; 0 - daca x=y; -1 - daca x<1
    """
    if(x[1]>y[1]):
        return 1
    elif(x[1]==y[1]):
        if(x[0]<y[0]):
            return 1
        elif(x[0]==y[0]):
            return 0
        else:
            return -1
    else:
        return -1

def comparare_float_invers(x,y):
    if(x[1]>y[1]):
        return -1
    elif(abs(x[1]-y[1])<0.000001):
        return 0
    else:
        return 1

def comparare_string(x,y):
    if(x>y):
        return 1
    elif(x==y):
        return 0
    else:
        return -1