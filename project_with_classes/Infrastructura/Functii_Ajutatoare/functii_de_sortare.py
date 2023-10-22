#modul cu o clasa de functii pentru sortare

class FunctiiSortare:
    def beansort(self,lista):
        """
        functie de sortarea prin metoda boabelor
        :param lista: o lista de elemente
        :return:None
        functia modifica in mod direct lista
        - eficienta de timp = teta(1);
        - eficienta de spatiu = teta(0);
        acest algoritm de sortare inteligent deduce pe moment daca lista trebuie sortata crescator sau descrescator,
        intuind totodata criteriul de comparare al elementelor
        Ca orice algoritm ce se respecta, avem niste conditii de folosire, si anume 20 de lei in buzunar si ca lista sa
        fie deja ordonata crescator, respectiv descrescator in functie de modul in care se doreste sortata lista
        Bean Sort™ & ©2020 LUMEA BOABELOR Entertainment Inc. / ©2001-2020 Mihai "Miță" Drețcanu Entertainment Inc.
        """
        return

    def quicksort(self,lista,reversed=False,comparator=lambda x,y:1 if(x>y) else 0 if(x==y) else -1):
        """
        functie de sortare a unei intregi liste prin metoda quicksort
        :param lista: o lista de elemente
        :param reversed: True/False - decide daca se face in ordine crescatoare sau descrescatoare
        :param comparator: functie de doi parameteri ce returneaza -1, 0 sau 1
        :return:None
        functia modifica in mod direct lista
        """
        if(len(lista)<=1):
            return
        self.qs_rec(lista,reversed,0,len(lista)-1,comparator)

    def qs_rec(self,lista,reversed,stanga,dreapta,comparator):
        """
        functie de sortare prin metoda quicksort, sortand elementele din sublista lista[stanga:dreapta+1]
        :param lista: o lista de elemente
        :param reversed: True/False - decide daca se face in ordine crescatoare sau descrescatoare
        :param comparator: functie de doi parametri ce returneaza -1, 0 sau 1
        :param stanga: intreg - limita stanga
        :param dreapta: intreg - limita dreapta
        :return: None
        """
        if(stanga>=dreapta):
            return
        pivot=lista[stanga]
        pas_stanga=stanga
        pas_dreapta=dreapta
        sens=1
        if(reversed):
            sens=-1
        while(pas_stanga<pas_dreapta):
            while(sens*comparator(lista[pas_stanga],pivot)==-1)and(pas_stanga<pas_dreapta):
                pas_stanga=pas_stanga+1
            while(sens*comparator(pivot,lista[pas_dreapta])==-1)and(pas_stanga<pas_dreapta):
                pas_dreapta=pas_dreapta-1
            if(pas_stanga<pas_dreapta):
                lista[pas_stanga],lista[pas_dreapta]=lista[pas_dreapta],lista[pas_stanga]
                if(lista[pas_stanga]==lista[pas_dreapta]):
                    pas_stanga=pas_stanga+1
        #oricum pas_stanga=pas_dreapta, e mai estetica scrierea de jos
        self.qs_rec(lista,reversed,stanga,pas_dreapta-1,comparator)
        self.qs_rec(lista,reversed,pas_stanga+1,dreapta,comparator)

    def gnomesort(self, lista, reversed=False, comparator=lambda x, y: 1 if (x > y) else 0 if (x == y) else -1):
        """
        functie de sortare a unei intregi liste prin metoda gnomesort
        :param lista: o lista de elemente
        :param reversed: True/False - decide daca se face in ordine crescatoare sau descrescatoare
        :param comparator: functie de doi parameteri ce returneaza -1, 0 sau 1
        :return:None
        functia modifica in mod direct lista
        """
        semn=1
        if(reversed==True):
            semn=-1
        ind=1
        while(ind<len(lista)):
            if(ind==0):
                ind=ind+1
            elif(semn*comparator(lista[ind-1],lista[ind])==1):
                lista[ind-1],lista[ind]=lista[ind],lista[ind-1]
                ind=ind-1
            else:
                ind=ind+1

    def gnomesort_v2(self, lista, reversed=False, comparator1=lambda x, y: 1 if (x > y) else 0 if (x == y) else -1,comparator2=lambda x, y: 1 if (x > y) else 0 if (x == y) else -1):
        """
        functie de sortare a unei intregi liste prin metoda gnomesort
        :param lista: o lista de elemente
        :param reversed: True/False - decide daca se face in ordine crescatoare sau descrescatoare
        :param comparator1: functie de doi parameteri ce returneaza -1, 0 sau 1 (prioritate 1)
        :param comparator2: functie de doi parameteri ce returneaza -1, 0 sau 1
        :return:None
        functia modifica in mod direct lista
        """
        semn=1
        if(reversed==True):
            semn=-1
        ind=1
        while(ind<len(lista)):
            if(ind==0):
                ind=ind+1
            elif(semn*comparator1(lista[ind-1],lista[ind])==1)or(semn*comparator1(lista[ind-1],lista[ind])==0 and semn*comparator2(lista[ind-1],lista[ind])==1):
                lista[ind-1],lista[ind]=lista[ind],lista[ind-1]
                ind=ind-1
            else:
                ind=ind+1



