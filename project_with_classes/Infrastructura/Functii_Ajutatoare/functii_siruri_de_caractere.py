#modul cu o clasa de functii ce opereaza pe siruri de caractere

from random import randint

class FunctiiSiruriCaractere:
    def nume_corect(self, sir):
        """
        functie ce verifica daca un sir reprezinta un nume corect (sir nevid, primul caracter este o litera mare, iar
        restul caracterelor sunt litere mici)
        :param sir: sirul de caractere ce il verificam
        :return: True - daca este un nume valid; False in caz contrar
        """
        if(sir==""):
            return False
        if(sir[0]<"A" or sir[0]>"Z"):
            return False
        for i in range (1,len(sir)):
            if(sir[i]<"a" or sir[i]>"z"):
                return False
        return True

    def fn_corect(self, sir):
        """
        functie ce verifica daca un string reprezinta un format de nume corect ("Nume Prenume")
        :param sir: string-ul de verificat
        :return: True - daca este un format de nume valid; False in caz contrar
        """
        sirv=sir.split(" ")
        if(len(sirv)!=2):
            return False
        return (self.nume_corect(sirv[0])and self.nume_corect(sirv[1]))

    def fd_corect(self, sir):
        """
        functie ce verifica daca un string reprezinta un format de denumire corect(adica sa fie un string nenul de
        cuvinte, despartite printr-un spatiu, unica majuscula a cuvintelor fiind prima litera
        :param sir: string-ul de verificat
        :return: True - daca este un format de denumire valid; False in caz contrar
        """
        sirv=sir.split(" ")
        for elem in sirv:
            if(self.nume_corect(elem)==False):
                return False
        return True

    def rand_cuv(self):
        """
        functie ce genereaza un cuvant aleatoriu valid
        :return: cuv - sir random
        """
        lit_mare="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lit_mica="abcdefghijklmnopqrstuvwxyz"
        cuv = lit_mare[randint(0, 25)]
        nr_lit = randint(0, 8)
        while (nr_lit):
            cuv = cuv + lit_mica[randint(0, 25)]
            nr_lit = nr_lit - 1
        return cuv