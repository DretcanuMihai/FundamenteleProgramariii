
def comparator_1(m1,m2):
    """
    functia compara doua melodii astfel: m1<m2 daca numele artistului lui m1 este mai mic lexicografic ca numele
     artistului lui m2; daca artistii sunt egali, m1<m2 daca titlul piesei m1 este mai mic lexicografic ca ce al lui
     m2
    :param m1: melodie
    :param m2: melodie
    :return: True/False - True daca este "mai mic" m1 ca m2, False contrar
    """
    if(m1.get_artist()<m2.get_artist()):
        return True
    elif m1.get_artist()==m2.get_artist():
        if(m1.get_titlu()<m2.get_titlu()):
            return True
        else:
            return False
    else:
        return False