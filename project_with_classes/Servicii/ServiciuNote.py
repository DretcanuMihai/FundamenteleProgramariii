#modul cu serviciu pentru note

from Domeniu.Entitati.Entitate_Nota import Nota
from Infrastructura.Functii_Ajutatoare.functii_de_sortare import FunctiiSortare
from Infrastructura.Functii_Ajutatoare.functii_de_comparare import comparare_nume_id,comparare_valoare_id,comparare_medie_id,comparare_medie_alfabetic_profesori,comparare_string,comparare_float_invers

class ServiciuNote:
    def __init__(self, repo_note,repo_stud,repo_dis,valid_note):
        self.__repo_note=repo_note
        self.__repo_stud=repo_stud
        self.__repo_dis=repo_dis
        self.__valid_note=valid_note

    def nr_note(self):
        """
        functie ce returneaza numarul de note din repo
        :return: intreg reprezentand numarul de note
        """
        return len(self.__repo_note)

    def get_all(self):
        """
        functie ce returneaza o lista cu toate notele din repo
        :return: lista de note
        """
        return self.__repo_note.get_all()

    def get_all_stud(self):
        """
        functie ce returneaza o lista cu toti studentii din repo
        :return: lista de entitati Student
        """
        return self.__repo_stud.get_studenti()

    def get_all_dis(self):
        """
        functie ce returneaza o lista cu toate disciplinele din repo
        :return:lista de entitati Disciplina
        """
        return self.__repo_dis.get_discipline()

    def get_all_for_print(self):
        """
        functie ce returneaza o lista de liste ce contin nota, studentul si disciplina notei
        :return: lista de liste ce contin nota, studentul si disciplina
        """
        l=self.get_all()
        L=[]
        for i in range(0,len(l)):
            elem=l[i]
            stud=self.__repo_stud.cauta(elem.get_id_student())
            dis=self.__repo_dis.cauta(elem.get_id_disciplina())
            L.append([elem,stud,dis])
        return L

    def adauga_nota(self,id_stud,id_dis,valoare):
        """
        functie ce adauga o nota in repo de note
        :param id_stud: intreg, id-ul studentului caruia ii apartine nota
        :param id_dis: intreg, id-ul disciplinei la care este nota
        :param valoare: float reprezentand valoare anotei
        :return: nimic, se modifica direct repo-ul
        se vor ridica exceptiile potrivite daca apare cazul
        """
        nota=Nota(id_stud,id_dis,valoare)
        self.__valid_note.validare(nota)
        self.__repo_stud.cauta(id_stud)
        self.__repo_dis.cauta(id_dis)
        self.__repo_note.adauga_nota(nota)

    def sterge_student(self,id_stud):
        """
        functie ce sterge un student si toate notele acestuia dupa id
        :param id_stud: intreg, id-ul studentului de sters
        :return: nimic, se modifica direct repo-urile
        se vor ridica exceptiile potrivite daca apare cazul
        """
        self.__valid_note.validare_id_stud(id_stud)
        self.__repo_stud.sterge(id_stud)
        l=self.get_all()
        i=0
        while(i<len(l)):
            elem=l[i]
            if(elem.get_id_student()==id_stud):
                self.__repo_note.sterge_nota(id_stud,elem.get_id_disciplina())
            else:
                i=i+1

    def sterge_disciplina(self,id_dis):
        """
        functie ce sterge o disciplina si toate notele acesteia dupa id
        :param id_dis: intreg, id-ul disciplinei de sters
        :return: nimic, se modifica direct repo-urile
        se vor ridica exceptiile potrivite daca apare cazul
        """
        self.__valid_note.validare_id_dis(id_dis)
        self.__repo_dis.sterge(id_dis)
        l=self.get_all()
        i=0
        while(i<len(l)):
            elem=l[i]
            if(elem.get_id_disciplina()==id_dis):
                self.__repo_note.sterge_nota(elem.get_id_student(),id_dis)
            else:
                i=i+1

    def raport_disciplina_aflabetic(self, id_dis):
        """
        functie ce formeaza o lista cu toti studentii si nota lor la o disciplina luata dupa id_dis, sau None daca nu au
        nota, ordonata alfabetic dupa numele studentilor, iar prima pozitie din lista contine disciplina in sine
        :param id_dis:id-ul disciplinei
        :return: o lista cu toti studentii si nota lor la o disciplina luata dupa id_dis, sau None daca nu au
        nota, ordonata alfabetic dupa numele studentilor, iar prima pozitie din lista contine disciplina in sine
        daca apar erori, acestea vor fi ridicate
        """
        self.__valid_note.validare_id_dis(id_dis)
        disciplina=self.__repo_dis.cauta(id_dis)
        LS=self.get_all_stud()
        L=[]
        for stud in LS:
            try:
                nota=self.__repo_note.cauta_nota(stud.get_id(),id_dis)
                aux=[stud, nota]
            except:
                aux=[stud,None]
            L.append(aux)
        FunctiiSortare().quicksort(L,comparator=comparare_nume_id)
        L=[disciplina]+L
        return L

    def raport_disciplina_descrescator(self, id_dis):
        """
        functie ce formeaza o lista cu toti studentii si nota lor la o disciplina luata dupa id_dis, sau None daca nu au
        nota, ordonata descrescator dupa nota, iar prima pozitie din lista contine disciplina in sine
        :param id_dis:id-ul disciplinei
        :return: o lista cu toti studentii si nota lor la o disciplina luata dupa id_dis, sau None daca nu au
        nota, ordonata descrescator dupa nota, iar prima pozitie din lista contine disciplina in sine
        Daca apar erori, acestea vor fi ridicate (ValidatorNotaException daca id-ul nu este valid si
        RepDisException daca nu exista disciplina - erorile vor aparea in aceasta ordine)
        """
        self.__valid_note.validare_id_dis(id_dis)
        disciplina=self.__repo_dis.cauta(id_dis)
        L=[]
        LS=self.get_all_stud()
        for stud in LS:
            try:
                nota=self.__repo_note.cauta_nota(stud.get_id(),id_dis)
                aux=[stud, nota]
            except:
                aux=[stud,Nota(None,None,0)]
            L.append(aux)
        FunctiiSortare().gnomesort(L,reversed=True,comparator=comparare_valoare_id)
        for i in range(0,len(L)):
            if(L[i][1].get_valoare()==0):
                L[i][1]=None
        L=[disciplina]+L
        return L

    def raport_20_la_suta(self):
        """
        functie ce afla care sunt primii 20% din studenti dupa media lor la toate disciplinele (daca elevul nu are note,
        media este considerata 0)
        :return:lista formate din liste ce contin pe prima pozitie studentul, iar pe a doua pozitie media studentului
        """
        LREZ=[]
        LS=self.get_all_stud()
        L=self.get_all()
        for elem in LS:
            valoare=0
            contor=0
            for elem_L in L:
                if(elem_L.get_id_student()==elem.get_id()):
                    valoare=valoare+elem_L.get_valoare()
                    contor=contor+1
            if(contor!=0):
                medie=valoare/contor
                medie=round(medie,2)
            else:
                medie=0.0
            LREZ.append([elem,medie])
        FunctiiSortare().quicksort(LREZ,reversed=True,comparator=comparare_medie_id)
        #am ordonat descrescator dupa medie elevii
        nrstud=len(LREZ)
        proc=nrstud//5
        if(nrstud%5!=0):
            proc=proc+1
        LREZ=LREZ[0:proc]
        return LREZ

    def raport_profesori_descrescator(self):
        """
        functie ce determina o lista cu toti profesorii ordonati dupa medie descrescator (daca doua medii sunt egale,
        dupa nume), si media notelor date de ei (daca nu a dat note, media este 0.0)
        :return: o lista formata din liste ce au pe prima pozitia un string ce reprezinta numele profesorului, iar pe
        a doua pozitie un float ce tine minte media
        """
        LD=self.get_all_dis()
        LP=[]
        for elem in LD:
            if(elem.get_nume_prof() not in LP):
                LP.append(elem.get_nume_prof())
        #am determinat care sunt toti profesorii
        LN=self.get_all_for_print()
        LREZ=[]
        for prof in LP:
            medie=0.0
            contor=0
            for elem in LN:
                if(elem[2].get_nume_prof()==prof):
                    contor=contor+1
                    medie=medie+elem[0].get_valoare()
            if(contor!=0):
                medie=medie/contor
                medie=round(medie,2)
            LREZ.append([prof,medie])
        FunctiiSortare().gnomesort_v2(LREZ,comparator1=comparare_float_invers,comparator2=comparare_string)
        return LREZ